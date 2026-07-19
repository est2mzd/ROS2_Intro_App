import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker

class SimpleMarkerPublisher(Node):
    def __init__(self):
        super().__init__('simple_marker_publisher')
        self.pub = self.create_publisher(Marker, '/visualization_marker', 10)
        self.timer = self.create_timer(1.0, self.publish_marker)
        self.get_logger().info('Publishing red sphere Marker to /visualization_marker (frame_id=base_link)')

    def publish_marker(self):
        m = Marker()
        m.header.frame_id = 'base_link'
        m.header.stamp = self.get_clock().now().to_msg()
        m.ns = 'demo'
        m.id = 0
        m.type = Marker.SPHERE
        m.action = Marker.ADD
        m.pose.position.x = 1.0
        m.pose.position.y = 0.0
        m.pose.position.z = 0.5
        m.pose.orientation.w = 1.0
        m.scale.x = 0.3
        m.scale.y = 0.3
        m.scale.z = 0.3
        m.color.r = 1.0
        m.color.g = 0.0
        m.color.b = 0.0
        m.color.a = 1.0
        m.lifetime.sec = 0
        self.pub.publish(m)

def main():
    rclpy.init()
    node = SimpleMarkerPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
