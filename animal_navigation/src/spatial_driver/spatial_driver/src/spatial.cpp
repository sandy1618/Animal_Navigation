#include "spatial_driver/spatial.h"

Spatial::Spatial()
    : nh_()
    , pnh_("~")
    , publish_tf_(false)
    , use_ros_frame_convention_(true)
    , output_raw_anpp_(false)
    , anpp_output_path_(".")
    , port_(io_service_)
    , an_decoder_()
    , raw_sensors_packet_()
    , geodetic_position_packet_()
    , euler_orientation_packet_()
    , quaternion_orientation_packet_()
    , raw_gnss_packet_()
    , detailed_satellites_packet_()
{
    unsigned baudrate;
    std::string topic_prefix;
    bool cold_start;
    pnh_.param("port", port_name_, std::string("/dev/ttyUSB0"));
    pnh_.param("frame_id", frame_id_, std::string("spatial"));
    pnh_.param("publish_tf", publish_tf_, false);
    pnh_.param("tf_parent_frame_id", tf_parent_frame_id_,
               std::string("base_link"));
    pnh_.param("tf_child_frame_id", tf_child_frame_id_, frame_id_);
    pnh_.param("use_device_timestamp", use_device_timestamp_, false);
    pnh_.param("use_ros_frame_convention", use_ros_frame_convention_, true);
    pnh_.param("cold_start", cold_start, false);
    pnh_.param("output_raw_anpp", output_raw_anpp_, false);
    pnh_.param("anpp_output_path", anpp_output_path_, std::string("."));
    pnh_.param("topic_prefix", topic_prefix, frame_id_);
    // 115200 baud is not sufficient for 200Hz sampling of IMU.
    // See "Spatial Reference Manual, 13.5 Packet Rates".
    int baudrate_tmp;
    pnh_.param("baudrate", baudrate_tmp, 1000000);
    baudrate = static_cast<unsigned>(baudrate_tmp);

    port_.open(port_name_);
    port_.set_option(boost::asio::serial_port_base::baud_rate(baudrate));

    if (output_raw_anpp_) {
        raw_anpp_.open(get_anpp_filename(anpp_output_path_));
    }

    an_packet_t* an_packet;

    // Set Baud Rate
    // Note:
    baud_rates_packet_t baud_rate_packet;
    baud_rate_packet.permanent = 1;
    baud_rate_packet.primary_baud_rate = baudrate;
    baud_rate_packet.gpio_1_2_baud_rate = baudrate;
    baud_rate_packet.auxiliary_baud_rate = baudrate;
    baud_rate_packet.reserved = 0;
    an_packet = encode_baud_rates_packet(&baud_rate_packet);
    an_packet_encode_and_send(an_packet);
    an_packet_free(&an_packet);
    wait_for_acknowledge(packet_id_e::packet_id_baud_rates);

    // Setup packet rate timer
    packet_timer_period_packet_t packet_timer_period_packet;
    packet_timer_period_packet.permanent = 1;
    packet_timer_period_packet.packet_timer_period = 1000; // 1 ms
    an_packet = encode_packet_timer_period_packet(&packet_timer_period_packet);
    an_packet_encode_and_send(an_packet);
    an_packet_free(&an_packet);
    wait_for_acknowledge(packet_id_e::packet_id_packet_timer_period);

    packet_periods_packet_t packet_periods_packet;
    if (pnh_.hasParam("packets")) {
        packet_periods_packet = set_packet_periods();
    }
    else {
        packet_periods_packet = set_default_packet_periods();
    }
    an_packet = encode_packet_periods_packet(&packet_periods_packet);
    an_packet_encode_and_send(an_packet);
    an_packet_free(&an_packet);
    wait_for_acknowledge(packet_id_e::packet_id_packet_periods);

    if (cold_start) {
        // Cold-start the device to reflect the changes
        an_packet = encode_reset_packet();
        // See Reference 13.8.6.1 Verification Sequence Values
        uint32_t verification = 0x9A5D38B7; //cold start reset
        std::memcpy(&an_packet->data[0], &verification, sizeof(uint32_t));
        an_packet_encode_and_send(an_packet);
        an_packet_free(&an_packet);
        wait_for_acknowledge(packet_id_e::packet_id_reset);
    }
    else {
        // hot-start the device to reflect the changes
        an_packet = encode_reset_packet();
        // See Reference 13.8.6.1 Verification Sequence Values
        uint32_t verification = 0x21057A7E; //hot start reset
        std::memcpy(&an_packet->data[0], &verification, sizeof(uint32_t));
        an_packet_encode_and_send(an_packet);
        an_packet_free(&an_packet);
        wait_for_acknowledge(packet_id_e::packet_id_reset);
    }
    
    // Setup ROS topic
    imu_raw_pub_ = nh_.advertise<sensor_msgs::Imu>(topic_prefix + "/imu", 10);
    magnetic_field_pub_ = nh_.advertise<sensor_msgs::MagneticField>(
        topic_prefix + "/mag", 10);
    temperature_pub_ = nh_.advertise<sensor_msgs::Temperature>(
        topic_prefix + "/temp", 10);
    pressure_pub_ = nh_.advertise<sensor_msgs::FluidPressure>(
        topic_prefix + "/pressure", 10);
    gnss_position_pub_ = nh_.advertise<sensor_msgs::NavSatFix>(
        topic_prefix + "/fix", 10);
    gnss_raw_pub_ = nh_.advertise<std_msgs::String>(
        topic_prefix + "/raw_gnss_packet", 5);
    posture_pub_ = nh_.advertise<geometry_msgs::Vector3Stamped>(
        topic_prefix + "/posture", 10);
    detailed_satellites_pub_ = nh_.advertise<std_msgs::Int32>(
        topic_prefix + "/number_of_satellites", 10);

    an_decoder_initialise(&an_decoder_);

    raw_sensors_received_ = false;
    euler_orientation_received_ = false;
    quaternion_orientation_received_ = false;
    geodetic_position_received_ = false;
    raw_gnss_received_ = false;
    detailed_satellites_received_ = false;
}

Spatial::~Spatial() {
    raw_anpp_.close();
}

void
Spatial::spin() {
    while (ros::ok()) {
        ros::spinOnce();
        bool packet_received = receive_next_packet();
        if (!packet_received) {
            continue;
        }

        // Decode all packets in buffer and publish them
        while (true) {
            current_header_.stamp = ros::Time::now();
            current_header_.frame_id = frame_id_;

            auto an_packet = an_packet_decode(&an_decoder_);
            if (an_packet == nullptr) {
                break;
            }

            process_packet(an_packet);
            publish();

            an_packet_free(&an_packet);
        }
    }
}

size_t
Spatial::an_packet_encode_and_send(an_packet_t* packet) {
    an_packet_encode(packet);
    // need cast to prevent autosizing of packet
    auto packet_ptr = reinterpret_cast<const void*>(an_packet_pointer(packet));
    auto packet_size = an_packet_size(packet);
    auto buf = boost::asio::buffer(packet_ptr, packet_size);
    return boost::asio::write(port_, buf);
}

bool
Spatial::receive_next_packet() {
    boost::system::error_code err_code;
    try {
        auto buffer_ptr = an_decoder_pointer(&an_decoder_);
        auto buffer_size = an_decoder_size(&an_decoder_);
        auto buf = boost::asio::buffer(buffer_ptr, buffer_size);
        size_t bytes_received = port_.read_some(buf, err_code);

        /* increment the decode buffer length by the number of bytes received */
        an_decoder_increment(&an_decoder_, bytes_received);

        if (output_raw_anpp_) {
            for (unsigned i = 0; i < bytes_received; i++) {
                raw_anpp_ << static_cast<uint8_t>(buffer_ptr[i]);
            }
        }
    }
    catch (std::exception& e) {
        ROS_FATAL_STREAM_THROTTLE(2, "Exception thrown: " << e.what());
        if (err_code == boost::asio::error::eof) {
            ROS_FATAL_STREAM_THROTTLE(2, "Maybe run: stty -F " << port_name_ << " raw");
        }
        return false;
    }

    return true;
}

void
Spatial::process_packet(an_packet_t* an_packet) {
    switch (an_packet->id) {
    case packet_id_boot_mode:
        boot_mode_packet_t boot_mode_packet;
        if (decode_boot_mode_packet(&boot_mode_packet, an_packet) != 0) {
            ROS_WARN("Boot Mode packet decode failure");
        }
        else {
            std::string boot_mode;
            if (boot_mode_packet.boot_mode == 0) {
                boot_mode = "Bootloader";
            }
            else if (boot_mode_packet.boot_mode == 1) {
                boot_mode = "Main Program";
            }
            ROS_DEBUG_STREAM("Boot mode: " << boot_mode);
        }
        break;
    case packet_id_system_state:
        system_state_packet_t system_state_packet;
        if (decode_system_state_packet(&system_state_packet, an_packet) != 0) {
            ROS_WARN("System state packet decode failure");
        }
        else {
            const auto secs = system_state_packet.unix_time_seconds;
            const auto usecs = system_state_packet.microseconds;
            if (use_device_timestamp_) {
                current_header_.stamp = ros::Time().fromSec(secs + usecs * 1e3);
            }
        }
        break;
    case packet_id_acknowledge:
        if (decode_acknowledge_packet(&acknowledge_packet_, an_packet) != 0) {
            ROS_WARN("Acknowledge packet decode failure");
        }
        else {
            acknowledge_received_ = true;
        }
        break;
    case packet_id_raw_sensors:
        if (decode_raw_sensors_packet(&raw_sensors_packet_, an_packet) != 0) {
            ROS_WARN("Raw sensors packet decode failure");
        }
        else {
            raw_sensors_received_ = true;
        }
        break;
    case packet_id_euler_orientation:
        if (decode_euler_orientation_packet(&euler_orientation_packet_, an_packet) != 0) {
            ROS_WARN("Euler orientation packet decode failure");
        }
        else {
            euler_orientation_received_ = true;
        }
        break;
    case packet_id_quaternion_orientation:
        if (decode_quaternion_orientation_packet(&quaternion_orientation_packet_, an_packet) != 0) {
            ROS_WARN("Quaternion orientation packet decode failure");
        }
        else {
            quaternion_orientation_received_ = true;
        }
        break;
    case packet_id_geodetic_position:
        if (decode_geodetic_position_packet(&geodetic_position_packet_, an_packet) != 0) {
            ROS_WARN("Geodetic position packet decode failure");
        }
        else {
            geodetic_position_received_ = true;
        }
        break;
    case packet_id_raw_gnss:
        if (decode_raw_gnss_packet(&raw_gnss_packet_, an_packet) != 0) {
            ROS_WARN("Raw GNSS packet decode failure");
        }
        else {
            raw_gnss_received_ = true;
        }
        break;
    case packet_id_satellites_detailed:
        if (decode_detailed_satellites_packet(&detailed_satellites_packet_, an_packet) != 0) {
            ROS_WARN("Detailed satellites packet decode failure");
        }
        else {
            detailed_satellites_received_ = true;
        }
        break;
    case packet_id_raw_satellite_data:
        // TODO: Implement me!
        break;
    default:
        ROS_WARN("Unknown packet id: %d", an_packet->id);
    }
}

void
Spatial::publish() {
    if (raw_sensors_received_ && quaternion_orientation_received_) {
        publish_imu_raw_msg();
        publish_magnetics_msg();
        publish_temperature_msg();
        publish_pressure_msg();
        raw_sensors_received_ = false;
    }
    if (euler_orientation_received_) {
        publish_posture_msg();
        euler_orientation_received_ = false;
    }
    if (geodetic_position_received_) {
        publish_gnss_position_msg();
        geodetic_position_received_ = false;
    }
    if (raw_gnss_received_) {
        publish_gnss_raw_msg();
        raw_gnss_received_ = false;
    }
    if (detailed_satellites_received_) {
        publish_detailed_satellites_msg();
        detailed_satellites_received_ = false;
    }
}

void
Spatial::publish_imu_raw_msg() {
    sensor_msgs::Imu imu_msg;
    geometry_msgs::Vector3 angular_velocity;
    geometry_msgs::Vector3 linear_acceleration;

    imu_msg.header.stamp = current_header_.stamp;
    imu_msg.header.frame_id = current_header_.frame_id;

    imu_msg.orientation_covariance[0] = -1;

    imu_msg.angular_velocity.x = raw_sensors_packet_.gyroscopes[0];
    imu_msg.angular_velocity.y = raw_sensors_packet_.gyroscopes[1];
    imu_msg.angular_velocity.z = raw_sensors_packet_.gyroscopes[2];
    imu_msg.angular_velocity_covariance[0] = -1;

    imu_msg.linear_acceleration.x = raw_sensors_packet_.accelerometers[0];
    imu_msg.linear_acceleration.y = raw_sensors_packet_.accelerometers[1];
    imu_msg.linear_acceleration.z = raw_sensors_packet_.accelerometers[2];
    imu_msg.linear_acceleration_covariance[0] = -1;

    imu_msg.orientation.w = quaternion_orientation_packet_.orientation[0];
    imu_msg.orientation.x = quaternion_orientation_packet_.orientation[1];
    imu_msg.orientation.y = quaternion_orientation_packet_.orientation[2];
    imu_msg.orientation.z = quaternion_orientation_packet_.orientation[3];

    if (use_ros_frame_convention_) {
        // Spatial's fixed frame convention has the x axis rotated 180 deg
        const auto& imu_o = imu_msg.orientation;
        tf2::Quaternion imu_q(imu_o.x, imu_o.y, imu_o.z, imu_o.w);

        // Rotate roll by 180 deg
        tf2::Quaternion flip_roll;
        flip_roll.setRPY(M_PI, 0, 0);

        // Apply rotation to the IMU message
        imu_q = flip_roll * imu_q;
        tf2::convert(imu_q, imu_msg.orientation);
    }

    if (publish_tf_) {
        geometry_msgs::TransformStamped tform;
        tform.header = imu_msg.header;
        tform.header.frame_id = tf_parent_frame_id_;
        tform.child_frame_id = tf_child_frame_id_;
        // Only publish the rotation
        tform.transform.rotation = imu_msg.orientation;
        tfb_.sendTransform(tform);
    }

    imu_raw_pub_.publish(imu_msg);
}

void
Spatial::publish_magnetics_msg() {
    sensor_msgs::MagneticField magnetic_field_msg;

    magnetic_field_msg.header.stamp = current_header_.stamp;
    magnetic_field_msg.header.frame_id = current_header_.frame_id;

    magnetic_field_msg.magnetic_field.x = raw_sensors_packet_.magnetometers[0] * (1.0e-7);
    magnetic_field_msg.magnetic_field.y = raw_sensors_packet_.magnetometers[1] * (1.0e-7);
    magnetic_field_msg.magnetic_field.z = raw_sensors_packet_.magnetometers[2] * (1.0e-7);

    magnetic_field_pub_.publish(magnetic_field_msg);
}

void
Spatial::publish_temperature_msg() {
    sensor_msgs::Temperature temp_msg;

    temp_msg.header.stamp = current_header_.stamp;
    temp_msg.header.frame_id = current_header_.frame_id;

    temp_msg.temperature = raw_sensors_packet_.imu_temperature;

    temperature_pub_.publish(temp_msg);
}

void
Spatial::publish_pressure_msg() {
    sensor_msgs::FluidPressure press_msg;

    press_msg.header.stamp = current_header_.stamp;
    press_msg.header.frame_id = current_header_.frame_id;

    press_msg.fluid_pressure = raw_sensors_packet_.pressure;

    pressure_pub_.publish(press_msg);
}

void
Spatial::publish_gnss_position_msg() {
    sensor_msgs::NavSatFix navsat_msg;

    navsat_msg.header.stamp = current_header_.stamp;
    navsat_msg.header.frame_id = current_header_.frame_id;

    navsat_msg.latitude = geodetic_position_packet_.position[0] * RADIANS_TO_DEGREES;
    navsat_msg.longitude = geodetic_position_packet_.position[1] * RADIANS_TO_DEGREES;
    navsat_msg.altitude = geodetic_position_packet_.position[2];
    navsat_msg.position_covariance[0] = -1;

    gnss_position_pub_.publish(navsat_msg);
}

void
Spatial::publish_gnss_raw_msg() {
    // TODO: Define custom message
    std_msgs::String rawgnss_msg;

    char str[1024];
    sprintf(str, "%d.%d,%lf,%lf,%lf,%f,%f,%f,%f,%f,%f,%d,%d,%d,%d",
            raw_gnss_packet_.unix_time_seconds,
            raw_gnss_packet_.microseconds,
            raw_gnss_packet_.position[0] * RADIANS_TO_DEGREES,
            raw_gnss_packet_.position[1] * RADIANS_TO_DEGREES,
            raw_gnss_packet_.position[2],
            raw_gnss_packet_.velocity[0],
            raw_gnss_packet_.velocity[1],
            raw_gnss_packet_.velocity[2],
            raw_gnss_packet_.position_standard_deviation[0],
            raw_gnss_packet_.position_standard_deviation[1],
            raw_gnss_packet_.position_standard_deviation[2],
            raw_gnss_packet_.flags.b.fix_type,
            raw_gnss_packet_.flags.b.velocity_valid,
            raw_gnss_packet_.flags.b.time_valid,
            raw_gnss_packet_.flags.b.external_gnss);
    rawgnss_msg.data = str;

    gnss_raw_pub_.publish(rawgnss_msg);
}

void
Spatial::publish_posture_msg() {
    geometry_msgs::Vector3Stamped posture_msg;

    posture_msg.header.stamp = current_header_.stamp;
    posture_msg.header.frame_id = current_header_.frame_id;

    posture_msg.vector.x = euler_orientation_packet_.orientation[0] * RADIANS_TO_DEGREES;
    posture_msg.vector.y = euler_orientation_packet_.orientation[1] * RADIANS_TO_DEGREES;
    posture_msg.vector.z = euler_orientation_packet_.orientation[2] * RADIANS_TO_DEGREES;

    posture_pub_.publish(posture_msg);
}

void
Spatial::publish_detailed_satellites_msg() {
    std_msgs::Int32 detailed_satellites_msg;

    int number_of_satellites;
    number_of_satellites = detailed_satellites_packet_.number_of_satellites;
    detailed_satellites_msg.data = number_of_satellites;
    detailed_satellites_pub_.publish(detailed_satellites_msg);
}

packet_periods_packet_t
Spatial::set_packet_periods() {
    packet_periods_packet_t packet_periods_packet;

    packet_periods_packet.permanent = 1;
    packet_periods_packet.clear_existing_packets = 1;

    XmlRpc::XmlRpcValue v;
    pnh_.getParam("packets", v);
    int idx;
    for (idx = 0; idx < v.size(); idx++) {
        auto& packet = v[idx];

        auto& packet_periods = packet_periods_packet.packet_periods[idx];
        using packet_id_t = decltype(packet_periods.packet_id);
        using period_t = decltype(packet_periods.period);

        auto int_id = static_cast<int>(packet["id"]);
        auto packet_id = static_cast<packet_id_t>(int_id);
        period_t period;
        if (packet.hasMember("period_ms")) {
            auto period_ms = static_cast<int>(packet["period_ms"]);
            period = static_cast<period_t>(period_ms);
        }
        else if (packet.hasMember("hz")) {
            double hz;
            if (packet.getType() == XmlRpc::XmlRpcValue::TypeDouble) {
                hz = static_cast<double>(packet["hz"]);
            }
            else {
                hz = static_cast<int>(packet["hz"]);
            }
            period = static_cast<period_t>(1000 / hz);
        }
        else {
            ROS_WARN_STREAM("ID " << static_cast<int>(packet_id)
                                  << ": specify period_ms or hz");
            continue;
        }

        packet_periods.packet_id = packet_id;
        packet_periods.period = period;

        auto hz = static_cast<unsigned>(1000 / period);
        ROS_INFO_STREAM("ID " << std::setw(3) << static_cast<int>(packet_id)
                              << " at " << std::setw(4) << hz << " hz");
    }

    // Last entry should have packet_id == 0
    packet_periods_packet.packet_periods[idx].packet_id = 0;

    return packet_periods_packet;
}

packet_periods_packet_t
Spatial::set_default_packet_periods() {
    packet_periods_packet_t packet_periods_packet;

    packet_periods_packet.permanent = 1;
    packet_periods_packet.clear_existing_packets = 1;
    // ID: 20 @ 200 Hz
    packet_periods_packet.packet_periods[0].packet_id = packet_id_system_state;
    packet_periods_packet.packet_periods[0].period = 5;
    // ID: 28 @ 200 Hz
    packet_periods_packet.packet_periods[1].packet_id = packet_id_raw_sensors;
    packet_periods_packet.packet_periods[1].period = 5;
    // ID: 29 @ 10 Hz
    packet_periods_packet.packet_periods[2].packet_id = packet_id_raw_gnss;
    packet_periods_packet.packet_periods[2].period = 100;
    // ID: 31 @ 10 Hz
    packet_periods_packet.packet_periods[3].packet_id = packet_id_satellites_detailed;
    packet_periods_packet.packet_periods[3].period = 100;
    // ID: 32 @ 10 Hz
    packet_periods_packet.packet_periods[4].packet_id = packet_id_geodetic_position;
    packet_periods_packet.packet_periods[4].period = 100;
    // ID: 39 @ 200 Hz
    packet_periods_packet.packet_periods[5].packet_id = packet_id_euler_orientation;
    packet_periods_packet.packet_periods[5].period = 5;
    // ID: 40 @ 200 Hz
    packet_periods_packet.packet_periods[6].packet_id = packet_id_quaternion_orientation;
    packet_periods_packet.packet_periods[6].period = 5;
    // ID: 60 @ 10 Hz
    packet_periods_packet.packet_periods[7].packet_id = packet_id_raw_satellite_data;
    packet_periods_packet.packet_periods[7].period = 100;

    // packet_id == 0 to indicate end
    packet_periods_packet.packet_periods[8].packet_id = 0;

    return packet_periods_packet;
}

void
Spatial::wait_for_acknowledge(const packet_id_e& packet_id) {
    while (ros::ok()) {
        bool packet_received = receive_next_packet();
        if (!packet_received) {
            continue;
        }

        // Decode all packets in buffer and publish them
        while (true) {
            current_header_.stamp = ros::Time::now();
            current_header_.frame_id = frame_id_;

            auto an_packet = an_packet_decode(&an_decoder_);
            if (an_packet == nullptr) {
                break;
            }

            process_packet(an_packet);

            if (acknowledge_received_) {
                const auto ack_packet_id = static_cast<int>(acknowledge_packet_.packet_id);
                const auto result = acknowledge_packet_.acknowledge_result;
                if (ack_packet_id != packet_id) {
                    ROS_WARN_STREAM("Expected packet ID "
                                            << packet_id
                                            << " but got "
                                            << ack_packet_id);
                    // Go on to the next packet (if it exists in the buffer)
                    continue;
                }
                // Acknowledge success == 0
                else if (result != 0) {
                    ROS_ERROR_STREAM("Acknowledge result " << result);
                }
                ROS_INFO_STREAM("Acknowledge OK");
                return;
            }

            an_packet_free(&an_packet);
        }
    }
}

std::string
Spatial::get_anpp_filename(const std::string& formatted_path) {
    using namespace boost::posix_time;

    // Current ROS time, in UTC
    const auto curr_ptime = ros::Time::now().toBoost();
    using c_adjustor = boost::date_time::c_local_adjustor<ptime>;
    const auto curr_local_ptime = c_adjustor::utc_to_local(curr_ptime);

    time_facet* facet;
    std::ostringstream file_path;
    // File name specified
    if (ends_with(formatted_path, ".anpp")) {
        facet = new time_facet(formatted_path.c_str());
        file_path.imbue(std::locale(file_path.getloc(), facet));
        file_path << curr_local_ptime;
    }
    // Directory name specified
    else {
        facet = new time_facet("%Y-%m-%dT%H-%M-%S");
        file_path.imbue(std::locale(file_path.getloc(), facet));
        file_path << formatted_path
            << boost::filesystem::path::preferred_separator
            << curr_local_ptime << ".anpp";
    }
    return file_path.str();
}

bool
Spatial::ends_with(const std::string& s, const std::string& suffix) {
    if (s.size() < suffix.size()) {
        return false;
    }
    const auto size_diff = s.size() - suffix.size();
    return s.compare(size_diff, suffix.size(), suffix) == 0;
}
