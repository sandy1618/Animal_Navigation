execute_process(COMMAND "/home/kvothe/Animal_Navigation/animal_navigation/build/gps_umd/gps_common/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/kvothe/Animal_Navigation/animal_navigation/build/gps_umd/gps_common/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
