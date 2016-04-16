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
