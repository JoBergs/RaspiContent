#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/painting-colors-with-the-skywriter-gesture-sensor-and-the-unicornhat
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import signal

import skywriter
import unicornhathd

unicornhathd.brightness(1.0)

@skywriter.move()
def move(x, y, z):
    for i in range(16):
        for j in range(16):
            unicornhathd.set_pixel(i, j, int(x*255), int(y*255), int(z*255))   
    unicornhathd.show()    

signal.pause()
