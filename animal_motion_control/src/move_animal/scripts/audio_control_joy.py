#!/usr/bin/env python
import rospy
import subprocess
from sensor_msgs.msg import Joy

def callback(msg):
    if msg.buttons[0]:
        subprocess.call("aplay -D default:CARD=Device ~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/left.wav", shell=True)
        
    if msg.buttons[1]: 
        subprocess.call("aplay -D default:CARD=Device ~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/front.wav", shell=True)
    
    if msg.buttons[3]: 	
        subprocess.call("aplay -D default:CARD=Device ~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/right.wav", shell=True)

def listener():
    rospy.init_node('audio_subscriber')
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()



if __name__ == '__main__':
    listener()
