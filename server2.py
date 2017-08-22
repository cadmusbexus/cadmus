#!/usr/bin/env python

import socket
import string
import os
import read_config as rc
import subprocess, signal

TCP_IP = ''
TCP_PORT = 5015
BUFFER_SIZE = 1000

while 1:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)

	conn, addr = s.accept()
	print 'Connection address:', addr
	while 1:
		data = conn.recv(BUFFER_SIZE)
    		conn.close()
		s.close()    	

		data_1 = data.strip()
		Data_1 = data_1.split(',')
		Data = []
		for i in Data_1:
			Data.append(int(i))

		if str(Data[0]) == "True": #data is a command
			command = data[5:].strip()
			os.system(command)
		else:
			if (Data[0]) == 0:
				syst = 'main'
			else: 
				syst = 'aux'

			if syst == 'main':
				if (Data[1]) == 0: #Camera action
					camera_state = (Data[2]) #Camera either on (1) or off (0)
					rc.camera_setauto(camera_state)
					
					p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
					out, err = p.communicate()	
							
					if (camera_state == 0):
						
						for line in out.splitlines():
							if "canon_capture.py" in line:
								pid = int((line.split(None, 1)[1]).split()[0])
								os.kill(pid, signal.SIGKILL)
								
					else:
						
						exists = False
						for line in out.splitlines():
							if 'canon_capture.py' in line:
								exists = True
						
						if exists == False:
							os.system('nohup python3 canon_capture.py &')
				
				elif (Data[1]) == 1: #LEDs action
					led1, led2, led3, led4 = (Data[2:])
					os.system('nohup python led_control.py'+' '+str(led1)+' '+str(led2)+' '+str(led3)+' '+str(led4)+' &')
					
				elif (Data[1]) == 2: #Heaters action
					h_mode, h_state = (Data[2:])
					rc.heater_setauto(h_mode)
					
					p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
					out, err = p.communicate()	
							
					if (h_state == 0):
						
						for line in out.splitlines():
							if 'thermal_control.py' in line:
								pid = int((line.split(None, 1)[1]).split()[0])
								os.kill(pid, signal.SIGKILL)
								
					else:
						
						exists = False
						for line in out.splitlines():
							if 'thermal_control.py' in line:
								exists = True
						
						if exists == False:
							os.system('nohup python thermal_control.py &')
					
			
				# Send command through UART to auxiliary computer
				# (auxiliary computer processes command, we do not care here)
    	
		print "received data:",data
		conn.close()
		s.close()
		if data: break
