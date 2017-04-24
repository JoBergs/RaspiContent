# This is the code for a Raspberry Pi RGB color mixer for LED strips.
# Checkout the tutorial at
# http://www.knight-of-pi.org/color-mixer-control-a-rgb-led-strip-with-the-raspberry-pi-and-the-n-channel-mosfet-irlb8721/
# kop

#!/usr/bin/python
#encoding:utf-8

from random import choice, randint

from time import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

RED_PIN , GREEN_PIN, BLUE_PIN = 11, 12, 13 # BOARD numbering
GPIO.setup([RED_PIN, GREEN_PIN, BLUE_PIN], GPIO.OUT)

# TODO
#   implement color as property that receives values (0.0, 0.0, 0.0) -> (1.0, 1.0, 1.0)???
#       stripe.color = [100, 50, 10]
#   dot dict for less obfuscation
#   there must be nicer ways for permutating colors...
#   make delay an LEDStrip attribute
#   CLI


class LEDStrip:
    color = None

    def __init__(self, color = [0, 0, 0]):
        """ Store initial color, create sPWM channels accordingly. """

        self.color = color[:]

        self.red_pwm = GPIO.PWM(RED_PIN, 100)
        self.green_pwm = GPIO.PWM(GREEN_PIN, 100)
        self.blue_pwm = GPIO.PWM(BLUE_PIN, 100)

        self.red_pwm.start(self.color[0])
        self.green_pwm.start(self.color[1])
        self.blue_pwm.start(self.color[2])

    def update_color(self):
        """ Update PWM values for all color channels. """

        self.red_pwm.ChangeDutyCycle(self.color[0]) 
        self.green_pwm.ChangeDutyCycle(self.color[1]) 
        self.blue_pwm.ChangeDutyCycle(self.color[2])  

    def morph_step(self, target_color):
        """ Morph self.color randomly into the direction of target_color by one step. """

        # list of the indices of colors that still need to be changed to reach target_color
        available = [i for i in range(3) if self.color[i] != target_color[i]]

        if available:
            color_index = choice(available)

            if self.color[color_index] > target_color[color_index]:
                self.color[color_index] -= 1
            else:
                self.color[color_index] += 1

        self.update_color()


    def morph_color(self, target_color = None, delay=0.1):
        """ Applies morph_steph until the target_color is reached. """       

        if not target_color:
            target_color = [randint(0, 100) for x in range(3)]

        print("current color (RGB): ", self.color)
        print("target color (RGB): ", target_color)

        while target_color != self.color:
            self.morph_step(target_color)
            sleep(delay)

    def test_channels(self):
        """ Test all channels. """

        print('RED active')
        self.morph_color([100, 0, 0])
        sleep(1)
        print('GREEN active')
        self.morph_color([0, 100, 0])
        sleep(1)
        print('BLUE active')
        self.morph_color([0, 0, 100])
        sleep(1)


if __name__ == '__main__':
    try:
        strip = LEDStrip()

        # DISABLE THIS for random color changes
        strip.test_channels()

        # mix colors 'til the end of the days
        while True:
            strip.morph_color()
            sleep(3)        
    except Exception as e:
        print(e)

    finally:
        GPIO.cleanup()
