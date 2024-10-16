import RPi.GPIO as GPIO
import time

Tr = 11  # The pin number of the input end of the ultrasonic module
Ec = 8   # Pin number of the output end of the ultrasonic module

GPIO.setmode(GPIO.BCM)
GPIO.setup(Tr, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Ec, GPIO.IN)

def checkdist():
    GPIO.output(Tr, GPIO.HIGH)  # Set the input terminal of the module to high level and send out an initial sound wave
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)

    while not GPIO.input(Ec):  # Wait until the module receives the initial sound wave
        pass
    t1 = time.time()  # Record the time when the initial sound wave is emitted

    while GPIO.input(Ec):  # Wait until the return sound wave is detected
        pass
    t2 = time.time()  # Record the time when the return sound wave is captured

    return round((t2 - t1) * 340 / 2, 2)  # Calculate the distance
