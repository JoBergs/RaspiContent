#!/usr/bin/python
#encoding:utf-8

import sys

from time import sleep
from random import randint

from RPi.GPIO import cleanup

from pi_switch import RCSwitchReceiver

from LED_display import display_number


def run_sender():
    sender = pi_switch.RCSwitchSender()
    sender.enableTransmit(0) # use WiringPi pin 0
    num = 1
    while True:
        print 'sending'
        sleep(1)
        sender.sendDecimal(num, 24)
        num += 1
        print(num)

def run_receiver():
    while True:
        display_number(randint(0, 100), True, 0.2)
        print 'Listening...'
        sleep(1)
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


if __name__ == '__main__':

    receiver = RCSwitchReceiver()
    receiver.enableReceive(2)

    num = 0

    try:
        # HACKish: anything besides "sender" being the last parameter
        #                creates a receiver
        if sys.argv[-1] == "sender":
            run_sender()
        else:
            run_receiver() 
    finally:
        cleanup()
    
    