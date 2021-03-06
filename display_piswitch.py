#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/using-pi-switch-for-easy-wireless-data-transmission-with-a-raspberry-pi/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import sys

from time import sleep
from random import randint

from RPi.GPIO import cleanup

from pi_switch import RCSwitchReceiver, RCSwitchSender

# needs to be in the same directory(me lazy)
from LED_display import display_number


def run_sender():
    """ Setup the Raspberry Pi as 433Mhz wifi sender and transmit a number 
         which is increased by one in every iteration. """

    sender = RCSwitchSender()
    sender.enableTransmit(0) # use WiringPi pin 0
    num = 1

    while True:
        print 'Sending: ' + str(num)
        sleep(1)
        sender.sendDecimal(num, 24)
        num += 1   

def run_receiver():
    """ Setup the Raspberry Pi as receiver, listen for transmitted values,
         display every received number as binary < 256 if the display is attached.
         Prints the received value, bit length and protocol to the terminal. """

    receiver = RCSwitchReceiver()
    receiver.enableReceive(2)

    while True:
        print 'Listening...'
        sleep(0.5)

        if receiver.available():
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
    
    