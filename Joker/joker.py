#!/usr/bin/python
#encoding: utf-8
#Tutorial: http://www.knight-of-pi.org/joker-a-raspberry-pi-joke-telling-machine-using-the-adafruit-lcd-plate/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import math
import time

import Adafruit_CharLCD as LCD

import pyjokes


class Joker:
    def __init__(self):
        self.lcd = LCD.Adafruit_CharLCDPlate()
        self.lcd.set_color(1.0, 0.0, 0.0)

    def split_joke(self, joke):      
        parts = []
        sentence = ''
        words = joke.split()

        for word in words:
            if len(sentence + word) + 1 >=16:
                # sentence becomes too long for a single line -> new sentence
                parts.append(sentence + '\n')
                sentence = word + ' '
            else:
                sentence += word + ' '
        else:
            parts.append(sentence)

        if len(parts) % 2 != 0:
            parts.append('')

        return parts

    def tell_joke(self, joke):
        parts = self.split_joke(joke)

        for (row1, row2) in zip(parts[0::2], parts[1::2]):
            self.lcd.clear()
            self.lcd.message(row1 + row2)
            time.sleep(3.0)
        
        time.sleep(3.0)
        self.lcd.clear()

    def start_joker(self):
        while True:
            joke = pyjokes.get_joke()
            self.tell_joke(joke)


if __name__ == '__main__':
    joker = Joker()
    joker.start_joker()
