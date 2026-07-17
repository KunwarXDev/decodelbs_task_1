# Project Architecture

## Components

- UR5e Robot
- ROS2 Humble
- Gazebo
- RViz2
- MoveIt2
- ros2_control

## Architecture

```text
MoveIt2
    │
Trajectory Planning
    │
Joint Trajectory Controller
    │
ros2_control
    │
Gazebo
    │
UR5e Robot
```
