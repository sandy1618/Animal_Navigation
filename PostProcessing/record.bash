#!/bin/bash
cd ~/Animal_Navigation/PostProcessing/data/
# rosbag record -a
rosbag record /cmd_sig \
/gps_common_navsat/odom \
/map/robot_pose \
/path \
/spatial/imu \
/waypoints \
/tf \
/tf_static \
/state \
/move_base/cancel \
/move_base/feedback \
/move_base/goal \
/move_base/result \
/move_base/status \