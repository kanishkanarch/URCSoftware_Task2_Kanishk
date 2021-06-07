#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64


dec = 0
rospy.init_node("decreasing")
rate = rospy.Rate(1)
publisher = rospy.Publisher("/dec", Int64)

while not rospy.is_shutdown():
    publisher.publish(dec)
    dec -= 1
    rate.sleep()