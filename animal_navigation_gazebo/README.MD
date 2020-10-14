### Animal_Description 

#### Links 
https://github.com/ros-planning/navigation
https://github.com/adrianapadilla/simple_local_planner


#### Dependencies 
sudo apt-get install ros-kinetic-teleop-twist-keyboard
sudo apt-get install ros-kinetic-ros-control
sudo apt-get install ros-kinetic-hector-gazebo-plugins


sudo apt-get install -y ros-kinetic-gmapping ros-kinetic-amcl
sudo apt-get install ros-kinetic-nav-core


### UTILITIES COMMANDS 
#### Saving Map: 
rosrun map_server map_saver --occ 90 --free 10 -f mymap map:=/grid_map_pcl_loader_node/occupancy_grid

#### Opening map:
rosrun map_server map_server mymap.yaml

### Launches 

### WORKFLOW 0: Running Simulation

rosbag play --clock -l <bagfile>
export TURTLEBOT3_MODEL=burger

roslaunch turtlebot3_gazebo turtlebot3_world.launch
 
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/Animal_Navigation/animal_navigation_gazebo/src/micronrobot/turtlebot3/turtlebot3_navigation/maps/map.yaml






### WORKFLOW 1: HUMAN ORIENTAITON CLAIBRATION 
 sudo su 
 source /opt/ros/kinetic/setup.bash
 source Animal_Navigation/animal_navigation/devel/setup.bash
