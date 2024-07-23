#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldSubscriber(Node):
    def __init__(self):
        super().__init__("Hello_world_sub_node") # create a node (Hello_world_sub_node)
        self.subscriber_1 = self.create_subscription(String, "hello_world", self.subscriber_callback, 10) # make the node subscribe to topic(hello_world)
        
    def subscriber_callback(self, msg):
        print("Received: " + msg.data)


def main(args=None):
    rclpy.init()
    my_sub = HelloWorldSubscriber()
    print("Waiting for data to be published...")

    try:
        rclpy.spin(my_sub) # keeps the node running
    except KeyboardInterrupt:
        print("Terminating node...")
        my_sub.destroy_node() # destroys node on key board intrruption (ctrl+c)


if __name__ == '__main__':
    main()