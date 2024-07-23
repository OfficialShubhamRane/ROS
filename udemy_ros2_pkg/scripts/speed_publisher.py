#!/user/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Speed_publisher(Node):
    rpm = 10
    wheel_circumference = 5

    def __init__(self):
        super().__init__("speed_publisher") # create a node (Hello_world_sub_node)
        self.subscriber_1 = self.create_subscription(Int16, "rpm", self.subscriber_callback, 10) # make the node subscribe to topic(hello_world)
        
        self.publisher_1 = self.create_publisher(Int16,"/speed",10)
        self.timer = self.create_timer(1.0,self.publish_speed)

    def subscriber_callback(self, msg: Int16):
        self.get_logger().info("Received RPM: %d" % msg.data)  # Use logger for output
        self.rpm = msg.data

    def publish_speed(self):
        speed = self.rpm * self.wheel_circumference
        msg = Int16()
        msg.data = speed
        self.publisher_1.publish(msg)
        self.get_logger().info("Published Speed: %d" % speed) # Use logger for output


def main(args=None):
    rclpy.init()
    speed_pub = Speed_publisher()
    print("Speed publisher node running...")

    try:
        rclpy.spin(speed_pub)
    except KeyboardInterrupt:
        print("Terminating speed publisher node...")
        speed_pub.destroy_node()

if __name__ == '__main__':
    main()