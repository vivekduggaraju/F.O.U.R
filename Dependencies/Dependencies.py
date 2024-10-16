# Dependencies and initialize
import time
import RPi.GPIO as GPIO
import json
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

Tr = 11 #Pin No. of Ultrasonic Module Input
Ec = 8 # Pin number of the output end of the ultrasonic module
servoPort = 1 #The number of the servo that controls the horizontal rotation of the ultrasonic module
servoMiddle = 330 #The middle position of the servo
servoLeft = 180 #Left position of the servo
servoRight = 480 #The right position of the servo
rangeKeep = 0.3 #Avoidance distance

scanDir = 1 #Scan direction, 1 is from left to right, -1 is from right to left
scanPos = 1 #Store the current scan position (1 is the left, 2 is the middle, and 3 is the right)
scanNum = 3 #The number of scan positions (left, middle, and right, these are three positions)

scanList = [0,0,0] #Save scan results

GPIO.setmode(GPIO.BCM)
GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Ec, GPIO.IN)