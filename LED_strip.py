#!/usr/bin/python
#encoding:utf-8

from random import choice, randint

from webiopi import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

RED_PIN , GREEN_PIN, BLUE_PIN = 11, 12, 13 # BOARD numbering
GPIO.setup([RED_PIN, GREEN_PIN, BLUE_PIN], GPIO.OUT)

# implement color as property that receives values (0.0, 0.0, 0.0) -> (1.0, 1.0, 1.0)???
# stripe.color = [100, 50, 10]


class LEDStripe:
    def __init__(self, color = [0, 0, 0]):

        self.store_color(color)

        self.red_pwm = GPIO.PWM(RED_PIN, 100)
        self.green_pwm = GPIO.PWM(GREEN_PIN, 100)
        self.blue_pwm = GPIO.PWM(BLUE_PIN, 100)

        self.red_pwm.start(self.red)
        self.green_pwm.start(self.green)
        self.blue_pwm.start(self.blue)

    def store_color(self, color):
        self.red = color[0]
        self.green =  color[1]
        self.blue =  color[2]


    def set_color(self, color=None):
        ''' color is a list with three values red, green and blue, 
        each from 0 to 100: [0,0,0] .. [100, 100, 100] '''

        if color:
            self.store_color(color)

        self.red_pwm.ChangeDutyCycle(self.red) 
        self.green_pwm.ChangeDutyCycle(self.green) 
        self.blue_pwm.ChangeDutyCycle(self.blue)     
        

def morph_color(current_color, target_color):
    """ Morph current_color into the direction of target_color by one step. """

    # build indices
    available = []

    for i in range(3):
        if current_color[i] != target_color[i]:
            available.append(i)

    if available:
        color_index = choice(available)

        if current_color[color_index] > target_color[color_index]:
            current_color[color_index] -= 1
        else:
            current_color[color_index] += 1

    return current_color

if __name__ == '__main__':
    try:
        stripe = LEDStripe()
        stripe.set_color([20, 50, 70])
        sleep(3)        
    except Exception as e:
        print(e)

    finally:
        GPIO.cleanup()
