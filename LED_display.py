#!/usr/bin/python
#encoding:utf-8

# Sample script for the Tutorial "Building a simple LED display" on
# http://www.knight-of-pi.org/building-a-simple-led-display/

from time import sleep
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
pins = [10, 11, 15, 16, 32, 33, 35, 36]
GPIO.setup(pins, GPIO.OUT)


def all_off():
    GPIO.output(pins, GPIO.LOW)  

def get_binary_pins(number):
    """ Convert a decimal number into a list of pins fitting its binary
         representation. """

    binary = bin(number)[2:][::-1]

    return [pins[i] for i in range(len(binary)) if binary[i] == '1']

def display_pins(pin_list, duration):
    """ Trigger all pins in pin_list on for duration seconds. """

    all_off()
    GPIO.output(pin_list, GPIO.HIGH)
    sleep(duration)
    all_off()

def display_number(number=5, as_binary=False, duration=0.2):
    """ Wrapper for displaying either a binary or a decimal number. """

    # the first n, n < 9 pins directly represent decimal numbers  
    pin_list = pins[:min(number,8)]

    if as_binary:
        pin_list = get_binary_pins(min(number, 255))

    display_pins(pin_list, duration)


if __name__ == '__main__':

    # test code
    try:
        for i in range(9):
            display_number(i, duration=0.5)

        for i in range(255):
            display_number(i, True)

    finally:
        GPIO.cleanup()


    
    
    