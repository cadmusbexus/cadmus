import ast
import os.path

def write_file(config):
    config_file = open("config.txt", "w")
    config_file.write(str(config))
    config_file.close()

def read_file():
    if (not os.path.isfile("config.txt")):
        auto = {"camera": 1, "heater": 1}
        write_file(auto)

    config_file = open("config.txt", "r")
    auto = config_file.read()
    print auto
    auto_dict = ast.literal_eval(auto)
    config_file.close()

    return auto_dict


def camera_isauto():
    myfile = read_file()
    return myfile.camera

def heater_isauto():
    myfile = read_file()
    return myfile.heater

def camera_setauto(status):
    myfile = read_file()
    myfile["camera"] = status
    write_file(myfile)

def heater_setauto(status):
    myfile = read_file()
    myfile["heater"] = status
    write_file(myfile)
