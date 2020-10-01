#include <ros/ros.h>
#include <tf/transform_listener.h>

#include <tf2_ros/transform_listener.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include <geometry_msgs/TransformStamped.h>


int main(int argc, char** argv){
  ros::init(argc, argv, "pose_tf_to_msg");

  ros::NodeHandle node;
   geometry_msgs::PoseWithCovarianceStamped pose{};
  geometry_msgs::TransformStamped msg{};

  ros::Publisher pose_pub_= 
    node.advertise<geometry_msgs::PoseWithCovarianceStamped >("/map/robot_pose", 10);

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
    
    ros::Rate rate(10.0);
    while (node.ok()){
        geometry_msgs::TransformStamped transformStamped;
        try{
        transformStamped = tfBuffer.lookupTransform("/map", "/base_link",
                                ros::Time(0));
        }
        catch (tf2::TransformException &ex) {
        ROS_WARN("%s",ex.what());
        ros::Duration(1.0).sleep();
        continue;
        }


    msg = transformStamped;
    // tf::transformStampedTFToMsg(transform,msg);
    pose.header.seq = msg.header.seq;
    pose.header.stamp = msg.header.stamp;
    pose.header.frame_id = msg.header.frame_id;
    pose.pose.pose.position.x = msg.transform.translation.x;
    pose.pose.pose.position.y =msg.transform.translation.y;
    pose.pose.pose.position.z =msg.transform.translation.z;
    pose.pose.pose.orientation = msg.transform.rotation;

    pose_pub_.publish(pose);
    rate.sleep();
  }
  return 0;
};