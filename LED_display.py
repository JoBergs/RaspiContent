#!/usr/bin/python
#encoding:utf-8

# TODO:
#   move into seperate repository
#   make a package
#   add 'permanent' option
#   make a decorator: display the(int) return value(binary, decimal, permanent, timed)
#   cleanup

# the display needs to be independent from the transmission

from time import sleep
import RPi.GPIO as GPIO

from pi_switch import RCSwitchReceiver
from time import sleep


GPIO.setmode(GPIO.BOARD)
pins = [10, 11, 15, 16, 32, 33, 35, 36]
GPIO.setup(pins, GPIO.OUT)


def convert_to_decimal(number):
    return pins[:min(number,9)]

def convert_to_binary(number):
    binary = bin(number)[-2::-1]
    print(binary)
    return [pins[i] for i in range(len(binary)) if binary[i] == '1']


def display_pins(pin_list, duration):
    GPIO.output(pin_list, GPIO.HIGH)
    if duration:
        sleep(duration)
        all_off()

def all_off():
    GPIO.output(pins, GPIO.LOW)  

# permanent should be delay interval
# if duration is False, the lights stay on until a new signal arrives
#   if duration is an float > 0, the leds will be lighted for that number of seconds
def display_number(number=5, as_binary=False, duration=False):
    all_off()
    print(number, as_binary, duration)

    pin_list = convert_to_decimal(number)

    if as_binary:
        pin_list = convert_to_binary(number)

    display_pins(pin_list, duration)


# make parameter 'permanent' which decides wheter all_off is executed after displaying

# could this be made a decorator? how do i use it in RL?

# a decorator which displays the return value?


# needs to be importable

# rethink: binary should be a flag

# keyboard interrupt -> GPIO.cleanup()

# fuse sender and receiver into one class?

if __name__ == '__main__':

    
    # self-testing code
    all_off()
    display_number(6)
    sleep(3)
    all_off()
    #display_number(7)
    #sleep(3)
    #display_number(8)
    #sleep(3)

    for i in range(9):
        display_number(i)
        sleep(0.5)

    # same effect since we sleep in the loop above
    #for i in range(9):
    #    display_number(i, duration=0.5)
    
  
    for i in range(255):
        display_number(i, True)
        sleep(0.2)

    all_off()
    


    
    
    