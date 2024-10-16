# Requires rpi.gpio
# Requires picamera
# Requires the initial motor settings program to run first

import RPi.GPIO as GPIO
import time
from math import *

# Define the GPIO pins for the motors
MOTOR_A_PIN1 = 17  # Motor A IN1
MOTOR_A_PIN2 = 27  # Motor A IN2
MOTOR_B_PIN1 = 22  # Motor B IN3
MOTOR_B_PIN2 = 23  # Motor B IN4

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up the motor pins as output
GPIO.setup(MOTOR_A_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_A_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_B_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_B_PIN2, GPIO.OUT)

def stop():
    """Stop all motors."""
    GPIO.output(MOTOR_A_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_A_PIN2, GPIO.LOW)
    GPIO.output(MOTOR_B_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_B_PIN2, GPIO.LOW)

def move_forward(duration):
    """Move the tank forward for the specified duration."""
    GPIO.output(MOTOR_A_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_A_PIN2, GPIO.LOW)
    GPIO.output(MOTOR_B_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_B_PIN2, GPIO.LOW)
    time.sleep(duration)
    stop()

def move_backward(duration):
    """Move the tank backward for the specified duration."""
    GPIO.output(MOTOR_A_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_A_PIN2, GPIO.HIGH)
    GPIO.output(MOTOR_B_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_B_PIN2, GPIO.HIGH)
    time.sleep(duration)
    stop()

def turn_left(duration):
    """Turn the tank left for the specified duration."""
    GPIO.output(MOTOR_A_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_A_PIN2, GPIO.HIGH)
    GPIO.output(MOTOR_B_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_B_PIN2, GPIO.LOW)
    time.sleep(duration)
    stop()

def turn_right(duration):
    """Turn the tank right for the specified duration."""
    GPIO.output(MOTOR_A_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_A_PIN2, GPIO.LOW)
    GPIO.output(MOTOR_B_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_B_PIN2, GPIO.HIGH)
    time.sleep(duration)
    stop()

def repo_left(spaces):
    turn_right(0.25)
    move_backward(sqrt(2)*spaces*0.25)
    turn_left(0.25)
    move_forward(spaces*(0.25))

def repo_right(spaces):
    turn_left(0.25)
    move_backward(sqrt(2)*spaces*0.25)
    turn_right(0.25)
    move_forward(spaces*(0.25))



# Main loop to test the functions
try:
    while True:
        print("Moving forward")
        move_forward(2)  # Move forward for 2 seconds
        time.sleep(1)
        
        print("Turning left")
        turn_left(1)  # Turn left for 1 second
        time.sleep(1)
        
        print("Moving backward")
        move_backward(2)  # Move backward for 2 seconds
        time.sleep(1)
        
        print("Turning right")
        turn_right(1)  # Turn right for 1 second
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Stopping the tank")
    stop()
    GPIO.cleanup()  # Reset the GPIO pins on exit
