/*
 * grid_map_pcl_loader_node.cpp
 *
 *  Created on: Aug 26, 2019
 *      Author: Edo Jelavic
 *      Institute: ETH Zurich, Robotic Systems Lab
 */

#include <ros/ros.h>

#include "grid_map_core/GridMap.hpp"
#include "grid_map_ros/GridMapRosConverter.hpp"
#include "grid_map_pcl/GridMapPclLoader.hpp"
#include "grid_map_pcl/helpers.hpp"
#include <nav_msgs/OccupancyGrid.h>

namespace gm = ::grid_map::grid_map_pcl;

int main(int argc, char** argv) {
  ros::init(argc, argv, "grid_map_pcl_loader_node");
  ros::NodeHandle nh("~");    
  gm::setVerbosityLevelToDebugIfFlagSet(nh);

  ros::Publisher gridMapPub;
  gridMapPub = nh.advertise<grid_map_msgs::GridMap>("grid_map_from_raw_pointcloud", 1, true);

  ros::Publisher occupancyMapPub;  
  occupancyMapPub = nh.advertise<nav_msgs::OccupancyGrid>("occupancy_grid",1,true);

  grid_map::GridMapPclLoader gridMapPclLoader;
  const std::string pathToCloud = gm::getPcdFilePath(nh);
  gridMapPclLoader.loadParameters(gm::getParameterPath());
  gridMapPclLoader.loadCloudFromPcdFile(pathToCloud);

  // Processing point clouds
  gm::processPointcloud(&gridMapPclLoader, nh);

  // Getting the grid map.
  grid_map::GridMap gridMap = gridMapPclLoader.getGridMap();
  gridMap.setFrameId(gm::getMapFrame(nh));

  gm::saveGridMap(gridMap, nh, gm::getMapRosbagTopic(nh));

  //publish grid map

  grid_map_msgs::GridMap msg;
  grid_map::GridMapRosConverter::toMessage(gridMap, msg);
  gridMapPub.publish(msg);

  //Convert to occupancygrid message 
  nav_msgs::OccupancyGrid occupancymsg;
  // elevation is default layer name.
  grid_map::GridMapRosConverter::toOccupancyGrid(gridMap,"elevation",-0.6858147,5.7494574,occupancymsg) ;
  occupancyMapPub.publish(occupancymsg);

  // run
  ros::spin();
  return EXIT_SUCCESS;
}
