cmake_minimum_required(VERSION 2.8.3)
project(animal_description)

## Add support for C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)

# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED COMPONENTS
  roscpp
  gazebo_ros
  #controller_manager
  joint_state_publisher
  robot_state_publisher
  rospy
  rviz
  std_msgs
)

# Depend on system install of Gazebo
find_package(gazebo REQUIRED)

link_directories(${GAZEBO_LIBRARY_DIRS})
include_directories(${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS})
list(APPEND CMAKE_CXX_FLAGS "${GAZEBO_CXX_FLAGS}")

# Custom motion_model
add_library(motion_model SHARED motion_model.cc)
target_link_libraries(motion_model ${GAZEBO_LIBRARIES})

# For plannar_mover plugin
add_library(plannar_mover_plugin SHARED plannar_mover.cpp)
target_link_libraries(plannar_mover_plugin ${catkin_LIBRARIES} ${GAZEBO_LIBRARIES})


catkin_package(
  DEPENDS
    roscpp
    gazebo_ros
    #controller_manager
    joint_state_publisher
    robot_state_publisher
    rospy
    rviz
    std_msgs
)




