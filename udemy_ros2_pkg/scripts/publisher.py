#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldPublisher(Node):
    def __init__(self):
        super().__init__("hello_world_pub_node") # create a node
        self.publisher_1 = self.create_publisher(String, "hello_world", 10) # create a publisher(publisher_1) with topic(hello_world)
        self.timer = self.create_timer(0.5, self.publish_hello_world) # call a method ever half second
        self.counter = 0

    def publish_hello_world(self): # this method publishes message
        msg = String()
        msg.data = "Hello World " + str(self.counter)
        self.publisher_1.publish(msg) # publish message to publisher (publisher_1)
        self.counter += 1

def main(args=None):
    rclpy.init()
    my_pub = HelloWorldPublisher()
    print("New Publisher node running...")

    try:
        rclpy.spin(my_pub) # keeps the node running
    except KeyboardInterrupt:
        print("Terminating node...")
        my_pub.destroy_node() # destroys node on key board intrruption (ctrl+c)


if __name__ == '__main__':
    main()