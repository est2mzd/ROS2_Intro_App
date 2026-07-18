from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim1',
            namespace='robot1' # ネームスペース
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim2',
            namespace='robot2' # ネームスペース
        )
    ])
