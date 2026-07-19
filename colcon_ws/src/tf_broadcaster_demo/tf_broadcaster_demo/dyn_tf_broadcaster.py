import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
import math

class DynamicTFBroadcaster(Node):
    def __init__(self):
        super().__init__('dynamic_tf_broadcaster')
        self.br = TransformBroadcaster(self)
        self.start = self.get_clock().now()
        self.timer = self.create_timer(0.1, self.publish_tf)

    def publish_tf(self):
        t = (self.get_clock().now() - self.start).nanoseconds * 1e-9

        msg = TransformStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'odom'
        msg.child_frame_id = 'base_link'

        msg.transform.translation.x = math.cos(t)
        msg.transform.translation.y = math.sin(t)
        msg.transform.translation.z = 0.0

        # quaternion around Z axis
        z = math.sin(t / 2.0)
        w = math.cos(t / 2.0)
        msg.transform.rotation.x = 0.0
        msg.transform.rotation.y = 0.0
        msg.transform.rotation.z = z
        msg.transform.rotation.w = w

        self.br.sendTransform(msg)

def main():
    rclpy.init()
    node = DynamicTFBroadcaster()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
