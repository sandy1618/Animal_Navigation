cmake_minimum_required(VERSION 2.8.3)
project(spatial_driver)

set(CMAKE_CXX_FLAGS "-std=c++11 -Wall -Wextra -Wpedantic")
set(CMAKE_CXX_FLAGS_DEBUG "-O0 -g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

find_package(catkin REQUIRED COMPONENTS
  tf2
  tf2_ros
  geometry_msgs
  std_msgs
  roscpp
  sensor_msgs
  spatial_sdk_c
  diagnostic_updater
)

catkin_package(
  CATKIN_DEPENDS tf2 tf2_ros geometry_msgs std_msgs roscpp sensor_msgs spatial_sdk_c diagnostic_updater
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_library(spatial
  src/spatial.cpp include/spatial_driver/spatial.h
)

add_executable(spatial_node src/spatial_node.cpp)
target_link_libraries(spatial_node
  spatial
  ${catkin_LIBRARIES}
)

install(TARGETS spatial_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY include/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
)
