#!/usr/bin/python
#encoding:utf-8

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
rows = [10, 11, 12]  # 16, 18, 40 on board
columns = [19, 21, 23]  # 16, 18, 40 on board
GPIO.setup(rows + columns, GPIO.OUT)

# it may be better to make functions which generate lists of tuples of pins to activate
# for decimal:
#   take the input number modulo 10
#   i = 0
#   for col in cols
#       GPIO.output(columns[col], GPIO.HIGH)
#       for row in rows
#           if i < input
#               GPIO.output(columns[col], GPIO.HIGH)
#           else
#               break;
#       i += 1
#           

# make function all_off 

if __name__ == '__main__':
    GPIO.output(columns[0], GPIO.HIGH)
    GPIO.output(rows[0], GPIO.HIGH)
    sleep(0.1)
    GPIO.output(rows[0], GPIO.LOW)
    GPIO.output(rows[1], GPIO.HIGH)
    sleep(0.1)
    GPIO.output(rows[1], GPIO.LOW)
    GPIO.output(rows[2], GPIO.HIGH)
    sleep(0.1)
    GPIO.output(rows[2], GPIO.LOW)
    GPIO.output(columns[0], GPIO.LOW)  

