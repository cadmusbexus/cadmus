#!/usr/bin/env python

import socket
import psutil
import time
import numpy as np
from time import sleep

#from scipy import misc
#photo = misc.imread('Test_030817/IMG_7635.JPG')
    
while True:

    data = open(r'Test_030817/cat.png').read()
    
    unix_time = int(time.time())
    disk_usage = psutil.disk_usage('/').percent
    cpu_usage = psutil.cpu_percent(interval=1)
    uptime = int(time.time())-int(psutil.boot_time())

    TCP_IP = '169.254.75.68'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    MESSAGE = ''+str(unix_time)+','+str(uptime)+','+str(cpu_usage)+','+str(disk_usage)

    # Send the technical data
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    s.close()
    print "Technical data sent"

    # Send the scientific data
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(data)
    s.close()
    print "Scientific data sent"

    sleep(2)
