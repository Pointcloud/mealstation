#!/usr/bin/env python

import time
import rospy
from mealstation.srv import *
from servosix import ServoSix

def handle_dispense_soylent(req):
    ss.set_servo(6, 0)
    time.sleep(2)
    ss.set_servo(6, 121)
    return True

def dispense_solyent_server():
    rospy.init_node('dispense_solyent_server')
    s = rospy.Service('dispense_soylent', PowderDispenser, handle_dispense_soylent)
    print "Soylent Dispenser service active"
    rospy.spin()

if __name__ == "__main__":
    ss = ServoSix()
    dispense_solyent_server()