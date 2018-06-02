#!/usr/bin/python3
#encoding:utf-8

from time import sleep
from random import randint

import unicornhathd

unicornhathd.brightness(1.0)

# iterate over x and y pixel locations
for x in range(16):
    for y in range(16):
        # color the current pixel randomly
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        unicornhathd.set_pixel(x, y, r, g, b)  
        unicornhathd.show()
        sleep(0.1)

sleep(3)
unicornhathd.clear()
unicornhathd.show()
