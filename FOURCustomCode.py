# custom robot code for movement, object detection, and whiteboard detection
# white_lower & white_upper values to be set based on lighting conditions
import cv2
import RPi.GPIO as GPIO
import time

# Motor and ultrasonic sensor setup
LEFT_MOTOR_PIN = 17
RIGHT_MOTOR_PIN = 18
ULTRASONIC_TRIG = 23
ULTRASONIC_ECHO = 24
WHITE_LOWER = (0, 0, 200)    # Color threshold for white detection
WHITE_UPPER = (180, 20, 255)

GPIO.setmode(GPIO.BCM)
GPIO.setup(ULTRASONIC_TRIG, GPIO.OUT)
GPIO.setup(ULTRASONIC_ECHO, GPIO.IN)

# Define functions for movement
def move_forward():
    print("Moving forward")
    # Code for moving forward

def turn_left():
    print("Turning left")
    # Code for turning left

def turn_right():
    print("Turning right")
    # Code for turning right

def stop():
    print("Stopping")
    # Code for stopping

def distance():
    GPIO.output(ULTRASONIC_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(ULTRASONIC_TRIG, False)
    start = time.time()
    stop = time.time()

    while GPIO.input(ULTRASONIC_ECHO) == 0:
        start = time.time()
    while GPIO.input(ULTRASONIC_ECHO) == 1:
        stop = time.time()

    elapsed = stop - start
    dist = (elapsed * 34300) / 2
    return dist

def detect_whiteboard(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, WHITE_LOWER, WHITE_UPPER)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        area = cv2.contourArea(cnt)
        if len(approx) == 4 and area > 500:  # Checks for a square-like shape
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            return (x + w // 2, y + h // 2), frame  # Center point of whiteboard

    return None, frame

# Main program loop
cap = cv2.VideoCapture(0)  # Assumes camera is available as device 0

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect whiteboard
        whiteboard_pos, processed_frame = detect_whiteboard(frame)

        # Check for obstacles
        dist = distance()
        if dist < 30:  # Threshold distance in cm to stop
            stop()
            time.sleep(0.5)
            turn_right()  # Change direction to avoid obstacle
            continue

        if whiteboard_pos:
            # Move toward the whiteboard
            x_center = whiteboard_pos[0]
            frame_center = processed_frame.shape[1] // 2

            if abs(x_center - frame_center) < 20:
                move_forward()
            elif x_center < frame_center:
                turn_left()
            else:
                turn_right()
        else:
            # No whiteboard detected, roam or stop
            stop()

        # Display the processed frame (optional, for debugging)
        cv2.imshow("Frame", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
