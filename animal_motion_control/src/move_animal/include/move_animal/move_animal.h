#ifndef MOVE_ANIMAL_ROS_H_
#define MOVE_ANIMAL_ROS_H_

//Move base action 
#include <actionlib/server/simple_action_server.h>
#include <move_base_msgs/MoveBaseAction.h>
//typedefs to help us out with the action server so that we don't hace to type so much
typedef actionlib::SimpleActionServer<move_base_msgs::MoveBaseAction> MoveBaseActionServer;

// SimpleActionServer (ros::NodeHandle n, std::string name, ExecuteCallback execute_callback, bool auto_start)

#include <ros/ros.h>
#include <nav_msgs/OccupancyGrid.h>

//position message 
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include <std_msgs/Header.h>

//light message importing
#include <light_signal_msg/light_signal.h>
#include <light_signal_msg/state.h>

// tf package import
#include <tf2/utils.h>
#include <tf/tf.h> // for quaternions.

// // for visualization 
// #include <nav_msgs/Path.h>


// definitions
#define PI 3.14159265
#define D2R 0.0174532925      // = 3.14159265/180
#define R2D 57.2958 // radians to degree 
struct pos {
    double x, y, az; // az is yaw angle.
};




/* data */  
 pos now{}; // present frame
 pos next{}; // next frame
 pos nError{}; // error between present and next goal frame 
 pos goal{}; // goal postion 
double distance{}; // Euclidean distance 
double ref_angle{}; // reference angle
double roll{}, pitch{},yaw{} ; // roll pitch and yaw angles made global.
light_signal_msg::light_signal cmd_sig{}; // contains the velocity
std_msgs::Header msg_header;

// nav_msgs::Path path;
geometry_msgs::PoseStamped path_pose;

ros::Publisher pub_sig_;
// ros::Publisher pub_path_;

/**
 * @brief Get robot postioin via amcl callback
 */ 
void getRobotPoseAMCL(const geometry_msgs::PoseWithCovarianceStamped& msg);

void getHumanPoseGNSS(const geometry_msgs::PoseWithCovarianceStamped& msg);

void getDogPoseGNSS(const geometry_msgs::PoseWithCovarianceStamped& msg);

void getGoalPos(const geometry_msgs::PoseStamped& msg);

/**
 * @brief setNowError: calculates the error between the next and present frame
 */
void setNowError();

void computeSignalCommands();
void setZeroSignal();
void setOneSignal();
void setRot();
void setVel();

void getGoalActionPose(const move_base_msgs::MoveBaseGoalConstPtr& move_base_goal, MoveBaseActionServer* as_);







#endif