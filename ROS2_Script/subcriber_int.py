import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MySubscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'counter_value',
            self.callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def callback(self, msg):
        self.get_logger().info('received: %d' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = MySubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
