#!/usr/bin/env python
import rospy
import subprocess
from sensor_msgs.msg import Joy
from light_signal_msg.msg import light_signal
left = 0 
right = 0 
forward = 0 
prev_left = 0
prev_right = 0 
prev_forward = 0 
left_state = 0 
right_state = 0 
forward_state = 0 
stop_state = 0
count = 0
AUDIO_WAIT_TIME_THRESHOLD = 5
prev_time = 0
now_time = 0


# def state_changer(state, prev, now, time):
#     global left 
#     global right
#     global forward 
#     global prev_left
#     global prev_right 
#     global prev_forward 
#     global left_state 
#     global right_state 
#     global forward_state 
#     global stop_state 
#     global count
#     global prev_time
#     global now_time
#     global AUDIO_WAIT_TIME_THRESHOLD

#     if prev == 0 and now == 1:
#         state = 1   
#         prev_time  = time      
#     elif prev == 1 and now == 0:
#         state = 0
#         prev_time  = time        
#     elif prev == 1 and now == 1:
#         state = 2
#         now_time = time
#         if (now_time - prev_time) == AUDIO_WAIT_TIME_THRESHOLD:
#             state = 1
#             prev_time = time

#      # UPDATING PREV. STATES.  
#     prev_left = left
    
def cmd_sig_control(msg):
    global left 
    global right
    global forward 
    global prev_left
    global prev_right 
    global prev_forward 
    global left_state 
    global right_state 
    global forward_state 
    global stop_state 
    global count
    global prev_time
    global now_time
    global AUDIO_WAIT_TIME_THRESHOLD
    
    left = msg.left
    right = msg.right
    forward = msg.forward
    time = msg.header.stamp.secs
    # rospy.loginfo(time)
    
   
    
#___________________STATE_BASED____________________________

    # left_state,prev_left = state_changer(state = left_state, prev = prev_left, now = msg.left, time=time)

    if prev_left == 0 and msg.left == 1:
        left_state = 1   
        prev_time  = time      
    elif prev_left == 1 and msg.left == 0:
        left_state = 0
        prev_time  = time        
    elif prev_left == 1 and msg.left == 1:
        left_state = 2
        now_time = time
        if (now_time - prev_time) == AUDIO_WAIT_TIME_THRESHOLD and stop_state == 0:
            left_state = 1
            prev_time = time        
    else :
        left_state = 0
    
    if prev_right == 0 and msg.right == 1:
        right_state = 1   
        prev_time  = time      
    elif prev_right == 1 and msg.right == 0:
        right_state = 0
        prev_time  = time        
    elif prev_right == 1 and msg.right == 1:
        right_state = 2
        now_time = time
        if (now_time - prev_time) == AUDIO_WAIT_TIME_THRESHOLD and stop_state == 0:
            right_state = 1
            prev_time = time        
    else :
        right_state = 0
    
    if prev_forward == 0 and msg.forward == 1:
        forward_state = 1   
        prev_time  = time      
    elif prev_forward == 1 and msg.forward == 0:
        forward_state = 0
        prev_time  = time        
    elif prev_forward == 1 and msg.forward == 1:
        forward_state = 2
        now_time = time
        if (now_time - prev_time) == AUDIO_WAIT_TIME_THRESHOLD and stop_state == 0:
            forward_state = 1
            prev_time = time        
    else :
        forward_state = 0
    
    # if prev_left == 0 and msg.left == 1:
    #     left_state = 1         
    # else :
    #     left_state = 0
    # prev_left = left
    # if prev_right == 0 and msg.right == 1:
    #     right_state = 1 
    #     prev_right = right
    # else :
    #     right_state = 0
    #     prev_right = right

    # if prev_forward == 0 and msg.forward == 1:
    #     forward_state = 1 
    #     prev_forward = forward
    # else :
    #     forward_state = 0
    #     prev_forward = forward

    if left*right*forward == 1:
        count +=1
        if count == 20 or count == 100:
            stop_state = 1
        else:
            stop_state = 2
        
    # UPDATING PREV. STATES.  
    prev_left = left
    prev_right = right
    prev_forward = forward
    aplay_cmd_pi = "aplay -D default:CARD=Device "
    # aplay_cmd_pi = "aplay "
    aplay_path = "~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/"
    sounds = ["left.wav","front.wav","right.wav","stop.wav"]

  

    # state_checker
    if left_state == 1:
        subprocess.call(aplay_cmd_pi+aplay_path+sounds[0], shell=True) 
               
    if forward_state == 1: 
        subprocess.call(aplay_cmd_pi+aplay_path+sounds[1], shell=True)  

    if right_state == 1: 
        subprocess.call(aplay_cmd_pi+aplay_path+sounds[2], shell=True)        
       
    if stop_state == 1: 	
        subprocess.call(aplay_cmd_pi+aplay_path+sounds[3], shell=True)        
       



def listener():
    #Human suit 
    subprocess.call("amixer -c 1 cset numid=6 30,30", shell=True)
    #lenevo pc
    subprocess.call("amixer set Master 100%", shell=True) 

    rospy.init_node('audio_control_cmd_sig')
    rospy.Subscriber("cmd_sig",light_signal,cmd_sig_control)
    rospy.spin()



if __name__ == '__main__':
    listener()
