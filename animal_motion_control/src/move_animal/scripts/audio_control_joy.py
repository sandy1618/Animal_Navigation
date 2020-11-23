#!/usr/bin/env python
import rospy
import subprocess
from sensor_msgs.msg import Joy
left = 0 
right = 0 
forward = 0 
prev_left = 0
prev_right = 0 
prev_forward = 0 
left_state = 0 
right_state = 0 
forward_state = 0 

def callback(msg):
    global left 
    global right
    global forward 
    global prev_left
    global prev_right 
    global prev_forward 
    global left_state 
    global right_state 
    global forward_state 

    left = msg.buttons[0]
    right = msg.buttons[1]
    forward = msg.buttons[3]

    if prev_left == 0 and left == 1:
        left_state = 1 
    else :
        left_state = 0

    # state_checker
    if left_state == 1:
        subprocess.call("aplay  ~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/left.wav", shell=True)
        
    if right_state == 1: 
        subprocess.call("aplay  ~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/forward.wav", shell=True)
    
    if forward_state == 1: 	
         subprocess.call("aplay ~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/right.wav", shell=True)

def listener():
    rospy.init_node('audio_subscriber')
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()



if __name__ == '__main__':
    listener()
