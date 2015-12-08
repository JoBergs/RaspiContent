#!/usr/bin/python
#encoding:utf-8

# Sample script for the Tutorial "Ultrasonic range detection with the Raspberry Pi" on
# http://www.knight-of-pi.org/ultrasonic-range-detection-with-the-raspberry-pi

import time
import RPi.GPIO as GPIO

from LED_display import display_number

GPIO.setmode(GPIO.BOARD)

trig = 38  # sends the signal
echo = 40  # listens for the signal

GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)

def measure_distance():
    """ Measure the distance per ultrasonic.  """

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0: pass

    start = time.time()  # reached when signal arrived

    while GPIO.input(echo) == 1:  pass

    end = time.time() # reached when signal died

    distance = ((end - start) * 34300) / 2

    return distance


if __name__ == '__main__':  

    try:
        while True:
            distance = measure_distance() 
            print("distance: ", distance, " cm, distance / 5: ", int(distance / 5))
            display_number(int(distance / 5))  # one display LED is 5 cm
            time.sleep(0.5)            
    finally:
        GPIO.cleanup()


    
    
    