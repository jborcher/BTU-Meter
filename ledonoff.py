#/Desktop/Python
#this propgram turns two leds on and off

import RPi.GPIO as GPIO		#imports GPIO Module
import time
GPIO.setmode (GPIO.BCM) 	#sets the mode to represent the preferred pin numbering scheme
#GPIO.cleanup ()  		#resets all channels back to inputs
GPIO.setwarnings (False)  	#turns off annoying warnings, can make 'True' for debugging
GPIO.setup (17, GPIO.OUT)	#sets GPIO17 to output (pin 11)
GPIO.setup (27, GPIO.OUT)	#sets GPIO27 to output (pin 13)
for x in range(0,3):
	print "Red on"				
	GPIO.output (17, GPIO.LOW)	#Turn LEDs 'on'
	GPIO.output (27, GPIO.HIGH)
	time.sleep(1)
	print "Blue on"
	GPIO.output (17, GPIO.HIGH)
	GPIO.output (27, GPIO.LOW)
	time.sleep(1)
GPIO.cleanup ()           	#resets all channels back to inputs
