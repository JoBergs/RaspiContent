#!/usr/bin/python
#encoding: utf-8

import time

from random import choice, random

import subprocess

from rrb3 import *

# the robotboard needs to be created as global for using the on/off button
# the parameters are 9V input voltage and 6V for the motors
robotboard = RRB3(9, 6)  

class RaspiRobot:

    def run(self):
        """ Life cycle of the RaspiRobot. """
        
        try:
            while True:
                if robotboard.sw1_closed() == True:
                    turn_off()

                print("Running...")

                distance = robotboard.get_distance()
                print("Distance: ", distance)

                if distance <= 10.0:
                    self.avert_collision()

                robotboard.forward()

                time.sleep(0.1)
        except:
            print('Quitting...')
            GPIO.cleanup()

    def avert_collision(self):
        """ Avert collision by moving backward for a second and then
        turning either left or right for maximally 1 second. """

        print('Averting collision...')

        robotboard.reverse(1)
        turn_time = random()

        if choice(['left', 'right']) == 'left':
            robotboard.left(turn_time)
        else:
            robotboard.right(turn_time)

        robotboard.forward()

def turn_off():
    """ Shutdown the Raspberry Pi """

    print("Shutting down...")

    GPIO.cleanup()
    subprocess.call(['echo posys | sudo -S poweroff'], shell=True)

if __name__ == '__main__':

    while True:
        print "Waiting for button press to start..."

        if robotboard.sw1_closed() == True:
            break

        time.sleep(0.02)

    # let the pushbutton become unpressed
    time.sleep(0.5)  

    raspirobot = RaspiRobot()
    raspirobot.run()
