# Animal_Navigation

### Workflow 

cd ~/Animal_Navigation/
rosbag play -l --clock .bag

cd ~/Animal_Navigation/gridmap2
roslaunch grid_map_pcl grid_map_pcl_loader_node.launch
roslaunch grid_map_pcl grid_map_pcl_loader_node_support.launch

// This contains both the spatial -> utm and map->spatial tranformation tf
cd ~/Animal_Navigation/animal_navigation
roslaunch gps_common utm_converter_tf_publisher.launch

cd ~/Animal_Navigation/hector_slam
roslaunch hector_imu_attitude_to_tf example.launch



