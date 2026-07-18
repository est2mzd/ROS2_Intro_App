from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # turtlesim のウィンドウ
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        # キーボード操作ノード（別ターミナルで起動）
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            prefix='xterm -e' # ノードを xtermの新しいターミナルで起動
        )
    ])
