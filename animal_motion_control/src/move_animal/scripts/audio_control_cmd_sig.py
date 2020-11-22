#!/usr/bin/env python
import rospy
import subprocess
from sensor_msgs.msg import Joy
from light_signal_msg.msg import light_signal


def cmd_sig_control(msg):
    if msg.left == 1:
        subprocess.call("aplay ~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/left.wav", shell=True)
        
    if msg.forward == 1: 
        subprocess.call("aplay ~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/front.wav", shell=True)
    
    if msg.right == 1: 	
         subprocess.call("aplay ~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/right.wav", shell=True)

def listener():
    rospy.init_node('audio_control_cmd_sig')
    rospy.Subscriber("cmd_sig",light_signal,cmd_sig_control)
    rospy.spin()



if __name__ == '__main__':
    listener()
