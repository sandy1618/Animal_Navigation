#include <ros/ros.h>
#include <nav_msgs/Odometry.h>
#include <sensor_msgs/Imu.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>

// tf package import
#include <tf/transform_broadcaster.h>
#include <tf/tf.h> // for quaternion.
#include <tf/transform_listener.h>

#include <tf2/utils.h>
#include <tf2/LinearMath/Transform.h>
#include <tf2_ros/static_transform_broadcaster.h>
#include <tf2_ros/buffer.h>
#include <tf2_ros/transform_listener.h>


// definitions
#define PI 3.14159265
#define D2R 0.0174532925      // = 3.14159265/180
#define R2D 57.2958 // radians to degree 


class UtmTransform
{
 private:
  ros::Subscriber gps_sub_;
  ros::Subscriber imu_sub_;
  ros::Subscriber gps_sub_tf_;
  geometry_msgs::PoseWithCovarianceStamped gps_odom;
  ros::Publisher pose_pub_;
  // tf::transform cartesian_wtr_map;


public:  
  // Making the constructor having subscriber when the object is called.
  UtmTransform(ros::NodeHandle nh)
  {
    ROS_INFO_STREAM("Starting Constructor for Utm_transform");
    gps_sub_tf_ = nh.subscribe("/gps_common_navsat/odom",1,&UtmTransform::tf_callback, this);

    // imu_sub_ = nh.subscribe("/spatial/imu",10,&UtmTransform::imu_tf_callback, this);
    // pose_pub_= nh.advertise<geometry_msgs::PoseWithCovarianceStamped >("/map/robot_pose", 10);
    // gps_sub_ = nh.subscribe("/gps_common_navsat/odom", 10, &UtmTransform::printGPS, this);
    // imu_sub_ = nh.subscribe("/spatial/imu",10,&UtmTransform::printIMU, this);
    // tf2_ros::Buffer tfBuffer;
    // tf2_ros::TransformListener tfListener(tfBuffer);

  }

  ~UtmTransform(){}; // destructor.

  
  void imu_tf_callback(const sensor_msgs::Imu::ConstPtr& msg){ // msg->orientation.x 
    // Get the tf between map and spatial and use the message file.
    tf2_ros::Buffer tfBuffer;
    tf2_ros::TransformListener listener(tfBuffer);
    geometry_msgs::TransformStamped transformStamped;
    try{
        transformStamped = tfBuffer.lookupTransform("map", "spatial",
                                ros::Time(0));
        }
    catch (tf2::TransformException &ex) {
        ROS_WARN("%s",ex.what());
        ros::Duration(1.0).sleep();
        
        }
    // convert this tf message into posewithconvariance message 
      gps_odom.header.seq = transformStamped.header.seq;
      gps_odom.header.stamp = transformStamped.header.stamp;
      gps_odom.header.frame_id = transformStamped.header.frame_id;
      gps_odom.pose.pose.position.x = transformStamped.transform.translation.x;
      gps_odom.pose.pose.position.y =transformStamped.transform.translation.y;
      gps_odom.pose.pose.position.z =transformStamped.transform.translation.z;
      
    // Add the imu values to this posewithconvariance
      gps_odom.pose.pose.orientation = msg->orientation;

    // publish this value. 
      pose_pub_.publish(gps_odom);
  
  
  
  //msg->orientation
    tf::Quaternion q( msg->orientation.x,
                      msg->orientation.y,
                      msg->orientation.z,
                      msg->orientation.w); 
    tf::Matrix3x3 m(q);
    double roll, pitch,yaw ;
    m.getRPY(roll,pitch,yaw);
    ROS_INFO_STREAM("Human: "
                    << "Roll Angle :"
                    << " " << roll * R2D
                    << "Pitch Angle :"
                    << " " << pitch * R2D
                    << "Yaw Angle :"
                    << " " << yaw * R2D);   

  }

  

  void printGPS(const nav_msgs::Odometry::ConstPtr &msg){
    ROS_INFO_STREAM("Inside printGPS function");       //msg.pose.pose.position.x
    ROS_INFO_STREAM("x" << msg->pose.pose.position.x); //msg.pose.pose.position.x
  }

  void printIMU(const sensor_msgs::Imu::ConstPtr& msg){ // msg->orientation.x 
    //msg->orientation
    tf::Quaternion q( msg->orientation.x,
                      msg->orientation.y,
                      msg->orientation.z,
                      msg->orientation.w); 
    tf::Matrix3x3 m(q);
    double roll, pitch,yaw ;
    m.getRPY(roll,pitch,yaw);
    ROS_INFO_STREAM("Human: "
                    << "Roll Angle :"
                    << " " << roll * R2D
                    << "Pitch Angle :"
                    << " " << pitch * R2D
                    << "Yaw Angle :"
                    << " " << yaw * R2D);   
  }
  void tf_callback(const nav_msgs::Odometry &msg)
  {
    ROS_INFO_STREAM("Inside TF_callback");
    static tf::TransformBroadcaster br;
    tf::Transform transform;
    transform.setOrigin(tf::Vector3(msg.pose.pose.position.x - 485600, msg.pose.pose.position.y - 4234000, msg.pose.pose.position.z - 205));
    // transform.setOrigin(tf::Vector3(- 485600,  - 4234000, - 205));
    tf::Quaternion q;
    q.setRPY(0, 0, 0);
    transform.setRotation(q);
    br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "map", "spatial"));

    // msg.pose.pose.position.x
    //485600, 4234000
  }
 
};

void localPrintGPS(const nav_msgs::Odometry::ConstPtr &msg)
{
  ROS_INFO_STREAM("Inside printGPS function");       //msg.pose.pose.position.x
  ROS_INFO_STREAM("x" << msg->pose.pose.position.x); //msg.pose.pose.position.x
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "gnss_tf_broadcaster");
  ROS_INFO_STREAM("Starting node for Utm_transform"); //msg.pose.pose.positio

  // ros::NodeHandle utm;
  // ros::Subscriber sub = utm.subscribe("/gps_common_navsat/odom",1,localPrintGPS); // Working.

  ros::NodeHandle nh;
  UtmTransform trans(nh);


  ros::spin();
  return 0;
}
