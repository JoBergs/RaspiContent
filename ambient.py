#!/usr/bin/python
#encoding:utf-8

from time import sleep

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.button import Label

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

RED , GREEN, BLUE = 11, 12, 13 
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
MyLayout:
    orientation: 'vertical'
    redslider: _redslider
    greenslider: _greenslider
    blueslider: _blueslider
    MySlider:
        id: _redslider
        mycolor: 'red'
        on_value: self.set_color(*args)
    MySlider:
        id: _greenslider
        mycolor: 'green'
        on_value: self.set_color(*args)
    MySlider:
        id: _blueslider
        mycolor: 'blue'
        on_value: self.set_color(*args)
    Button:
        text: 'Test'
        size_hint: .2, .2
        pos_hint: {'center_x':.5,'center_y':.5}
        on_press: root.test_func(*args)
        
'''

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super (MyLayout, self).__init__(**kwargs)

    def test_func(self, instance):
        blink(RED)

def blink(color):
    GPIO.output(color, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(color, GPIO.LOW)

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
