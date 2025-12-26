import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleMover(Node):
    def __init__(self):
        super().__init__('circle_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_circle)

    def move_circle(self):
        msg = Twist()
        msg.linear.x = 2.0  # İleri hız
        msg.angular.z = 1.0 # Dönüş hızı
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CircleMover()
    rclpy.spin(node)
    rclpy.shutdown()
