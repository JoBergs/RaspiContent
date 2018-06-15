import os
import time

import RPi.GPIO as GPIO

# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up the pin numbers we are using for each LED
# pin number
# LED_PIN=int(os.environ['LED_PIN'])
LED_PIN = 11

# Environment variables are a way to pass distinct data to nodes for initialisation ect.

# Set Pin 11, 16 and 7 on the GPIO header to act as an output
GPIO.setup(LED_PIN,GPIO.OUT)

# This loop runs forever and handles the LED
while True:
    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN,GPIO.LOW)
    time.sleep(1)
