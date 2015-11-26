#!/usr/bin/python
#encoding:utf-8

import sys

from time import sleep
from random import randint

from RPi.GPIO import cleanup

from pi_switch import RCSwitchReceiver, RCSwitchSender

from LED_display import display_number


def run_sender():
    sender = RCSwitchSender()
    sender.enableTransmit(0) # use WiringPi pin 0
    num = 1

    while True:
        print 'Sending: ' + str(num)
        sleep(1)
        sender.sendDecimal(num, 24)
        num += 1   

def run_receiver():
    receiver = RCSwitchReceiver()
    receiver.enableReceive(2)

    while True:
        print 'Listening...'
        sleep(0.1)

        if receiver.available():
            #print 'yes'
            received_value = receiver.getReceivedValue()

            if received_value:
                display_number(received_value % 256, True)

                print("Value: %s | Bit: %s | Protocol: %s" % (received_value,
                        receiver.getReceivedBitlength(),
                        receiver.getReceivedProtocol()))

            receiver.resetAvailable()  


if __name__ == '__main__':

    try:
        # HACKish: "sender" as last parameter - be a sender; be a receiver else
        if sys.argv[-1] == "sender":
            run_sender()
        else:
            run_receiver() 
    finally:
        cleanup()
    
    