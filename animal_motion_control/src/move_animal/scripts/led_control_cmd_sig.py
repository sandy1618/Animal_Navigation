#!/usr/bin/env python
#include <light_signal_msg/light_signal.h>
import rospy
import RPi.GPIO as GPIO
from sensor_msgs.msg import Joy
from light_signal_msg.msg import light_signal

def cmd_sig_test(msg):
    if msg.left == 1 :
        rospy.loginfo("Move left")
    if msg.forward == 1 :
        rospy.loginfo("Move forward")
    if msg.right == 1 :
        rospy.loginfo("Move right")

def joy_test(msg):
    if msg.buttons[0] == 1  :
        rospy.loginfo("Move left")
    if msg.buttons[1] == 1 :
        rospy.loginfo("Move forward")
    if msg.buttons[3] == 1 :
        rospy.loginfo("Move right")


def cmd_sig_control(msg):
    led_onoff(16, msg.left == 1) # left

    led_onoff(20, msg.forward == 1) #foward

    led_onoff(21, msg.right == 1) #right

    led_onoff(4, msg.buttons[0] == 1)

def joy_control(msg):
    led_onoff(16, msg.buttons[0] == 1) # left

    led_onoff(20, msg.buttons[1] == 1) #foward

    led_onoff(21, msg.buttons[2] == 1) #right

    led_onoff(4, msg.buttons[0] == 1)


def led_onoff(pin_number, is_high):
    if is_high:
        GPIO.output(pin_number, GPIO.HIGH)
    else:
        GPIO.output(pin_number, GPIO.LOW)




def setup_GPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT) 
    GPIO.setup(21, GPIO.OUT)

def listener():
    rospy.init_node('led_control_cmd_sig')
    # setup_GPIO()
    # rospy.Subscriber("joy", Joy, callback)
      rospy.Subscriber("cmd_sig",light_signal,cmd_sig_control)
    # rospy.Subscriber("cmd_sig",light_signal,cmd_sig_test)
    # rospy.Subscriber("joy", Joy, joy_test)
    rospy.spin()

if __name__ == '__main__':
    listener()
