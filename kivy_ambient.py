#!/usr/bin/python
#encoding:utf-8

import kivy
kivy.require('1.9.0')

from kivy.app import App

from kivy.uix.button import Label

class Hello2App(App):
    def build(self):
        return Label()

if __name__ == '__main__':
    Hello2App().run() 


'''
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
RED , GREEN, BLUE = 11, 12, 13 
GPIO.setup([RED, GREEN, BLUE], GPIO.OUT)

def blink(color):
    GPIO.output(color, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(color, GPIO.LOW)

try:
    while True:
        # randomize
        blink(RED)
        sleep(0.5)
        blink(GREEN)
        sleep(0.5)
        blink(BLUE)
except KeyboardInterrupt:
    GPIO.cleanup()
'''