#!/usr/bin/python
#Retruns the temperatures of top and bottom of the cloud chamber, and both cameras'.
import os
import glob
import time

import sys
import RPi.GPIO as GPIO

HEATER_PIN = 26
CC_TEMPMAX = 0 # TBD
CC_THRESHOLD = 0 # TBD
     
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
     
base_dir = '/sys/bus/w1/devices/'
device_folder_0 = glob.glob(base_dir + '28*')[0] #'0' set for the sensor placed on the top of the chamber, IT MAY CHANGE
device_folder_1 = glob.glob(base_dir + '28*')[1] #'1' set for the sensor placed on the bottom of the chamber, IT MAY CHANGE
device_folder_2 = glob.glob(base_dir + '28*')[2] #'2' set for the sensor placed at the camera, IT MAY CHANGE

device_file_0 = device_folder_0 + '/w1_slave'
device_file_1 = device_folder_1 + '/w1_slave'
device_file_2 = device_folder_2 + '/w1_slave'

def read_temp_raw():
    f0 = open(device_file_0, 'r')
    f1 = open(device_file_1, 'r')
    f2 = open(device_file_2, 'r')
    lines0 = f0.readlines()
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    f0.close()
    f1.close()
    f2.close()
    return lines0. lines1, lines2
     
def top_temp():
    lines[0] = read_temp_raw()
    while (lines[0][0].strip()[-3:] != 'YES'):
        time.sleep(0.2)
        lines[0] = read_temp_raw()
    equals_pos = lines[0][1].find('t=')
    if (equals_pos != -1):
        temp_string = lines[0][1][equals_pos+2:]
        temp_top = float(temp_string) / 1000
        return temp_top

def low_temp():
    lines[1] = read_temp_raw()
    while (lines[1][0].strip()[-3:] != 'YES'):
        time.sleep(0.2)
        lines[1] = read_temp_raw()
    equals_pos = lines[1][1].find('t=')
    if (equals_pos != -1):
        temp_string = lines[1][1][equals_pos+2:]
        temp_low = float(temp_string) / 1000
        return temp_low

def cam_temp():
    lines[2] = read_temp_raw()
    while (lines[2][0].strip()[-3:] != 'YES'):
        time.sleep(0.2)
        lines[2] = read_temp_raw()
    equals_pos = lines[2][1].find('t=')
    if (equals_pos != -1):
        temp_string = lines[2][1][equals_pos+2:]
        temp_cam = float(temp_string) / 1000
        return temp_cam


#sensor 1 is top cloud chamber's sensor
#sensor 2 is low cloud chamber's sensor
#sensor 3 is the sensor of the camera
def temp(sensor_number): #sensor_number equals 1 for sensor 1, 2 for sensor 2, 3 for sensor 3.
	t1 = top_temp()
	t2 = low_temp()
	t3 = cam_temp()
	templist = [t1,t2,t3]
	return templist[sensor_number -1]
