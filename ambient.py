#!/usr/bin/python
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/kivy-on-a-raspberry-pi-control-light-color-with-a-touch-interface/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

from time import sleep

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.slider import Slider
from kivy.uix.button import Label

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

RED , GREEN, BLUE = 11, 12, 13 # BOARD numbering
GPIO.setup([RED, GREEN, BLUE], GPIO.OUT)

# setup sofware pulse width modulation - pwm
red_pwm = GPIO.PWM(RED, 100)
green_pwm = GPIO.PWM(GREEN, 100)
blue_pwm = GPIO.PWM(BLUE, 100)

# start duty cycle with the same value as the sliders
red_pwm.start(50)
green_pwm.start(50)
blue_pwm.start(50)

kv = '''
BoxLayout:
    orientation: 'vertical'
    MySlider:
        mycolor: 'red'
        on_value: self.set_color(*args)
    MySlider:
        mycolor: 'green'
        on_value: self.set_color(*args)
    MySlider:
        mycolor: 'blue'
        on_value: self.set_color(*args)
        
'''

class MySlider(Slider):
    def __init__(self, **kwargs):
        kwargs['min'] = 0
        kwargs['max'] = 100
        kwargs['value'] = 50
        super (MySlider, self).__init__(**kwargs)    

    def set_color(self, instance, value):
        if self.mycolor == 'red':
            red_pwm.ChangeDutyCycle(int(value))
        elif self.mycolor == 'green':
            green_pwm.ChangeDutyCycle(int(value))
        elif self.mycolor == 'blue':
            blue_pwm.ChangeDutyCycle(int(value))

class AmbientApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    try:
        AmbientApp().run() 
    except KeyboardInterrupt:
        GPIO.cleanup()
