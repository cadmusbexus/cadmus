#data is the input from the server
data = 'False,0,1,1,1,1,1'
data.strip()
Data = data.split(',')
if Data[0] == True: #data is a command
        command = strip(data[5:])
        os.system(command)
else:   #data is an action
        for index,element in enumerate(Data[1:]):
                Data[index+1] = int(element)
        print(Data)
        if Data[1] == 0:
                syst = 'main'   #action on main system
        else: 
                syst = 'aux'    #action on auxiliary system
if syst == 'main':
        if Data[2] == 0: #Camera action
                camera_state = Data[3] #Camera either on (1) or off (0)
        elif Data[2] == 1: #LEDs action
                led1, led2, led3, led4 = Data[3:]
                #os.system('python led_controlprovisional.py '+ led1 + ' ' + led2 + ' ' + led3  + ' ' +led4 + ' 1 1 1 1')
        elif Data[2] == 2: #Heaters action
                h_mode, h_sate = Data[3:]
else:
        if Data[2] == 1: #LEDs action
                led1, led2, led3, led4 = Data[3:]
        elif Data[2] == 2: #Heaters action
                h_mode, h_sate = Data[3:]


