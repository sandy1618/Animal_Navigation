# Animal_Navigation
## Main Packages at Work
-gridmap2/ gridmap_pcl
-animal_motion_control/ move_animal
-light_signal_msg
-animal_navigation 




### Workflow 

cd ~/Animal_Navigation/data/
rosbag play -l --clock .bag

cd ~/Animal_Navigation/gridmap2
roslaunch grid_map_pcl grid_map_pcl_loader_node.launch
roslaunch grid_map_pcl grid_map_pcl_loader_node_support.launch

// Remeber that, for a proper Occupancy grid map, you need to set mininmum and maximum value based on heght. in 
// grid_map_pcl_loader_node.cpp. 
// The python file is Height_Min_Max.ipynb (open with jupyter notebooks), in Animal_Naviation/data/
// Make sure you make the file accessible and executeble 

// This contains both the spatial -> utm and map->spatial tranformation tf
cd ~/Animal_Navigation/animal_navigation
roslaunch gps_common utm_converter_tf_publisher.launch
- input: /spatial/fix  < /sensor_msgs/NavSatFix >
- output: /gps_common_navsat/odom < /nav_msgs/Odometry >


cd ~/Animal_Navigation/hector_slam
roslaunch hector_imu_attitude_to_tf example.launch



Note: utm_transfom.cpp inside gps_common has the map to spatial transformnation. 


Workflow 1:
### Starting spatial node.
sudo su
roslaunch spatial_driver output_anpp_complete.launch

### Starting the GNSS + IMU launch file
roslaunch gps_common utm_converter_tf_publisher.launch

### RUN mapserver and Rviz 
rosrun map_server map_server map/mymap.yaml

### Starting the move_animal_sig.launch controller. 
roslaunch move_animal move_animal_sig.launch

### Starting the LED control in root. 
sudo su
rosrun move_animal led_control_cmd_sig.py 

### Run Rosbag node. 

