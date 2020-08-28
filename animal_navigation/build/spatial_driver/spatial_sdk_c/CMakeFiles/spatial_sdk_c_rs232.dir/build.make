# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kvothe/Animal_Navigation/animal_navigation/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kvothe/Animal_Navigation/animal_navigation/build

# Include any dependencies generated for this target.
include spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/depend.make

# Include the progress variables for this target.
include spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/progress.make

# Include the compile flags for this target's objects.
include spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/flags.make

spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o: spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/flags.make
spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o: /home/kvothe/Animal_Navigation/animal_navigation/src/spatial_driver/spatial_sdk_c/src/rs232/rs232.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kvothe/Animal_Navigation/animal_navigation/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o"
	cd /home/kvothe/Animal_Navigation/animal_navigation/build/spatial_driver/spatial_sdk_c && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o   -c /home/kvothe/Animal_Navigation/animal_navigation/src/spatial_driver/spatial_sdk_c/src/rs232/rs232.c

spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.i"
	cd /home/kvothe/Animal_Navigation/animal_navigation/build/spatial_driver/spatial_sdk_c && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/kvothe/Animal_Navigation/animal_navigation/src/spatial_driver/spatial_sdk_c/src/rs232/rs232.c > CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.i

spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.s"
	cd /home/kvothe/Animal_Navigation/animal_navigation/build/spatial_driver/spatial_sdk_c && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/kvothe/Animal_Navigation/animal_navigation/src/spatial_driver/spatial_sdk_c/src/rs232/rs232.c -o CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.s

spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o.requires:

.PHONY : spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o.requires

spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o.provides: spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o.requires
	$(MAKE) -f spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/build.make spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o.provides.build
.PHONY : spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o.provides

spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o.provides.build: spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o


# Object files for target spatial_sdk_c_rs232
spatial_sdk_c_rs232_OBJECTS = \
"CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o"

# External object files for target spatial_sdk_c_rs232
spatial_sdk_c_rs232_EXTERNAL_OBJECTS =

/home/kvothe/Animal_Navigation/animal_navigation/devel/lib/libspatial_sdk_c_rs232.so: spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o
/home/kvothe/Animal_Navigation/animal_navigation/devel/lib/libspatial_sdk_c_rs232.so: spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/build.make
/home/kvothe/Animal_Navigation/animal_navigation/devel/lib/libspatial_sdk_c_rs232.so: spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kvothe/Animal_Navigation/animal_navigation/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared library /home/kvothe/Animal_Navigation/animal_navigation/devel/lib/libspatial_sdk_c_rs232.so"
	cd /home/kvothe/Animal_Navigation/animal_navigation/build/spatial_driver/spatial_sdk_c && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/spatial_sdk_c_rs232.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/build: /home/kvothe/Animal_Navigation/animal_navigation/devel/lib/libspatial_sdk_c_rs232.so

.PHONY : spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/build

spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/requires: spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/src/rs232/rs232.c.o.requires

.PHONY : spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/requires

spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/clean:
	cd /home/kvothe/Animal_Navigation/animal_navigation/build/spatial_driver/spatial_sdk_c && $(CMAKE_COMMAND) -P CMakeFiles/spatial_sdk_c_rs232.dir/cmake_clean.cmake
.PHONY : spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/clean

spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/depend:
	cd /home/kvothe/Animal_Navigation/animal_navigation/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kvothe/Animal_Navigation/animal_navigation/src /home/kvothe/Animal_Navigation/animal_navigation/src/spatial_driver/spatial_sdk_c /home/kvothe/Animal_Navigation/animal_navigation/build /home/kvothe/Animal_Navigation/animal_navigation/build/spatial_driver/spatial_sdk_c /home/kvothe/Animal_Navigation/animal_navigation/build/spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : spatial_driver/spatial_sdk_c/CMakeFiles/spatial_sdk_c_rs232.dir/depend

