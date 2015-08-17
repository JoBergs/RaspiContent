#!/usr/bin/python
#encoding: utf-8


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
