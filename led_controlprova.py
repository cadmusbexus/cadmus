#!/usr/bin/python

# Usage: LED_control.py led1state led2state led3state led4state
# ledXstate 0 -> turn off LED
# ledXstate 1 -> turn on LED
# If only one parameter is received, its value is assumed for all LEDs

import sys
import RPi.GPIO as GPIO

LED_1 = 12
LED_2 = 16
LED_3 = 20
LED_4 = 21
LED_5 = 26
LED_6 = 19
LED_7 = 13
LED_8 = 25


if (len(sys.argv) != 2 and len(sys.argv) != 9):
	raise Exception('Missing parameters')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_1, GPIO.OUT) #LED1
GPIO.setup(LED_2, GPIO.OUT) #LED2
GPIO.setup(LED_3, GPIO.OUT) #LED3
GPIO.setup(LED_4, GPIO.OUT) #LED4
GPIO.setup(LED_5, GPIO.OUT) #LED5
GPIO.setup(LED_6, GPIO.OUT) #LED6
GPIO.setup(LED_7, GPIO.OUT) #LED7
GPIO.setup(LED_8, GPIO.OUT) #LED8
	
if (len(sys.argv) == 2):
	if (int(sys.argv[1]) != 0 and int(sys.argv[1]) != 1):
		raise Exception('Incorrect parameter values1')
	else:
		GPIO.output(LED_1, int(sys.argv[1]))
		GPIO.output(LED_2, int(sys.argv[1]))
		GPIO.output(LED_3, int(sys.argv[1]))
		GPIO.output(LED_4, int(sys.argv[1]))
		GPIO.output(LED_5, int(sys.argv[1]))
		GPIO.output(LED_6, int(sys.argv[1]))
		GPIO.output(LED_7, int(sys.argv[1]))
		GPIO.output(LED_8, int(sys.argv[1]))
		
else:
	for elem in sys.argv[1:]:	#The first input argument is the name of the file

		if (int(elem) != 0 and int(elem) != 1):
			raise Exception('Incorrect parameter values')
			
	GPIO.output(LED_1, int(sys.argv[1]))
	GPIO.output(LED_2, int(sys.argv[2]))
	GPIO.output(LED_3, int(sys.argv[3]))
	GPIO.output(LED_4, int(sys.argv[4]))
	GPIO.output(LED_5, int(sys.argv[5]))
	GPIO.output(LED_6, int(sys.argv[6]))
	GPIO.output(LED_7, int(sys.argv[7]))
	GPIO.output(LED_8, int(sys.argv[8]))
 
