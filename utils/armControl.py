import Adafruit_PCA9685
import time
pwm = Adafruit_PCA9786.PCA9685()
pwm.set_pwnfreq(50)

def pickup():
    while 1:
        
        # Initiates the arm movement to pick up the eraser
        for i in range(0,100):
            pwm.set_pwm(13, 0, (400-i))
            time.sleep(1)
                    
            pwm.set_pwm(12, 0, (300+i+i))
            time.sleep(1)
        
        # Initiates the claw to grab the eraser
        for i in range(0, 100):
            pwm.set_pwm(15, 0, (100+i))
            time.sleep(0.5)

        for i in range(0,10):
            pwm.set_pwm(15, 0, (100-i))
            time.sleep(0.5)
        
        # Initiates the arm movement back to rest
        for i in range(0, 100):
            pwm.set_pwm(13, 0, (300+i))
            time.sleep(1)
            
            pwm.set_pwm(12, 0, (500-i-i))
            time.sleep(1)            

def extend():
    while 1:
        for i in range(0, 150):
            pwm.set_pwm(12, 0, (400-i))
            time.sleep(1)
            
            pwm.set_pwm(13, 0, (300+i))
            time.sleep(1)
            
def erase():
    while 1:
        for j in range(0,3):
            for i in range(0, 35):
                pwm.set_pwm(14, 0, (300-i))
                time.sleep(0.5)

            for i in range(0, 35):
                pwm.set_pwm(14, 0, (300+i))
                time.sleep(0.5)
                
"""

claw = 0
wrist = 0
joint1 = 300
joint2 = 400

def math(servo, degree):
    
    if servo < degree:
        range = degree - servo
        
    else:
        range = servo - degree
    
    return range
"""