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
include rabit/CMakeFiles/rabit.dir/depend.make

# Include the progress variables for this target.
include rabit/CMakeFiles/rabit.dir/progress.make

# Include the compile flags for this target's objects.
include rabit/CMakeFiles/rabit.dir/flags.make

rabit/CMakeFiles/rabit.dir/src/allreduce_base.cc.o: rabit/CMakeFiles/rabit.dir/flags.make
rabit/CMakeFiles/rabit.dir/src/allreduce_base.cc.o: ../rabit/src/allreduce_base.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/dingwang/flask_react/backend/xgboost/my_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object rabit/CMakeFiles/rabit.dir/src/allreduce_base.cc.o"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rabit.dir/src/allreduce_base.cc.o -c /Users/dingwang/flask_react/backend/xgboost/rabit/src/allreduce_base.cc

rabit/CMakeFiles/rabit.dir/src/allreduce_base.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rabit.dir/src/allreduce_base.cc.i"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/dingwang/flask_react/backend/xgboost/rabit/src/allreduce_base.cc > CMakeFiles/rabit.dir/src/allreduce_base.cc.i

rabit/CMakeFiles/rabit.dir/src/allreduce_base.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rabit.dir/src/allreduce_base.cc.s"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/dingwang/flask_react/backend/xgboost/rabit/src/allreduce_base.cc -o CMakeFiles/rabit.dir/src/allreduce_base.cc.s

rabit/CMakeFiles/rabit.dir/src/allreduce_robust.cc.o: rabit/CMakeFiles/rabit.dir/flags.make
rabit/CMakeFiles/rabit.dir/src/allreduce_robust.cc.o: ../rabit/src/allreduce_robust.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/dingwang/flask_react/backend/xgboost/my_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object rabit/CMakeFiles/rabit.dir/src/allreduce_robust.cc.o"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rabit.dir/src/allreduce_robust.cc.o -c /Users/dingwang/flask_react/backend/xgboost/rabit/src/allreduce_robust.cc

rabit/CMakeFiles/rabit.dir/src/allreduce_robust.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rabit.dir/src/allreduce_robust.cc.i"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/dingwang/flask_react/backend/xgboost/rabit/src/allreduce_robust.cc > CMakeFiles/rabit.dir/src/allreduce_robust.cc.i

rabit/CMakeFiles/rabit.dir/src/allreduce_robust.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rabit.dir/src/allreduce_robust.cc.s"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/dingwang/flask_react/backend/xgboost/rabit/src/allreduce_robust.cc -o CMakeFiles/rabit.dir/src/allreduce_robust.cc.s

rabit/CMakeFiles/rabit.dir/src/engine.cc.o: rabit/CMakeFiles/rabit.dir/flags.make
rabit/CMakeFiles/rabit.dir/src/engine.cc.o: ../rabit/src/engine.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/dingwang/flask_react/backend/xgboost/my_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object rabit/CMakeFiles/rabit.dir/src/engine.cc.o"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rabit.dir/src/engine.cc.o -c /Users/dingwang/flask_react/backend/xgboost/rabit/src/engine.cc

rabit/CMakeFiles/rabit.dir/src/engine.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rabit.dir/src/engine.cc.i"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/dingwang/flask_react/backend/xgboost/rabit/src/engine.cc > CMakeFiles/rabit.dir/src/engine.cc.i

rabit/CMakeFiles/rabit.dir/src/engine.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rabit.dir/src/engine.cc.s"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/dingwang/flask_react/backend/xgboost/rabit/src/engine.cc -o CMakeFiles/rabit.dir/src/engine.cc.s

rabit/CMakeFiles/rabit.dir/src/c_api.cc.o: rabit/CMakeFiles/rabit.dir/flags.make
rabit/CMakeFiles/rabit.dir/src/c_api.cc.o: ../rabit/src/c_api.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/dingwang/flask_react/backend/xgboost/my_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object rabit/CMakeFiles/rabit.dir/src/c_api.cc.o"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rabit.dir/src/c_api.cc.o -c /Users/dingwang/flask_react/backend/xgboost/rabit/src/c_api.cc

rabit/CMakeFiles/rabit.dir/src/c_api.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rabit.dir/src/c_api.cc.i"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/dingwang/flask_react/backend/xgboost/rabit/src/c_api.cc > CMakeFiles/rabit.dir/src/c_api.cc.i

rabit/CMakeFiles/rabit.dir/src/c_api.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rabit.dir/src/c_api.cc.s"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && /usr/local/bin/g++-8 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/dingwang/flask_react/backend/xgboost/rabit/src/c_api.cc -o CMakeFiles/rabit.dir/src/c_api.cc.s

# Object files for target rabit
rabit_OBJECTS = \
"CMakeFiles/rabit.dir/src/allreduce_base.cc.o" \
"CMakeFiles/rabit.dir/src/allreduce_robust.cc.o" \
"CMakeFiles/rabit.dir/src/engine.cc.o" \
"CMakeFiles/rabit.dir/src/c_api.cc.o"

# External object files for target rabit
rabit_EXTERNAL_OBJECTS =

rabit/librabit.a: rabit/CMakeFiles/rabit.dir/src/allreduce_base.cc.o
rabit/librabit.a: rabit/CMakeFiles/rabit.dir/src/allreduce_robust.cc.o
rabit/librabit.a: rabit/CMakeFiles/rabit.dir/src/engine.cc.o
rabit/librabit.a: rabit/CMakeFiles/rabit.dir/src/c_api.cc.o
rabit/librabit.a: rabit/CMakeFiles/rabit.dir/build.make
rabit/librabit.a: rabit/CMakeFiles/rabit.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/dingwang/flask_react/backend/xgboost/my_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX static library librabit.a"
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && $(CMAKE_COMMAND) -P CMakeFiles/rabit.dir/cmake_clean_target.cmake
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rabit.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
rabit/CMakeFiles/rabit.dir/build: rabit/librabit.a

.PHONY : rabit/CMakeFiles/rabit.dir/build

rabit/CMakeFiles/rabit.dir/clean:
	cd /Users/dingwang/flask_react/backend/xgboost/my_build/rabit && $(CMAKE_COMMAND) -P CMakeFiles/rabit.dir/cmake_clean.cmake
.PHONY : rabit/CMakeFiles/rabit.dir/clean

rabit/CMakeFiles/rabit.dir/depend:
	cd /Users/dingwang/flask_react/backend/xgboost/my_build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/dingwang/flask_react/backend/xgboost /Users/dingwang/flask_react/backend/xgboost/rabit /Users/dingwang/flask_react/backend/xgboost/my_build /Users/dingwang/flask_react/backend/xgboost/my_build/rabit /Users/dingwang/flask_react/backend/xgboost/my_build/rabit/CMakeFiles/rabit.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : rabit/CMakeFiles/rabit.dir/depend
