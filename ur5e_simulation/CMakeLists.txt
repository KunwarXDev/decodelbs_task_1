cmake_minimum_required(VERSION 3.8)
project(ur5e_simulation)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY
    config
    launch
    rviz
    urdf
    worlds
    docs
    images
  DESTINATION share/${Robotics_Arm}
)

install(
  PROGRAMS
    scripts/spawn_robot.py
    scripts/controller_test.py
    scripts/pick_place_demo.py
  DESTINATION lib/${Robotics_Arm}
)

ament_package()
