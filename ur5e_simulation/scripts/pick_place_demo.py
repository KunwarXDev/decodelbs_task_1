#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class PickPlaceDemo(Node):

    def __init__(self):
        super().__init__('pick_place_demo')
        self.get_logger().info("Pick and Place Demo Started")


def main(args=None):

    rclpy.init(args=args)

    node = PickPlaceDemo()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
