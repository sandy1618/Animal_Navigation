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
# AUDIO_WAIT_TIME_THRESHOLD
prev_time = 0
now_time = 0
counter = 0
    
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
    global counter # for counting no. of times warning to be played. 
    
    left = msg.left
    right = msg.right
    forward = msg.forward
    sound = msg.sound
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


    if prev_sound == 0 and msg.sound == 1:
        sound_state = 1   
        prev_time  = time   # for time delay counter. 
        counter += 1   
    elif prev_sound == 1 and msg.sound == 0:
        sound_state = 0
        prev_time  = time   
        counter = 0     
    elif prev_sound == 1 and msg.sound == 1:
        sound_state = 2
        now_time = time
        if (now_time - prev_time) == AUDIO_WAIT_TIME_THRESHOLD and stop_state == 0 and counter < 3:
            counter +=1
            sound_state = 1
            prev_time = time        
    else :
        sound_state = 0


    # State based approach for prewarning sound signal 
    # UPDATING PREV. STATES.  
    prev_sound = sound

    #Human suit
    # aplay_cmd_pi = "aplay -D default:CARD=Device " # space must be there at end. 
    #Lenevo PC
    aplay_cmd_pi = "aplay "
    # aplay_cmd_pi = "aplay "
    aplay_path = "~/Animal_Navigation/animal_motion_control/src/move_animal/scripts/"
    sounds = ["approaching_goal.wav","goal_ahead.wav","turn_ahead.wav"]

  

    # state_checker      
    if sound_state == 1:
        subprocess.call(aplay_cmd_pi+aplay_path+sounds[1], shell=True)   


def listener():
    global AUDIO_WAIT_TIME_THRESHOLD
    #Human suit 
    # subprocess.call("amixer -c 1 cset numid=6 30,30", shell=True)
    #lenevo pc
    subprocess.call("amixer set Master 100%", shell=True) 

    rospy.init_node('audio_control_cmd_sig')
    AUDIO_WAIT_TIME_THRESHOLD = rospy.get_param('~AUDIO_WAIT_TIME_THRESHOLD') 
    rospy.Subscriber("cmd_sig",light_signal,cmd_sig_control)
    rospy.spin()



if __name__ == '__main__':
    listener()
