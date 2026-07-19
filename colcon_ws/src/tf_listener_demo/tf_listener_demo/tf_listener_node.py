import rclpy
from rclpy.node import Node
from tf2_ros import Buffer, TransformListener
import math

class TFListenerNode(Node):
    def __init__(self):
        super().__init__('tf_listener_node')
        self.buffer = Buffer()
        self.listener = TransformListener(self.buffer, self)
        self.timer = self.create_timer(0.5, self.on_timer)

    def on_timer(self):
        try:
            tf = self.buffer.lookup_transform('odom', 'base_link', rclpy.time.Time())
        except Exception as e:
            self.get_logger().warn(f'TF not available yet: {e}')
            return

        t = tf.transform.translation
        r = tf.transform.rotation

        # yaw from quaternion (Z-axis rotation)
        yaw = math.atan2(2.0*(r.w*r.z), 1.0 - 2.0*(r.z*r.z))

        self.get_logger().info(f"odom -> base_link : x={t.x:.2f}, y={t.y:.2f}, θ={yaw:.2f}")

def main():
    rclpy.init()
    node = TFListenerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
