import math
import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

class ArrayMarkerPublisher(Node):
    def __init__(self):
        super().__init__('array_marker_publisher')
        self.pub = self.create_publisher(MarkerArray, '/visualization_marker_array', 10)
        self.t = 0.0
        self.timer = self.create_timer(0.5, self.publish_array)
        self.get_logger().info('Publishing LINE_STRIP path + TEXT via /visualization_marker_array (frame_id=base_link)')

    def publish_array(self):
        arr = MarkerArray()

        line = Marker()
        line.header.frame_id = 'base_link'
        line.header.stamp = self.get_clock().now().to_msg()
        line.ns = 'path'
        line.id = 1
        line.type = Marker.LINE_STRIP
        line.action = Marker.ADD
        line.scale.x = 0.05
        line.color.r = 0.1
        line.color.g = 0.8
        line.color.b = 1.0
        line.color.a = 1.0
        line.pose.orientation.w = 1.0

        line.points = []
        for i in range(80):
            ang = 0.2 * i + self.t
            r = 0.02 * i
            p = Point()
            p.x = 0.5 + r * math.cos(ang)
            p.y = 0.0 + r * math.sin(ang)
            p.z = 0.1 * math.sin(0.5 * ang)
            line.points.append(p)
        arr.markers.append(line)

        text = Marker()
        text.header.frame_id = 'base_link'
        text.header.stamp = line.header.stamp
        text.ns = 'label'
        text.id = 2
        text.type = Marker.TEXT_VIEW_FACING # 文字が常に、画面の方を向く設定
        text.action = Marker.ADD
        text.pose.position.x = 0.5
        text.pose.position.y = 0.0
        text.pose.position.z = 1.0
        text.scale.z = 0.2
        text.color.r = 1.0
        text.color.g = 1.0
        text.color.b = 1.0
        text.color.a = 1.0
        text.text = 'MarkerArray demo'
        arr.markers.append(text)

        self.pub.publish(arr)
        self.t += 0.2

def main():
    rclpy.init()
    node = ArrayMarkerPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
