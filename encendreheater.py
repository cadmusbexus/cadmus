import RPi.GPIO as GPIO

HEATER_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(HEATER_PIN, GPIO.OUT)

GPIO.output(HEATER_PIN, GPIO.LOW)