# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

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
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.17.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.17.1/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/dingwang/flask_react/backend/xgboost

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/dingwang/flask_react/backend/xgboost/my_build

# Include any dependencies generated for this target.
include rabit/CMakeFiles/rabit_base.dir/depend.make

# Include the progress variables for this target.
include rabit/CMakeFiles/rabit_base.dir/progress.make

# Include the compile flags for this target's objects.
include rabit/CMakeFiles/rabit_base.dir/flags.make

rabit/CMakeFiles/rabit_base.dir/src/allreduce_base.cc.o: rabit/CMakeFiles/rabit_base.dir/flags.make
rabit/CMakeFiles/rabit_base.dir/src/allreduce_base.cc.o: ../rabit/src/allreduce_base.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/dingwang/flask_react/backend/xgboost/my_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object rabit/CMakeFiles/rabit_base.dir/src/allreduce_base.cc.o"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rabit_base.dir/src/allreduce_base.cc.o -c /Users/dingwang/flask_react/backend/xgboost/rabit/src/allreduce_base.cc

rabit/CMakeFiles/rabit_base.dir/src/allreduce_base.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rabit_base.dir/src/allreduce_base.cc.i"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/dingwang/flask_react/backend/xgboost/rabit/src/allreduce_base.cc > CMakeFiles/rabit_base.dir/src/allreduce_base.cc.i

rabit/CMakeFiles/rabit_base.dir/src/allreduce_base.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rabit_base.dir/src/allreduce_base.cc.s"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/dingwang/flask_react/backend/xgboost/rabit/src/allreduce_base.cc -o CMakeFiles/rabit_base.dir/src/allreduce_base.cc.s

rabit/CMakeFiles/rabit_base.dir/src/engine_base.cc.o: rabit/CMakeFiles/rabit_base.dir/flags.make
rabit/CMakeFiles/rabit_base.dir/src/engine_base.cc.o: ../rabit/src/engine_base.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/dingwang/flask_react/backend/xgboost/my_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object rabit/CMakeFiles/rabit_base.dir/src/engine_base.cc.o"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rabit_base.dir/src/engine_base.cc.o -c /Users/dingwang/flask_react/backend/xgboost/rabit/src/engine_base.cc

rabit/CMakeFiles/rabit_base.dir/src/engine_base.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rabit_base.dir/src/engine_base.cc.i"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/dingwang/flask_react/backend/xgboost/rabit/src/engine_base.cc > CMakeFiles/rabit_base.dir/src/engine_base.cc.i

rabit/CMakeFiles/rabit_base.dir/src/engine_base.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rabit_base.dir/src/engine_base.cc.s"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/dingwang/flask_react/backend/xgboost/rabit/src/engine_base.cc -o CMakeFiles/rabit_base.dir/src/engine_base.cc.s

rabit/CMakeFiles/rabit_base.dir/src/c_api.cc.o: rabit/CMakeFiles/rabit_base.dir/flags.make
rabit/CMakeFiles/rabit_base.dir/src/c_api.cc.o: ../rabit/src/c_api.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/dingwang/flask_react/backend/xgboost/my_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object rabit/CMakeFiles/rabit_base.dir/src/c_api.cc.o"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rabit_base.dir/src/c_api.cc.o -c /Users/dingwang/flask_react/backend/xgboost/rabit/src/c_api.cc

rabit/CMakeFiles/rabit_base.dir/src/c_api.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rabit_base.dir/src/c_api.cc.i"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/dingwang/flask_react/backend/xgboost/rabit/src/c_api.cc > CMakeFiles/rabit_base.dir/src/c_api.cc.i

rabit/CMakeFiles/rabit_base.dir/src/c_api.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rabit_base.dir/src/c_api.cc.s"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/dingwang/flask_react/backend/xgboost/rabit/src/c_api.cc -o CMakeFiles/rabit_base.dir/src/c_api.cc.s

# Object files for target rabit_base
rabit_base_OBJECTS = \
"CMakeFiles/rabit_base.dir/src/allreduce_base.cc.o" \
"CMakeFiles/rabit_base.dir/src/engine_base.cc.o" \
"CMakeFiles/rabit_base.dir/src/c_api.cc.o"

# External object files for target rabit_base
rabit_base_EXTERNAL_OBJECTS =

rabit/librabit_base.a: rabit/CMakeFiles/rabit_base.dir/src/allreduce_base.cc.o
rabit/librabit_base.a: rabit/CMakeFiles/rabit_base.dir/src/engine_base.cc.o
rabit/librabit_base.a: rabit/CMakeFiles/rabit_base.dir/src/c_api.cc.o
rabit/librabit_base.a: rabit/CMakeFiles/rabit_base.dir/build.make
rabit/librabit_base.a: rabit/CMakeFiles/rabit_base.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/dingwang/flask_react/backend/xgboost/my_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX static library librabit_base.a"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && $(CMAKE_COMMAND) -P CMakeFiles/rabit_base.dir/cmake_clean_target.cmake
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rabit_base.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
rabit/CMakeFiles/rabit_base.dir/build: rabit/librabit_base.a

.PHONY : rabit/CMakeFiles/rabit_base.dir/build

rabit/CMakeFiles/rabit_base.dir/clean:
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && $(CMAKE_COMMAND) -P CMakeFiles/rabit_base.dir/cmake_clean.cmake
.PHONY : rabit/CMakeFiles/rabit_base.dir/clean

rabit/CMakeFiles/rabit_base.dir/depend:
	cd /Users/dingwang/flask_react/backend/xgboost/my_build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/dingwang/flask_react/backend/xgboost /Users/dingwang/flask_react/backend/xgboost/rabit /Users/dingwang/flask_react/backend/xgboost/my_build /Users/dingwang/flask_react/backend/xgboost/my_build/rabit /Users/dingwang/flask_react/backend/xgboost/my_build/rabit/CMakeFiles/rabit_base.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : rabit/CMakeFiles/rabit_base.dir/depend

