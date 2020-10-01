
#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>

void tf_callback(const nav_msgs::Odometry& msg){
  static tf::TransformBroadcaster br;
  tf::Transform transform;
  transform.setOrigin(tf::Vector3(msg.pose.pose.position.x-485600,msg.pose.pose.position.y-4234000,msg.pose.pose.position.z-200));
  tf::Quaternion q;
  q.setRPY(0,0,0);
  transform.setRotation(q);
  br.sendTransform(tf::StampedTransform(transform,ros::Time::now(),"map","spatial"));

// msg.pose.pose.position.x

//485600, 4234000


}

int main(int argc, char** argv){
  ros::init(argc, argv, "gnss_tf_broadcaster");
  ros::NodeHandle node;
  ros::Subscriber sub = node.subscribe("/gps_common_navsat/odom",1,tf_callback);


  ros::spin();
  return 0;



}
