#!/usr/bin/python
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/webiopi-a-simple-but-great-web-api-for-the-raspberry-pi/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import webiopi

GPIO = webiopi.GPIO

BLUE = 17 # GPIO pin using BCM numbering(BOARD 11)
RED = 18 # GPIO pin using BCM numbering(BOARD 12)
GREEN = 27 # GPIO pin using BCM numbering(BOARD 13)

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(BLUE, GPIO.OUT)
    GPIO.setFunction(RED, GPIO.OUT)
    GPIO.setFunction(GREEN, GPIO.OUT)

# loop function is repeatedly called by WebIOPi 
def loop():
    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(BLUE, GPIO.LOW)

@webiopi.macro
def shutdown_raspi():
    call(["sudo poweroff"], shell=True)

# this macro is called from the web interface, counts  and returns the
# counted value to be displayed on the website
@webiopi.macro
def count_a_lot():
    x = 0
    GPIO.digitalWrite(RED, GPIO.HIGH)

    while x < 1000000:
        x+=1

    GPIO.digitalWrite(RED, GPIO.LOW)
    GPIO.digitalWrite(GREEN, GPIO.HIGH)
    webiopi.sleep(1)
    GPIO.digitalWrite(GREEN, GPIO.LOW)

    return x 