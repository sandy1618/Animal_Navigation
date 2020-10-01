/************************************************
 * Spatial Driver for ROS.
 *
 * This manuscript is based on Orientus driver
 * developed by Nick Otero and Mitchell Wills,
 * and maintained by Mitchell Wills.
 * See https://wiki.ros.org/orientus_driver
 ************************************************/
#include "spatial_driver/spatial.h"

int main(int argc, char* argv[]) {
    ros::init(argc, argv, "spatial_node");

    Spatial node;
    node.spin();

    return 0;
}
