#!/usr/bin/env python

import rospy
from mealstation.srv import *

def dispense_soylent():
    rospy.wait_for_service('dispense_soylent')
    try:
        dispense_soylent = rospy.ServiceProxy('dispense_soylent', PowderDispenser)
        resp1 = dispense_soylent(1)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def dispense_water():
    rospy.wait_for_service('dispense_water')
    try:
        dispense_water = rospy.ServiceProxy('dispense_water', WaterDispenser)
        resp1 = dispense_water(1)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    dispense_water()