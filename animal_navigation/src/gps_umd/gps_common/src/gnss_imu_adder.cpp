#include <ros/ros.h>

// tf package import
#include <tf/transform_broadcaster.h>
#include <tf/tf.h> // for quaternion.
#include <tf/transform_listener.h>

#include <tf2_ros/transform_listener.h>

#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include <geometry_msgs/TransformStamped.h>

#include <sensor_msgs/Imu.h> // for IMU type 
#include <nav_msgs/Odometry.h>  // for gnss msg. 

// definitions
#define PI 3.14159265
#define D2R 0.0174532925      // = 3.14159265/180
#define R2D 57.2958 // radians to degree 

//Global Variables.
ros::Subscriber imu_sub_;
ros::Subscriber gnss_sub_;
ros::Publisher pose_pub_;

sensor_msgs::Imu imu_msg;
nav_msgs::Odometry gnss_msg;
geometry_msgs::PoseWithCovarianceStamped gps_odom;



void pose_imu_publisher(const sensor_msgs::Imu::ConstPtr& msg){ // msg->orientation.x 
    // Get the tf between map and spatial and use the message file.
    ROS_INFO_STREAM("Inside TF_callback");
    imu_msg = *msg; // adding imu_message inside global variable. 
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

void gnss_to_mapframe(const nav_msgs::Odometry::ConstPtr& msg){
  // conves
  gnss_msg.header = msg->header;
  gnss_msg.header.frame_id = "map";
  gnss_msg.child_frame_id = msg->child_frame_id;
  gnss_msg.pose.pose.position.x = msg->pose.pose.position.x - 485600;
  gnss_msg.pose.pose.position.y = msg->pose.pose.position.y - 4234000;
  gnss_msg.pose.pose.position.z = msg->pose.pose.position.z - 204;
  gnss_msg.twist = msg->twist;



 
}
int main(int argc, char** argv){
  ros::init(argc, argv, "pose_tf_to_msg");

  ros::NodeHandle node;
//   tf::TransformListener listener;
//   ros::Rate rate(10.0);
//   while (node.ok()){
//     tf::StampedTransform transform;
//     try{
//       listener.lookupTransform( "base_link",  "map",
//                                ros::Time(0), transform);
//     }
//     catch (tf::TransformException ex){
//       ROS_ERROR("%s",ex.what());
//       ros::Duration(1.0).sleep();
//     }
    tf2_ros::Buffer tfBuffer;
    tf2_ros::TransformListener listener(tfBuffer);
    geometry_msgs::TransformStamped transformStamped;
    pose_pub_= node.advertise<geometry_msgs::PoseWithCovarianceStamped >("/map/robot_pose", 2);
      
    gnss_sub_ = node.subscribe("/gps_common_navsat/odom",2,gnss_to_mapframe);
    // imu_sub_ = node.subscribe("/imu/data",2,pose_imu_publisher);
    imu_sub_ = node.subscribe("/spatial/imu",2,pose_imu_publisher);
   
   ros::Rate loop_rate(200);

    while (node.ok()){
      //setup publisher.
     

     // spinOnce for subscriber to take action 
      ros::spinOnce();
    // convert this tf message into posewithconvariance message 
      
      // gps_odom.pose.pose.position.y =transformStamped.transform.translation.y;
      // gps_odom.pose.pose.position.z =transformStamped.transform.translation.z;
    gps_odom.header = gnss_msg.header;
    gps_odom.pose = gnss_msg.pose;
   // Add the imu values to this posewithconvariance
    gps_odom.pose.pose.orientation = imu_msg.orientation;
   // publish this value. 
    pose_pub_.publish(gps_odom);
      
	loop_rate.sleep();
   


    

   

    }
  return 0;
};
