#!/usr/bin/env python

import time
import rospy
from mealstation.srv import *
import piplates.RELAYplate as RELAY

def handle_dispense_water(req):
    RELAY.relayON(0,1)
    time.sleep(3)
    RELAY.relayOFF(0,1)
    return True

def dispense_water_server():
    rospy.init_node('dispense_water_server')
    s = rospy.Service('dispense_water', WaterDispenser, handle_dispense_water)
    print "Water dispenser service active"
    rospy.spin()

if __name__ == "__main__":
    RELAY.getID(0)
    dispense_water_server()