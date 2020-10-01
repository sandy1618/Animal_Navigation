#!/usr/bin/env python
import rospy
import subprocess
from sensor_msgs.msg import Joy

def callback(msg):
    if msg.buttons[10]:
        subprocess.call("aplay clicker_single.wav", shell=True)
        
    if msg.buttons[11]: 
        subprocess.call("aplay iguchisan_look.wav", shell=True)
    
    if msg.buttons[12]: 	
        subprocess.call("aplay mikayamasan_look.wav", shell=True)

def listener():
    rospy.init_node('audio_subscriber')
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()



if __name__ == '__main__':
    listener()
