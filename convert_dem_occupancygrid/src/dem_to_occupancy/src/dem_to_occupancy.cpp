#include <ros/ros.h>
#include <grid_map_core/GridMap.hpp>
#include <grid_map_ros/GridMapRosConverter.hpp>
#include <nav_msgs/OccupancyGrid.h>
#include <dem_to_occupancy/Conversion.h>

bool
to_occupancy_grid(dem_to_occupancy::Conversion::Request& req,
                  dem_to_occupancy::Conversion::Response& res) {
    grid_map::GridMap grid_map;
    grid_map::GridMapRosConverter::fromMessage(req.grid_map, grid_map);
    grid_map::GridMapRosConverter::toOccupancyGrid(grid_map,
                                                   "traversability",
                                                   0,
                                                   1,
                                                   res.grid);
    // Convert to threshold for the OccupancyGrid [0, 100]
    auto threshold = 100 * static_cast<double>(req.threshold);
    auto retain_unknown = static_cast<bool>(req.retain_unknown);

    // Do not apply threshold
    if (threshold < 0) {
        return true;
    }

    // White is 0, black is 100, unknown is -1
    for (auto& g : res.grid.data) {
        if (g == -1) {
            if (!retain_unknown) {
                g = 0;
            }
        }
        else {
            // White to black, vice versa
            g = g * -1 + 100;
            g = g > threshold ? 100 : 0;
        }
    }

    return true;
}

int
main(int argc, char* argv[]) {
    ros::init(argc, argv, "dem_to_occupancy");

    ros::NodeHandle nh;
    auto service = nh.advertiseService("dem_to_occupancy", to_occupancy_grid);

    ros::spin();

    return 0;
}
