from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    gazebo = ExecuteProcess(
        cmd=[
            'gazebo',
            '--verbose'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo
    ])
