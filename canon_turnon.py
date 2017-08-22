#!/usr/bin/python
# Turns on conversor connected to camera. Turns it off if temperture is too high
#and turns it back on if temperature lowers enough.

#Importing packages
import os
import glob
import time
import sys
import RPi.GPIO as GPIO

CONVERSOR_PIN = 36 #TBD - Could be 16
CAM_TEMP_MAX = 0 # TBD - Temp. camera is turned off
CAM_TEMP_RESTART = 0 # TBD - Temp. camera is turned back on
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(CONVERSOR_PIN, GPIO.OUT)     #Conversor connected to camera

while True:
	import read_config
	sleep(1)
	if camera_isauto() == 1:
		GPIO.output(CONVERSOR_PIN, GPIO.HIGH)   #Turns conversor on
		camera = 'ON'
		os.system('modprobe w1-gpio')
		os.system('modprobe w1-therm')
			 
		base_dir = '/sys/bus/w1/devices/'
		device_folder = glob.glob(base_dir + '28*')[1] #'1' set for the #sensor placed at the camera, IT MAY CHANGE
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


		while camera_isauto() == 1:
			if camera == 'ON':
				time.sleep(5)   #Time TBD
				cam_temp = read_temp()
				if (cam_temp >= CAM_TEMP_MAX):
					GPIO.output(CONVERSOR_PIN, GPIO.LOW)    #Conversor turned off
					camera = 'OFF'

			elif camera == 'OFF':
				time.sleep(10) #Time TBD
				cam_temp = read_temp()
					if (cam_temp <= CAM_TEMP_RESTART):
						GPIO.output(CONVERSOR_PIN, GPIO.HIGH)   #Conversor turned back on
						camera = 'ON'

	else: 
		GPIO.output(CONVERSOR_PIN, GPIO.LOW)   #Turns conversor off
		camera = 'OFF'

