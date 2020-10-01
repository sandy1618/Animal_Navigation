#include "spatial_sdk_c/an_packet_protocol.h"
#include "spatial_sdk_c/spatial_packets.h"

#include <ros/ros.h>
#include <tf2/LinearMath/Quaternion.h>
#include <tf2_ros/transform_broadcaster.h>
#include <tf2/transform_datatypes.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>
#include <sensor_msgs/Imu.h>
#include <sensor_msgs/MagneticField.h>
#include <sensor_msgs/Temperature.h>
#include <sensor_msgs/FluidPressure.h>
#include <sensor_msgs/NavSatFix.h>
#include <sensor_msgs/NavSatStatus.h>
#include <geometry_msgs/Vector3Stamped.h>
#include <geometry_msgs/TransformStamped.h>
#include <std_msgs/String.h>
#include <std_msgs/Int32.h>

#include <cstdlib>
#include <cstdio>
#include <cstdint>
#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

#include <boost/asio.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>
#include <boost/date_time/c_local_time_adjustor.hpp>
#include <boost/filesystem.hpp>

#define RADIANS_TO_DEGREES (180.0/M_PI)

class Spatial {
public:
    Spatial();

    ~Spatial();

    void
    spin();

private:
    size_t
    an_packet_encode_and_send(an_packet_t* packet);

    bool
    receive_next_packet();

    void
    process_packet(an_packet_t* an_packet);

    void
    publish();

    void
    publish_imu_raw_msg();

    void
    publish_magnetics_msg();

    void
    publish_temperature_msg();

    void
    publish_pressure_msg();

    void
    publish_gnss_position_msg();

    void
    publish_gnss_raw_msg();

    void
    publish_posture_msg();

    void
    publish_detailed_satellites_msg();

    packet_periods_packet_t
    set_packet_periods();

    packet_periods_packet_t
    set_default_packet_periods();

    void
    wait_for_acknowledge(const packet_id_e& packet_id);

    /**
     * Given a path in the strftime format, return the path to an anpp file
     *
     * If the given path endswith .anpp, it is considered to be a path to
     * a file, and datetime format expansion is performed. Otherwise, the
     * given path is assumed to be a directory name, and filename in the
     * format %Y-%m-%dT%H-%M-%S.anpp is appended to become the path.
     * @param formatted_path path to a file or directory, with strftime
     * @return file path, with the datetime format expanded
     */
    std::string
    get_anpp_filename(const std::string& formatted_path);

    bool
    ends_with(const std::string& s, const std::string& suffix);

    ros::NodeHandle nh_;
    ros::NodeHandle pnh_;
    std::string frame_id_;
    bool publish_tf_;
    std::string tf_parent_frame_id_;
    std::string tf_child_frame_id_;
    bool use_device_timestamp_;
    bool use_ros_frame_convention_;
    bool output_raw_anpp_;
    std::string anpp_output_path_;
    tf2_ros::TransformBroadcaster tfb_;
    ros::Publisher imu_raw_pub_;
    ros::Publisher magnetic_field_pub_;
    ros::Publisher temperature_pub_;
    ros::Publisher pressure_pub_;
    ros::Publisher posture_pub_;
    ros::Publisher gnss_position_pub_;
    ros::Publisher gnss_raw_pub_;
    ros::Publisher detailed_satellites_pub_;

    boost::asio::io_service io_service_;
    std::string port_name_;
    boost::asio::serial_port port_;
    an_decoder_t an_decoder_; // Packet decoder given by SpatialSDK.
    std_msgs::Header current_header_;

    std::ofstream raw_anpp_;

    // Packets of Spatial.

    acknowledge_packet_t acknowledge_packet_;
    raw_sensors_packet_t raw_sensors_packet_; // including pressure (float)
    geodetic_position_packet_t geodetic_position_packet_; // lat, lon, alt
    euler_orientation_packet_t euler_orientation_packet_;
    quaternion_orientation_packet_t quaternion_orientation_packet_;
    raw_gnss_packet_t raw_gnss_packet_;
    device_information_packet_t device_information_packet_;
    detailed_satellites_packet_t detailed_satellites_packet_;
    bool acknowledge_received_;
    bool raw_sensors_received_;
    bool geodetic_position_received_;
    bool euler_orientation_received_;
    bool quaternion_orientation_received_;
    bool raw_gnss_received_;
    bool detailed_satellites_received_;
};
