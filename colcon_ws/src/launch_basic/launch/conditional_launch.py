from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    use_teleop = LaunchConfiguration('use_teleop') # 引数の use_teleop:=true/false を取得

    return LaunchDescription([
        DeclareLaunchArgument('use_teleop', default_value='true'), # デフォルトはtrue

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),

        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            prefix='xterm -e',
            condition=IfCondition(use_teleop) # 引数の use_teleop:=true のときに、このNodeが実行される
        )
    ])
