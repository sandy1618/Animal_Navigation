# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/kinetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/kinetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in "/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/navigation;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/simple_local_planner;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/move_base;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/rotate_recovery;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/global_planner;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/navfn;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/move_slow_and_clear;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/dwa_local_planner;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/clear_costmap_recovery;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/carrot_planner;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/base_local_planner;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/nav_core;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/costmap_2d;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/voxel_grid;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/amcl;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/map_server;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/fake_localization;/home/sandy/Animal_Navigation/animal_navigation/devel;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot_teleop;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_teleop;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_slam;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_simulations;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_navigation;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_fake;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_example;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_bringup;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_msgs;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_gazebo;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3_description;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/turtlebot3;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/teleop_tools_msgs;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/teleop_tools;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/mouse_teleop;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/key_teleop;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/joy_teleop;/home/sandy/Animal_Navigation/light_signal/devel;/home/sandy/Animal_Navigation/animal_navigation_gazebo/devel_isolated/animal_description;/opt/ros/kinetic".split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/sandy/Animal_Navigation/animal_navigation/devel/env.sh')

output_filename = '/home/sandy/Animal_Navigation/animal_navigation/build/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    #print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
