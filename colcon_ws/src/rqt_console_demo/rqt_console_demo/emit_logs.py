import rclpy
from rclpy.node import Node

class LogEmitter(Node):
    def __init__(self):
        super().__init__('log_emitter')
        self.c = 0
        self.timer = self.create_timer(1.0, self.tick)
        self.get_logger().info("log_emitter started (INFO every sec, WARN every 3, ERROR every 5).")

    def tick(self):
        self.c += 1
        if self.c % 5 == 0:
            self.get_logger().error(f"ERROR {self.c}")
        elif self.c % 3 == 0:
            self.get_logger().warn(f"WARN {self.c}")
        else:
            self.get_logger().info(f"INFO {self.c}")

def main():
    rclpy.init()
    node = LogEmitter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
