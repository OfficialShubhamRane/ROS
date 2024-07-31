#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class RPM_publisher(Node):
    def __init__(self):
        super().__init__("rpm_pub_node")
        self.pub = self.create_publisher(Int16,"rpm",10)
        self.timer = self.create_timer(1, self.publish_rpm)

    def publish_rpm(self):
        msg = Int16()
        msg.data = 10
        self.pub.publish(msg)


def main(args=None):
    rclpy.init()
    rpm_pub = RPM_publisher()
    print("RPM publisher node running...")

    try:
        rclpy.spin(rpm_pub)
    except KeyboardInterrupt:
        print("Terminating RPM publisher node...")
        rpm_pub.destroy_node()

if __name__ == '__main__':
    main()