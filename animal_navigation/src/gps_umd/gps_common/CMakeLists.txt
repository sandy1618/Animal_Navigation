cmake_minimum_required(VERSION 2.8.3)
project(gps_common CXX)

add_compile_options(-std=c++14)

############
## Catkin ##
############

set(DEPS
  message_filters
  nav_msgs
  roscpp
  sensor_msgs
  std_msgs
  rospy
  tf
  tf2
  tf2_ros
  
)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  ${DEPS}
)

catkin_python_setup()

#######################################
## Declare ROS messages and services ##
#######################################

add_message_files(
  FILES
    GPSStatus.msg
    GPSFix.msg
)

generate_messages(DEPENDENCIES 
  nav_msgs
  sensor_msgs
  std_msgs
)

###################################################
## Declare things to be passed to other projects ##
###################################################

catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS 
    message_runtime
    tf
    ${DEPS}
)

###########
## Build ##
###########

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include ${catkin_INCLUDE_DIRS})

add_executable(${PROJECT_NAME}/utm_odometry_node src/utm_odometry_node.cpp)
add_executable(${PROJECT_NAME}/utm_odometry_to_navsatfix_node src/utm_odometry_to_navsatfix_node.cpp)
add_executable(utm_transform src/utm_transform.cpp)
add_executable(pose_tf_to_msg src/pose_tf_to_msg.cpp)
add_executable(gnss_imu_adder src/gnss_imu_adder.cpp)



set_target_properties(${PROJECT_NAME}/utm_odometry_node PROPERTIES OUTPUT_NAME "utm_odometry_node")
target_link_libraries(${PROJECT_NAME}/utm_odometry_node ${catkin_LIBRARIES})

set_target_properties(${PROJECT_NAME}/utm_odometry_to_navsatfix_node PROPERTIES OUTPUT_NAME "utm_odometry_to_navsatfix_node")
target_link_libraries(${PROJECT_NAME}/utm_odometry_to_navsatfix_node ${catkin_LIBRARIES})

set_target_properties(utm_transform PROPERTIES OUTPUT_NAME "utm_transform")
target_link_libraries(utm_transform ${catkin_LIBRARIES})

set_target_properties(pose_tf_to_msg PROPERTIES OUTPUT_NAME "pose_tf_to_msg")
target_link_libraries(pose_tf_to_msg ${catkin_LIBRARIES})

set_target_properties(gnss_imu_adder PROPERTIES OUTPUT_NAME "gnss_imu_adder")
target_link_libraries(gnss_imu_adder ${catkin_LIBRARIES})


add_dependencies(${PROJECT_NAME}/utm_odometry_node
  ${PROJECT_NAME}_generate_messages_cpp 
  ${catkin_EXPORTED_TARGETS} 
  ${${PROJECT_NAME}_EXPORTED_TARGETS}
)

add_dependencies(${PROJECT_NAME}/utm_odometry_to_navsatfix_node
  ${PROJECT_NAME}_generate_messages_cpp 
  ${catkin_EXPORTED_TARGETS} 
  ${${PROJECT_NAME}_EXPORTED_TARGETS}
)
add_dependencies(utm_transform
  ${PROJECT_NAME}_generate_messages_cpp 
  ${catkin_EXPORTED_TARGETS} 
  ${${PROJECT_NAME}_EXPORTED_TARGETS}
)
add_dependencies(pose_tf_to_msg
  ${PROJECT_NAME}_generate_messages_cpp 
  ${catkin_EXPORTED_TARGETS} 
  ${${PROJECT_NAME}_EXPORTED_TARGETS}
)
add_dependencies(gnss_imu_adder
  ${PROJECT_NAME}_generate_messages_cpp 
  ${catkin_EXPORTED_TARGETS} 
  ${${PROJECT_NAME}_EXPORTED_TARGETS}
)




#############
## Install ##
#############

install(TARGETS
  ${PROJECT_NAME}/utm_odometry_node
  ${PROJECT_NAME}/utm_odometry_to_navsatfix_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY include/${PROJECT_NAME}/ 
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)

catkin_install_python(PROGRAMS nodes/fix_translator scripts/bag_converter
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
