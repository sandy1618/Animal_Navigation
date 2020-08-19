# Install script for directory: /home/kvothe/Animal_Navigation/convert_dem_occupancygrid/src/dem_to_occupancy

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dem_to_occupancy/srv" TYPE FILE FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/src/dem_to_occupancy/srv/Conversion.srv")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dem_to_occupancy/cmake" TYPE FILE FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/build/dem_to_occupancy/catkin_generated/installspace/dem_to_occupancy-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/devel/include/dem_to_occupancy")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/devel/share/roseus/ros/dem_to_occupancy")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/devel/share/common-lisp/ros/dem_to_occupancy")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/devel/share/gennodejs/ros/dem_to_occupancy")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/devel/lib/python2.7/dist-packages/dem_to_occupancy")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/devel/lib/python2.7/dist-packages/dem_to_occupancy")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/build/dem_to_occupancy/catkin_generated/installspace/dem_to_occupancy.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dem_to_occupancy/cmake" TYPE FILE FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/build/dem_to_occupancy/catkin_generated/installspace/dem_to_occupancy-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dem_to_occupancy/cmake" TYPE FILE FILES
    "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/build/dem_to_occupancy/catkin_generated/installspace/dem_to_occupancyConfig.cmake"
    "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/build/dem_to_occupancy/catkin_generated/installspace/dem_to_occupancyConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dem_to_occupancy" TYPE FILE FILES "/home/kvothe/Animal_Navigation/convert_dem_occupancygrid/src/dem_to_occupancy/package.xml")
endif()

