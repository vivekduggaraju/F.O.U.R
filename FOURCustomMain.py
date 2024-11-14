** 
Mekhel
This code integrates `FOURCustomCode.py` into `main.py` for handling movement, obstacle avoidance, and whiteboard detection. This allows `main.py` to use modularized code from `FOURCustomCode.py`, enhancing readability and organization.
**

from utils.armControl import *
from utils.basicMovement import *
import cv2
import time

# Include custom movement and detection code
from FOURCustomCode import move_forward, turn_left, turn_right, stop, distance, detect_whiteboard

# Constants for detection and buffers
min_distance = 10
buffer1 = 30
buffer2 = 15

def main():
    pickup()  # Prepare the arm or other necessary actions

    cap = cv2.VideoCapture(0)  # Initialize camera capture

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Check for whiteboard detection
            whiteboard_pos, processed_frame = detect_whiteboard(frame)
            dist = distance()  # Check obstacle distance

            if dist < min_distance:
                move_backward(0.5)
                time.sleep(1)
            elif dist < buffer2:
                move_forward(0.25)
                time.sleep(1)
            elif dist < buffer1:
                move_forward(0.5)
                time.sleep(1)
            else:
                move_forward(1)
                time.sleep(1)

            # Whiteboard navigation
            if whiteboard_pos:
                x_center = whiteboard_pos[0]
                frame_center = processed_frame.shape[1] // 2

                if abs(x_center - frame_center) < 20:
                    move_forward()
                elif x_center < frame_center:
                    turn_left()
                else:
                    turn_right()

                # Start cleaning when close to the board
                if dist <= min_distance:
                    stop()
                    erase_board()
                    break

            cv2.imshow("Frame", processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
        GPIO.cleanup()

def erase_board():
    extend()
    erase()
    for i in range(3):
        repo_right(1)
        erase()
    repo_left(3)
    for j in range(3):
        repo_left(1)
        erase()
    repo_right(3)
