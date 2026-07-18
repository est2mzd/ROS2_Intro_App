from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            remappings=[
                ('/turtle1/cmd_vel', '/robot1/cmd_vel') # turtule1 --> robot1 に読み替える
            ]
        )
    ])
