#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
from sensor_msgs.msg import Joy

def callback(msg):
    led_onoff(16, msg.buttons[0] == 1) # left

    led_onoff(20, msg.buttons[1] == 1) #foward

    led_onoff(21, msg.buttons[2] == 1) #right

    led_onoff(4, msg.buttons[0] == 1)

def led_onoff(pin_number, is_high):
    if is_high:
        GPIO.output(pin_number, GPIO.HIGH)
    else:
        GPIO.output(pin_number, GPIO.LOW)

def listener():
    rospy.init_node('subscriber')
    setup_GPIO()
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()



def setup_GPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT) 
    GPIO.setup(21, GPIO.OUT)


if __name__ == '__main__':
    listener()
