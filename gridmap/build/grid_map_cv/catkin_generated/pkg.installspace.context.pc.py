# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/opt/ros/kinetic/include/opencv-3.3.1-dev;/opt/ros/kinetic/include/opencv-3.3.1-dev/opencv".split(';') if "${prefix}/include;/opt/ros/kinetic/include/opencv-3.3.1-dev;/opt/ros/kinetic/include/opencv-3.3.1-dev/opencv" != "" else []
PROJECT_CATKIN_DEPENDS = "grid_map_core;cv_bridge;filters".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lgrid_map_cv;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_photo3.so.3.3.1".split(';') if "-lgrid_map_cv;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_photo3.so.3.3.1" != "" else []
PROJECT_NAME = "grid_map_cv"
PROJECT_SPACE_DIR = "/home/kvothe/Animal_Navigation/gridmap/install"
PROJECT_VERSION = "1.6.2"
