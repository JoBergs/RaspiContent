#!/usr/bin/python
#encoding:utf-8


# naaaah: just try importing the required functions, but make the script multipurpose!

# needs to be classbased

# TODO:
#   move into seperate repository
#   make a package
#   add 'permanent' option
#   make a decorator: display the(int) return value(binary, decimal, permanent, timed)
#   cleanup

# the display needs to be independent from the transmission

from time import sleep
from random import randint

from RPi.GPIO import cleanup

from pi_switch import RCSwitchReceiver

from LED_display import display_number


'''
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
'''


# make parameter 'permanent' which decides wheter all_off is executed after displaying

# could this be made a decorator? how do i use it in RL?

# a decorator which displays the return value?


# needs to be importable

# rethink: binary should be a flag

# keyboard interrupt -> GPIO.cleanup()

# fuse sender and receiver into one class?

# This is the sender script:
'''
# Type B example: address group = 1, channel = 1
import pi_switch
from time import sleep
sender = pi_switch.RCSwitchSender()
sender.enableTransmit(0) # use WiringPi pin 0
num = 1
while True:
    print 'sending'
    sleep(2)
    sender.sendDecimal(num, 24)
    num += 1
    print(num)
    #sender.send('00010111')
    #sleep()
#sender.send("000101010001010101010101") # switch on
#sender.send("000101010001010101010100") # switch off
'''

if __name__ == '__main__':

    receiver = RCSwitchReceiver()
    receiver.enableReceive(2)

    num = 0

    try:
        while True:
            #display_number(randint(0, 100), True, 0.2)
            print 'Listening...'
            sleep(0.5)
            if receiver.available():
                received_value = receiver.getReceivedValue()
                if received_value:
                    num += 1
                    #print("Received[%s]:" % num)
                    # needs a % 256
                    display_number(received_value % 256, True)
                    # cleanup below
                    print("Value: %s | Bit: %s | Protocol: %s" % (received_value,
                            receiver.getReceivedBitlength(),
                            receiver.getReceivedProtocol()))
                    #print("Protocol: %s\n" % receiver.getReceivedProtocol())

                receiver.resetAvailable()   
    finally:
        cleanup()
    
    