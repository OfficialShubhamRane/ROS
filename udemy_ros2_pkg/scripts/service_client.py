#!/usr/bin/python3

import rclpy
from rclpy.node import Node

from udemy_ros2_pkg.srv import OddEvenCheck

class OddEvenCheckClient(Node):
    def __init__(self):
        super().__init__("odd_even_check_client_node")
        self.client = self.create_client(OddEvenCheck, "odd_even_check")
        self.req = OddEvenCheck.Request()

    def send_request(self, number):
        self.req.number = number
        self.client.wait_for_service()
        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)

        self.result = self.future.result()
        return self.result
    
        

def main(args=None):
    rclpy.init()
    client_node = OddEvenCheckClient()
    print("OddEven Check Client running...")

    try:
        user_input = int(input("Enter a number: "))
        response = client_node.send_request(user_input)
        print("server returned: ", response)
    except KeyboardInterrupt:
        print("Terminating node...")
        client_node.destroy_node() # destroys node on key board intrruption (ctrl+c)


if __name__ == '__main__':
    main()