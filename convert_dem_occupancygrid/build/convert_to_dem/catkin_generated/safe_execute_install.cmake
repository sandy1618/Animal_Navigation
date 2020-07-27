execute_process(COMMAND "/home/sandy/Animal_Navigation/convert_dem_occupancygrid/build/convert_to_dem/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/sandy/Animal_Navigation/convert_dem_occupancygrid/build/convert_to_dem/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
