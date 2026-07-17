#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class ControllerTest(Node):

    def __init__(self):
        super().__init__('controller_test')
        self.get_logger().info("Controller Test Running")


def main(args=None):

    rclpy.init(args=args)

    node = ControllerTest()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
