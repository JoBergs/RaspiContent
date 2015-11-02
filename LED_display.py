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

def convert_to_decimal(number):
    pin_list = []
    number = number % 10  

    i = 0
    for col in columns:
        pin_list.append(col)
        #GPIO.output(columns[col], GPIO.HIGH)
        for row in rows:

            if i < number:
                pin_list.append(row)
                #GPIO.output(columns[col], GPIO.HIGH)
            else:
                break;
            i += 1   

    return pin_list   


def convert_to_binary(number):
    pin_list = [] 

    i = 0
    for col in columns:
        pin_list.append(col)
        #GPIO.output(columns[col], GPIO.HIGH)
        for row in rows:

            if i < number:
                pin_list.append(row)
                #GPIO.output(columns[col], GPIO.HIGH)
            else:
                break;
            i += 1   

    return pin_list  

def display_pins(pin_list):
    for pin in pin_list:
         GPIO.output(pin, GPIO.HIGH)

def all_off():
    for pin in columns + rows:  
        GPIO.output(pin, GPIO.LOW)  

def display_number(number = 5, numbering='decimal'):
    all_off()
    number = number % 10
    if numbering == 'decimal':
        pin_list = convert_to_decimal(number)
    else:
        pin_list = convert_to_binary(number)
    display_pins(pin_list)

# make function all_off 

if __name__ == '__main__':
    display_number()
    sleep(2)
    all_off()
    #print(convert_decimal_to_pins(366))
    '''
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
    '''

