# Installation Guide

## Requirements

- Ubuntu 22.04
- ROS2 Humble
- Gazebo
- RViz2
- MoveIt2

## Clone Repository

```bash
git clone <repository_url>
```

## Build

```bash
cd ~/ur5e_ws
colcon build --symlink-install
source install/setup.bash
```

## Launch

```bash
ros2 launch ur5e_simulation ur5e_simulation.launch.py
```
