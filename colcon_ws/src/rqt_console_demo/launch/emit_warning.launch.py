from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rqt_console_demo',
            executable='emit_logs',
            name='log_emitter',
            output='screen'
        )
    ])
