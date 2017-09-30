#!/usr/bin/env python

import time
import rospy
from mealstation.srv import *
from servosix import ServoSix

def handle_dispense_soylent(req):
    ss.set_servo(6, 0)
    time.sleep(1)
    ss.set_servo(6, 120)
    return True

def dispense_solyent_server():
    rospy.init_node('dispense_solyent_server')
    s = rospy.Service('dispense_soylent', PowderDispenser, handle_dispense_soylent)
    ss = ServoSix()
    print "Soylent Dispenser service active"
    rospy.spin()

if __name__ == "__main__":
    dispense_solyent_server()