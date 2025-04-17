import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker')

        self.declare_parameter('frequency', 1.0)
        freq = self.get_parameter('frequency').get_parameter_value().double_value

        self.get_logger().info(f'📡 Fréquence configurée : {freq} Hz')

        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0 / freq, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Bonjour depuis le talker 😄'
        self.publisher.publish(msg)
        self.get_logger().info(f'🔊 Envoi : {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
