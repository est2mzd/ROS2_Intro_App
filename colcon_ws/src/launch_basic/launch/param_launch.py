from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Launch arguments (string by default)
    bg_r = LaunchConfiguration('bg_r', default='200')
    bg_g = LaunchConfiguration('bg_g', default='200')
    bg_b = LaunchConfiguration('bg_b', default='255')

    return LaunchDescription([
        DeclareLaunchArgument('bg_r', default_value='200', description='Background red (0-255)'),
        DeclareLaunchArgument('bg_g', default_value='200', description='Background green (0-255)'),
        DeclareLaunchArgument('bg_b', default_value='255', description='Background blue (0-255)'),

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim_with_params',
            parameters=[{
                'background_r': bg_r,
                'background_g': bg_g,
                'background_b': bg_b
            }]
        )
    ])