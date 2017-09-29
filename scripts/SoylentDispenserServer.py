#!/usr/bin/env python

import system
import time
import rospy
from servosix import ServoSix

def handle_dispense_soylent(req):
    ss.set_servo(6, 0)
    time.sleep(1)0
    ss.set_servo(6, 120)
    return True

def dispense_solyent_server():
    rospy.init_node('dispense_solyent_server')
    s = rospy.Service('dispense_soylent', DispenseSoylent, handle_dispense_soylent)
    ss = ServoSix()
    print "Soylent Dispenser service active"
    rospy.spin()

if __name__ == "__main__":
    dispense_solyent_server()