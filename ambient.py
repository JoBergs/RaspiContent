#!/usr/bin/python
#encoding:utf-8

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.button import Label

kv = '''
<Label>:
    text: 'Hello World!' 
'''

Builder.load_string(kv)

class AmbientApp(App):
    def build(self):
        return Label()

if __name__ == '__main__':
    AmbientApp().run() 


'''
    GPIO.setup(self.pinForward, GPIO.OUT)
    GPIO.setup(self.pinBackward, GPIO.OUT)
    GPIO.setup(self.pinControl, GPIO.OUT)

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