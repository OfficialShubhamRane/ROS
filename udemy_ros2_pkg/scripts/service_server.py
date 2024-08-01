#!/usr/bin/python3

import rclpy
from rclpy.node import Node

from udemy_ros2_pkg.srv import OddEvenCheck

class OddEvenCheckServer(Node):
    def __init__(self):
        super().__init__("odd_even_check_server_node")
        self.server_ = self.create_service(OddEvenCheck, "odd_even_check", self.odd_even_check_callback)

    def odd_even_check_callback(self, request, response):
        print("request received")

        if request.number % 2 == 0:
            response.decision = "Even"
        elif request.number % 2 == 1:
            response.decision = "Odd"
        else:
            response.decision = "Error"

        print(f"Number: {request.number} is {response.decision}")
        return response 

def main(args=None):
    rclpy.init()
    server_node = OddEvenCheckServer()
    print("OddEven Check Server node running...")

    try:
        rclpy.spin(server_node) # keeps the node running
    except KeyboardInterrupt:
        print("Terminating node...")
        server_node.destroy_node() # destroys node on key board intrruption (ctrl+c)


if __name__ == '__main__':
    main()