from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='marker_demo_pkg',
            executable='simple_marker_pub',
            name='simple_marker_pub',
            output='screen'
        ),
        Node(
            package='marker_demo_pkg',
            executable='array_marker_pub',
            name='array_marker_pub',
            output='screen'
        ),
    ])
