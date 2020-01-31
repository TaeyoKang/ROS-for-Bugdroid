#!/usr/bin/env python

#MODULE_AUTHOR("Taeyo Kang")
#MODULE_DESCRIPTION("ROS program for Bugdroid")
#MODULE_LICENSE("BSD")
#MODULE_VERSION("1.0")

#PIGPIO library is released under the MIT License, see PIGPIO_LICENSE.txt. 

import pigpio
import rospy
import time
from std_msgs.msg import Int32

#pwm
pwm_pin = 18
led_pin = 27
pi = pigpio.pi()
led= pigpio.pi()
pi.set_mode(pwm_pin,pigpio.OUTPUT)
led.set_mode(led_pin,pigpio.OUTPUT)

rospy.init_node('pwm')
pub=rospy.Publisher('pwm_servo',Int32,queue_size=1)



count=0
led.write(led_pin,1)
pi.hardware_PWM(pwm_pin,50,90000)
time.sleep(1)

while(count < 10):
	pi.hardware_PWM(pwm_pin, 50,90000)
        pub.publish(90000)
        time.sleep(0.3)
        pi.hardware_PWM(pwm_pin, 50,72500)
        pub.publish(72500)
        time.sleep(0.3)
        pi.hardware_PWM(pwm_pin, 50,90000)
        pub.publish(90000)
        time.sleep(0.3)
        pi.hardware_PWM(pwm_pin, 50,72500)
        pub.publish(72500)
        time.sleep(1)
        count=count+1
        

led.write(led_pin,0)
pi.hardware_PWM(pwm_pin, 50,30000)

