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


if (len(sys.argv) != 2 and len(sys.argv) != 5):
	raise Exception('Missing parameters')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_1, GPIO.OUT) #LED1
GPIO.setup(LED_2, GPIO.OUT) #LED2
GPIO.setup(LED_3, GPIO.OUT) #LED3
GPIO.setup(LED_4, GPIO.OUT) #LED4

	
if (len(sys.argv) == 2):
	if (int(sys.argv[1]) != 0 and int(sys.argv[1]) != 1):
		raise Exception('Incorrect parameter values1')
	else:
		GPIO.output(LED_1, int(sys.argv[1]))
		GPIO.output(LED_2, int(sys.argv[1]))
		GPIO.output(LED_3, int(sys.argv[1]))
		GPIO.output(LED_4, int(sys.argv[1]))

		
else:
	for elem in sys.argv[1:]:	#The first input argument is the name of the file
		if (int(elem) != 0 and int(elem) != 1):
			raise Exception('Incorrect parameter values')

	GPIO.output(LED_1, int(sys.argv[1]))
	GPIO.output(LED_2, int(sys.argv[2]))
	GPIO.output(LED_3, int(sys.argv[3]))
	GPIO.output(LED_4, int(sys.argv[4]))

 
