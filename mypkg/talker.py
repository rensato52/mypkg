# SPDX-FileCopyrightText: 2023 Ren Sato
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String
from time import time, localtime, strftime

class Talker():
    def __init__(self, node):
        self.pub_count = node.create_publisher(Int16, "countup", 10)
        self.pub_time = node.create_publisher(String, "current_time", 10)
        self.n = 0
        self.node = node

        node.create_timer(0.5, self.cb)

    def cb(self):
        msg_count = Int16()
        msg_count.data = self.n
        self.pub_count.publish(msg_count)

        msg_time = String()
        current_time = strftime("%Y-%m-%d %H:%M:%S", localtime(time()))
        msg_time.data = current_time
        self.pub_time.publish(msg_time)

        self.n += 1

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

