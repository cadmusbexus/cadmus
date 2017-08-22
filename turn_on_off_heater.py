#Turn on heater 1

import os 
import sys
import RPi.GPIO as GPIO

Heater_Pin = 27 #GPIO27, tbd
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Heater_Pin, GPIO.OUT)

def turn_on_h():
	GPIO.output(Heater_Pin, GPIO.HIGH)

def turn_off_h():
	GPIO.output(Heater_Pin, GPIO.LOW)
	
	
