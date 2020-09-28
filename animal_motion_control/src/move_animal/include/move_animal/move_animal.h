#ifndef MOVE_ANIMAL_ROS_H_
#define MOVE_ANIMAL_ROS_H_

#include <ros/ros.h>
#include <nav_msgs/OccupancyGrid.h>

//position message 
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>

//light message importing
#include <light_signal_msg/light_signal.h>

// tf package import
#include <tf2/utils.h>

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
light_signal_msg::light_signal cmd_sig{}; // contains the velocity


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
void setRot();
void setVel();








#endif