import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String

def count_callback(msg):
    node.get_logger().info("Listen: %d" % msg.data)

def time_callback(msg):
    node.get_logger().info("現在時刻: %s" % msg.data)

rclpy.init()
node = Node("listener")
sub_count = node.create_subscription(Int16, "countup", count_callback, 10)
sub_time = node.create_subscription(String, "current_time", time_callback, 10)
rclpy.spin(node)

