# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "grid_map_core;grid_map_msgs;grid_map_ros;pcl_ros;roscpp".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lgrid_map_pcl;-lyaml-cpp".split(';') if "-lgrid_map_pcl;-lyaml-cpp" != "" else []
PROJECT_NAME = "grid_map_pcl"
PROJECT_SPACE_DIR = "/home/kvothe/Animal_Navigation/gridmap/install"
PROJECT_VERSION = "1.6.2"
