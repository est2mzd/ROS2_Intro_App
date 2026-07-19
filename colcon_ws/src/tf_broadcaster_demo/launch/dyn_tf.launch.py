from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf_broadcaster_demo',
            executable='dyn_tf_broadcaster',
            output='screen'
        )
    ])
