# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "dem_to_occupancy: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Inav_msgs:/opt/ros/kinetic/share/nav_msgs/cmake/../msg;-Igrid_map_msgs:/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(dem_to_occupancy_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv" NAME_WE)
add_custom_target(_dem_to_occupancy_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "dem_to_occupancy" "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv" "std_msgs/Float32MultiArray:std_msgs/Header:std_msgs/MultiArrayLayout:geometry_msgs/Quaternion:geometry_msgs/Point:std_msgs/MultiArrayDimension:nav_msgs/MapMetaData:grid_map_msgs/GridMap:nav_msgs/OccupancyGrid:grid_map_msgs/GridMapInfo:geometry_msgs/Pose"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(dem_to_occupancy
  "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Float32MultiArray.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMap.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMapInfo.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dem_to_occupancy
)

### Generating Module File
_generate_module_cpp(dem_to_occupancy
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dem_to_occupancy
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(dem_to_occupancy_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(dem_to_occupancy_generate_messages dem_to_occupancy_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv" NAME_WE)
add_dependencies(dem_to_occupancy_generate_messages_cpp _dem_to_occupancy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dem_to_occupancy_gencpp)
add_dependencies(dem_to_occupancy_gencpp dem_to_occupancy_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dem_to_occupancy_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(dem_to_occupancy
  "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Float32MultiArray.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMap.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMapInfo.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dem_to_occupancy
)

### Generating Module File
_generate_module_eus(dem_to_occupancy
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dem_to_occupancy
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(dem_to_occupancy_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(dem_to_occupancy_generate_messages dem_to_occupancy_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv" NAME_WE)
add_dependencies(dem_to_occupancy_generate_messages_eus _dem_to_occupancy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dem_to_occupancy_geneus)
add_dependencies(dem_to_occupancy_geneus dem_to_occupancy_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dem_to_occupancy_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(dem_to_occupancy
  "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Float32MultiArray.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMap.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMapInfo.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dem_to_occupancy
)

### Generating Module File
_generate_module_lisp(dem_to_occupancy
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dem_to_occupancy
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(dem_to_occupancy_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(dem_to_occupancy_generate_messages dem_to_occupancy_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv" NAME_WE)
add_dependencies(dem_to_occupancy_generate_messages_lisp _dem_to_occupancy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dem_to_occupancy_genlisp)
add_dependencies(dem_to_occupancy_genlisp dem_to_occupancy_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dem_to_occupancy_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(dem_to_occupancy
  "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Float32MultiArray.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMap.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMapInfo.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dem_to_occupancy
)

### Generating Module File
_generate_module_nodejs(dem_to_occupancy
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dem_to_occupancy
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(dem_to_occupancy_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(dem_to_occupancy_generate_messages dem_to_occupancy_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv" NAME_WE)
add_dependencies(dem_to_occupancy_generate_messages_nodejs _dem_to_occupancy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dem_to_occupancy_gennodejs)
add_dependencies(dem_to_occupancy_gennodejs dem_to_occupancy_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dem_to_occupancy_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(dem_to_occupancy
  "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Float32MultiArray.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMap.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/grid_map_msgs/cmake/../msg/GridMapInfo.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dem_to_occupancy
)

### Generating Module File
_generate_module_py(dem_to_occupancy
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dem_to_occupancy
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(dem_to_occupancy_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(dem_to_occupancy_generate_messages dem_to_occupancy_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sandy/rosws/tohoku_acv_original/src/dem_to_occupancy/srv/Conversion.srv" NAME_WE)
add_dependencies(dem_to_occupancy_generate_messages_py _dem_to_occupancy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dem_to_occupancy_genpy)
add_dependencies(dem_to_occupancy_genpy dem_to_occupancy_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dem_to_occupancy_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dem_to_occupancy)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dem_to_occupancy
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(dem_to_occupancy_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET nav_msgs_generate_messages_cpp)
  add_dependencies(dem_to_occupancy_generate_messages_cpp nav_msgs_generate_messages_cpp)
endif()
if(TARGET grid_map_msgs_generate_messages_cpp)
  add_dependencies(dem_to_occupancy_generate_messages_cpp grid_map_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dem_to_occupancy)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dem_to_occupancy
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(dem_to_occupancy_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET nav_msgs_generate_messages_eus)
  add_dependencies(dem_to_occupancy_generate_messages_eus nav_msgs_generate_messages_eus)
endif()
if(TARGET grid_map_msgs_generate_messages_eus)
  add_dependencies(dem_to_occupancy_generate_messages_eus grid_map_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dem_to_occupancy)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dem_to_occupancy
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(dem_to_occupancy_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET nav_msgs_generate_messages_lisp)
  add_dependencies(dem_to_occupancy_generate_messages_lisp nav_msgs_generate_messages_lisp)
endif()
if(TARGET grid_map_msgs_generate_messages_lisp)
  add_dependencies(dem_to_occupancy_generate_messages_lisp grid_map_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dem_to_occupancy)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dem_to_occupancy
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(dem_to_occupancy_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET nav_msgs_generate_messages_nodejs)
  add_dependencies(dem_to_occupancy_generate_messages_nodejs nav_msgs_generate_messages_nodejs)
endif()
if(TARGET grid_map_msgs_generate_messages_nodejs)
  add_dependencies(dem_to_occupancy_generate_messages_nodejs grid_map_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dem_to_occupancy)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dem_to_occupancy\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dem_to_occupancy
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(dem_to_occupancy_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET nav_msgs_generate_messages_py)
  add_dependencies(dem_to_occupancy_generate_messages_py nav_msgs_generate_messages_py)
endif()
if(TARGET grid_map_msgs_generate_messages_py)
  add_dependencies(dem_to_occupancy_generate_messages_py grid_map_msgs_generate_messages_py)
endif()
