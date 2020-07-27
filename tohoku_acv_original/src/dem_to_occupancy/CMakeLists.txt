cmake_minimum_required(VERSION 2.8.3)
project(dem_to_occupancy)

include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
if(COMPILER_SUPPORTS_CXX11)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")
elseif(COMPILER_SUPPORTS_CXX0X)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
else()
    message(STATUS "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()

find_package(catkin REQUIRED COMPONENTS
  roscpp
  grid_map_ros
  std_msgs
  nav_msgs
  grid_map_msgs
  message_generation
)

find_package(Boost REQUIRED)

add_service_files(
  DIRECTORY srv
  FILES Conversion.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  nav_msgs
  grid_map_msgs
)

catkin_package(
  CATKIN_DEPENDS
  roscpp
  grid_map_msgs
  grid_map_ros
)

include_directories(
  ${Boost_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
)

add_executable(dem_to_occupancy
  src/dem_to_occupancy.cpp
)
add_dependencies(dem_to_occupancy ${catkin_EXPORTED_TARGETS})

target_link_libraries(dem_to_occupancy
  ${Boost_LIBRARIES}
  ${catkin_LIBRARIES}
)
