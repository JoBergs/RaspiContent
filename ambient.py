#!/usr/bin/python
#encoding:utf-8

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.slider import Slider
from kivy.uix.button import Label

kv = '''
BoxLayout:
    orientation: 'vertical'
    Label:
        text: 'Hello World!' 
    Label:
        text: 'Bla' 
'''



class AmbientApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    AmbientApp().run() 


'''
    bass_slider = Slider(orientation='vertical', size_hint=(None, .92), 
                                        min=0, max=100, value=50, step=1)  

    GPIO.setup(self.pinForward, GPIO.OUT)
    GPIO.setup(self.pinBackward, GPIO.OUT)
    GPIO.setup(self.pinControl, GPIO.OUT)
    self.pwm_forward = GPIO.PWM(self.pinForward, 100)
    self.pwm_backward = GPIO.PWM(self.pinBackward, 100)
    self.pwm_forward.start(0)
    self.pwm_backward.start(0)
    self.pwm_forward.ChangeDutyCycle(speed) 

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