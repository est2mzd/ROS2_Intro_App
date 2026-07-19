from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf_listener_demo',
            executable='tf_listener_node',
            output='screen'
        )
    ])
