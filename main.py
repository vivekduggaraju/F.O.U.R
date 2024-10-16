from utils.armControl import *
from utils.basicMovement import *
import RPi.GPIO as GPIO
import time

min_distance=10
sleep= time.sleep(1)
buffer1= 30
buffer2=15

def main():
    pickup()

    while True:
        distance= checkdist()
        if distance > buffer1:
            move_forward(1)
            sleep
        
        elif distance< buffer1 and distance> buffer2:
            move_forward(0.5)
            sleep

        elif distance< buffer2 and distance> min_distance:
            move_forward(0.25)
            sleep      

        elif distance < min_distance:
            move_backward(0.5)
            sleep

        else:
            stop()
            erase_board()
            break

def erase_board():
    
    extend()
    erase()
    for i in range(0,3):
        repo_right(1)
        erase()
    repo_left(3)
    for j in range(0,3):
        repo_left(1)
        erase()
    repo_right(3)
        

             

