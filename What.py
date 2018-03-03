#!/usr/bin/python
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/raspberry-pi-and-jasper-a-custom-voice-command-for-measuring-the-distance
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

# This is a Python Script which could be imported by Jasper as voice command
# on a Raspberry Pi. For fun, an ultrasonic sensor was added. If Jasper is running
# and hears the command 'What', the distance to the ultrasonic sensor is measured
# and Jasper tells the result.
# For Raspbian pre Jessie, PiGPIO (Website: http://abyz.co.uk/rpi/pigpio/)
# needs to be installed & started for sudoless GPIO access.

import re, time

import pigpio

WORDS = ["WHAT"]

pi = pigpio.pi()

trig = 20  # sends the signal
echo = 21  # listens for the signal

pi.set_mode( trig, pigpio.OUTPUT)
pi.set_mode( echo, pigpio.INPUT)

def measure_distance():
    """ Measure the distance per ultrasonic.  """

    pi.write(trig, 1)
    time.sleep(0.00001)
    pi.write(trig, 0)

    while pi.read(echo) == 0: pass

    start = time.time()  # reached when signal arrived

    while pi.read(echo) == 1:  pass

    end = time.time() # reached when signal died

    distance = ((end - start) * 34300) / 2

    return distance

def handle(text, mic, profile):
    """
        Reports the current distance as measured with ultrasonic.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    
    distance = measure_distance()
    mic.say("The distance is " + str(round(distance, 1)) + " centimeters.")


def isValid(text):
    """
        Returns True if input is What, as in 'What distance is that?'.

        Arguments:
        text -- user-input, typically transcribed speech
    """

    return bool(re.search(r'\bwhat\b', text, re.IGNORECASE))
