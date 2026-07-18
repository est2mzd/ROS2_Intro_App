"""
1秒ごとに、 Hello N と chatter という topic に送信し続ける publisher node 
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class MinimalPublisher(Node):
    """
    定常円運動
    """
    def __init__(self):
        # Nodeクラスの初期化
        super().__init__('minimal_publisher')
        
        # String を chatter というトピックに送る publisherを作成. buffer size = 10
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        
        # 1秒間隔で、 自作関数 self.timer_callback を呼び出す timer を作成
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # カウンターの初期化
        self.count = 0
    
    # 1秒ごとに呼ばれる自作関数
    def timer_callback(self):
        msg = String()
        msg.data = f'Hello {self.count}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Pusblishing: "{msg.data}"')
        self.count += 1


class TurtleController(Node):
    """
    螺旋を描く
    """
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0
    
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0 + self.count*0.05 # 少しずつ速度を上げることで半径を大きくする v=r*w
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
        self.get_logger().info(f'Pusblished: linear={msg.linear.x}, angular={msg.angular.z}')
        
        self.count += 1


class EightFigureController(Node):
    """
    8の字を描く
    """
    def __init__(self):
        super().__init__('eight_figure_controller')
        
        self.linear_speed = 1.0
        self.angular_speed = 2.0
        self.current_angular_z = self.angular_speed
        
        self.last_theta = None
        self.cumulative_angle = 0.0
        
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        
        self.timer = self.create_timer(0.1, self.timer_callback)
    
    def pose_callback(self, msg):
        theta = msg.theta
        
        # 差分を計算し、-π〜+πにラップ
        if self.last_theta is not None:
            delta = theta - self.last_theta
            delta = (delta + math.pi) % (2 * math.pi) - math.pi # -pi to +pi
            self.cumulative_angle += delta
            
            # 1回転（約2π）以上で方向反転
            if abs(self.cumulative_angle) > 2 * math.pi:
                self.current_angular_z *= -1
                self.cumulative_angle = 0.0
                self.get_logger().info('--> Inverse Direction')

        self.last_theta = theta
        
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.linear_speed
        msg.angular.z = self.current_angular_z
        self.publisher_.publish(msg)
        
def main(args=None):
    test_type = 3
    rclpy.init(args=args)
    #
    if test_type == 1:
        node = MinimalPublisher()
    elif test_type == 2:
        node = TurtleController()
    elif test_type == 3:
        node = EightFigureController()
    else:
        node = MinimalPublisher()
    #
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()