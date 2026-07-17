# UR5e Robotic Arm Simulation using ROS2 Humble, Gazebo & MoveIt2

A simulation project for the **Universal Robots UR5e** robotic manipulator built using **ROS2 Humble**, **Gazebo**, and **MoveIt2**. The repository is organized to demonstrate robot description, simulation, controller configuration, visualization, and a foundation for motion planning.

---

## Features

- UR5e Robot Description
- ROS2 Humble Integration
- Gazebo Simulation
- RViz Visualization
- ros2_control Configuration
- Joint Trajectory Controller
- MoveIt2 Motion Planning Setup
- Pick and Place Project Structure
- Modular ROS2 Package Layout

---

## Tech Stack

| Technology | Version |
|------------|---------|
| Ubuntu | 22.04 |
| ROS2 | Humble Hawksbill |
| Gazebo | Gazebo Classic |
| MoveIt2 | Humble |
| Language | Python, XML, YAML |
| Build System | ament_cmake |

---

# Repository Structure

```text
ur5e_simulation/
│
├── config/
├── docs/
├── images/
├── launch/
├── rviz/
├── scripts/
├── urdf/
├── worlds/
│
├── CMakeLists.txt
├── package.xml
├── README.md
├── LICENSE
└── .gitignore
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/<KunwarXDev>/ur5e_simulation.git
```

Go to the workspace:

```bash
cd ~/ur5e_ws
```

Install dependencies:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

Build:

```bash
colcon build --symlink-install
```

Source the workspace:

```bash
source install/setup.bash
```

---

# Launch Simulation

```bash
ros2 launch ur5e_simulation ur5e_simulation.launch.py
```

---

# Project Architecture

```
RViz
   │
Robot State Publisher
   │
URDF/Xacro
   │
ros2_control
   │
Joint Controllers
   │
Gazebo
   │
UR5e Robot
```

---

# Project Components

## URDF

Contains the robot description files.

## Launch

ROS2 launch files used to start the simulation.

## Config

Controller and MoveIt2 configuration files.

## Worlds

Gazebo simulation environments.

## RViz

Visualization configuration.

## Scripts

Python ROS2 nodes for testing and future automation.

---

# Future Improvements

- MoveIt2 Motion Planning
- Pick and Place Demonstration
- Vision-Based Object Detection
- Gear Detection Integration
- Gripper Support
- Collision Object Planning
- Autonomous Manipulation

---

# Screenshots

## Gazebo

_/home/kunwar/Downloads/WhatsApp Image 2026-07-17 at 17.19.15.jpeg_

## RViz

_/home/kunwar/Downloads/WhatsApp Image 2026-07-17 at 17.19.16.jpeg_


# License

This project is released under the MIT License.

---

# Author

**Kunwar Singh**

Electronics & Communication Engineering

KIET Group of Institutions

GitHub: https://github.com/KunwarXDev

---

## Acknowledgements

This project uses and builds upon the ROS2 ecosystem and the official Universal Robots description packages where applicable.
