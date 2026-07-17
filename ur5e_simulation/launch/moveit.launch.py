from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    move_group = Node(
        package='moveit_ros_move_group',
        executable='move_group',
        output='screen'
    )

    return LaunchDescription([
        move_group
    ])
