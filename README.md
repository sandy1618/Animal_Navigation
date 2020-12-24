# Animal_Navigation
git clone https://github.com/sandy1618/Animal_Navigation.git

## Dependencies : 
### Kinectic 
Run catkin_make on the light_signal/ folder so that light_msg depedencies are installed.
sudo apt-get install ros-kinetic-navigation
sudo apt-get install ros-kinetic-joy ros-kinetic-joystick-drivers
sudo apt-get install libgps-dev
sudo apt-get install ros-kinetic-tf2-sensor-msgs

### Melodic 
Run catkin_make on the light_signal/ folder so that light_msg depedencies are installed.
sudo apt-get install ros-melodic-navigation
sudo apt-get install ros-melodic-joy ros-melodic-joystick-drivers
sudo apt-get install libgps-dev
sudo apt-get install ros-melodic-tf2-sensor-msgs
sudo apt-get install ros-melodic-map-server

# for audio
sudo apt install alsa-utils



## Main Packages at Work
-gridmap2/ gridmap_pcl
To make the occupancy grid map. But not used after saving it in map_server. 
-animal_motion_control/ move_animal
-light_signal_msg
-animal_navigation 

## Order Of packgage installation & sourcing  for better overlay of workspaces. 
It means, build the package, & add the execute source into bash file.
catkin_make
source /home/alien/Animal_Navigation/light_signal/devel/setup.bash
catkin_make
source /home/alien/Animal_Navigation/animal_navigation/devel/setup.bash
catkin_make
source /home/alien/Animal_Navigation/animal_motion_control/devel/setup.bash
catkin_make
source /home/alien/Animal_Navigation/animal_navigation_gazebo/devel/setup.bash





### Utilities 
#### Saving Maps 
rosrun map_server map_saver -f mymap2 map:=/grid_map_pcl_loader_node/occupancy_grid
rosrun map_server map_sever mymap2

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

## Rosbag Recorded Topics 
/cmd_sig
/map
/map/robot_pose
/map_metadata
/move_base_simple/goal

/gps_comon_navsat/odom
/spatial/fix
/spatial/imu


## Workflow 1:
### For Running Turtle bot simulation 
#### Run Gazebo 
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_world.launch 

#### Run Navigation + Rviz 
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/Animal_Navigation/animal_navigation_gazebo/src/micronrobot/turtlebot3/turtlebot3_navigation/maps/map.yaml


#### Run Command signal & comman velocity node. 
<!-- - Check if the node is subscribing to AMCL signal .  -->
roslaunch move_animal move_animal_vel.launch

#### follow waypoints
roslaunch move_animal move_animal_waypoint.launch 

rostopic pub /path_ready std_msgs/Empty -1



___ 
## Workflow 2:
### Wearable Human Suit Up PC:
#### Starting spatial node.
sudo su
roslaunch spatial_driver output_anpp_complete.launch


### Starting led controlerl 
roslaunch move_animal move_animal_led_sig.launch
#### Audio
roslaunch move_animal move_animal_audio_sig.launch
#### LED+AUDIO signal
roslaunch move_animal move_animal_led_audio_sig.launch
### LED+WARN Audio signal
roslaunch move_animal move_animal_led_warn_audio_sig.launch




### Laptop PC 
#### Starting the GNSS + IMU launch file
roslaunch gps_common final_animal_pose.launch

#### Starting the move_animal_waypoint controller. 
<!-- Check if the node is subscribing to /map/robot_pose signal -->
roslaunch move_animal move_animal_waypoint.launch

#### Starting the move_animal_waypoint controller sig controller.
roslaunch move_animal move_animal_sig.launch

# LATEST BOTH FILES AT ONCE. 
roslaunch move_animal move_animal_waypoint_sig.launch

### RUN mapserver and Rviz in other PC
rosrun map_server map_server map/mymap2.yaml

### Rviz 
roslaunch move_animal rviz_display.launch

#### Run Rosbag node. 
roslaunch move_animal rosbag_record.launch

### Bash Alias 

alias start='rostopic pub /path_ready std_msgs/Empty -1 && rostopic pub -l --once /state light_signal_msg/state '{header: auto,state: 1}''
alias stop='rostopic pub /path_reset std_msgs/Empty -1 && rostopic pub -l --once /state light_signal_msg/state '{header: auto,state: 2}''
alias start_file='rostopic pub /start_journey std_msgs/Empty -1'




## Utilities.

scp dog@192.168.1.2:/home/dog/Animal_Navigation/data/tamura/* /home/sandy/Animal_Navigation/PostProcessing/data/tamura/

rosparam set /use_sim_time true
# rosbag record excluding path
rosbag record -a -x "/path"

rosbag play -l --clock <bag_name> --topics /cmd_sig

