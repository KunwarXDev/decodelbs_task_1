#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class SpawnRobot(Node):

    def __init__(self):
        super().__init__('spawn_robot')
        self.get_logger().info("Spawn Robot Node Started")


def main(args=None):
    rclpy.init(args=args)

    node = SpawnRobot()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
