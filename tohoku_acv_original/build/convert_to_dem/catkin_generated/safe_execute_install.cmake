execute_process(COMMAND "/home/sandy/rosws/tohoku_acv_original/build/convert_to_dem/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/sandy/rosws/tohoku_acv_original/build/convert_to_dem/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
