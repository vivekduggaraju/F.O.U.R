import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG_PIN = 23
ECHO_PIN = 24

# Set up the trigger and echo pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    """Measures distance using the HC-SR04 ultrasonic sensor."""
    # Ensure the trigger pin is low
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(2)  # Wait for the sensor to settle
    
    # Send a 10µs pulse to trigger the measurement
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)  # 10µs pulse
    GPIO.output(TRIG_PIN, GPIO.LOW)
    
    # Wait for the echo response
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()  # Record start time
    
    while GPIO.input(ECHO_PIN) == 1:
        end_time = time.time()  # Record end time
    
    # Calculate time difference (pulse duration)
    pulse_duration = end_time - start_time
    
    # Speed of sound is 34300 cm/s, so calculate distance
    distance = pulse_duration * 34300 / 2  # Divide by 2 to account for the round trip
    
    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(1)
finally:
    GPIO.cleanup()
