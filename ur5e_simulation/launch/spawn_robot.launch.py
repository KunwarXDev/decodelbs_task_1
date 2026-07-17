from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    spawn = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity',
            'ur5e',
            '-topic',
            'robot_description'
        ],
        output='screen'
    )

    return LaunchDescription([
        spawn
    ])
