#!/usr/bin/env python
#github test comment 2

import rospy
from std_msgs.msg import String

def set_mode():
    pub = rospy.Publisher('/robotis/base/set_mode_msg',String, queue_size=0)
    rospy.init_node('set_mode', anonymous=True)
    msg = "set_mode"
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown(): 
        pub.publish(msg) 
        rate.sleep() 

if __name__ == '__main__':
    try:
        set_mode()
    except rospy.ROSInterruptException:
        pass
