#!/usr/bin/python
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/raspi-ardi-big-love-pyfirmata-introduction/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import time

import pyfirmata

board = pyfirmata.Arduino('/dev/ttyUSB0')  # arduino setup

iter8 = pyfirmata.util.Iterator(board)
iter8.start()

LED = board.get_pin('d:3:p')
STEPS = 10000.0

if __name__ == '__main__':

    # increase PWM output in STEPS increments
    for i in range(int(STEPS)):
        print i
        LED.write(i / STEPS)  # hardware-PWM accepts values 0.0 ... 1.0
        time.sleep(0.001)
