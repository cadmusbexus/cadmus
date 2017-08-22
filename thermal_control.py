#!/usr/bin/python
# Cloud chamber's thermal control code for the principal computer.

import os
import glob
import time

import sys
import RPi.GPIO as GPIO
import read_config
from read_config import 

HEATER_PIN = 27 #GPIO TBD
CC_TEMPMAX = 0 #Maximum temperature cloud chamber top TBD
CC_THRESHOLD = 0 #Thresold temperature cloud chamber top TBD

os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0] #'0' set for the #sensor placed on the top of the chamber, IT MAY CHANGE
device_file = device_folder + '/w1_slave'
     
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while (lines[0].strip()[-3:] != 'YES'):
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if (equals_pos != -1):
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000
        return temp_c

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(HEATER_PIN, GPIO.OUT) #HEATER

h_mode = 1
while (True):
	import functions
	time.sleep(1)
	if h_mode == 1: 	#automatic mode
		time.sleep(3)
		cc_top_temp = read_temp()
		if (cc_top_temp > CC_TEMPMAX):
			GPIO.output(HEATER_PIN, GPIO.LOW)
		elif (cc_top_temp <= CC_THRESHOLD):
			GPIO.output(HEATER_PIN, GPIO.HIGH)
	else:
		GPIO.output(HEATER_PIN, h_state) 

