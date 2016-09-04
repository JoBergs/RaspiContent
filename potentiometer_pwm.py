#!/usr/bin/env python
 
# Written by Limor "Ladyada" Fried for Adafruit Industries, (c) 2015
# This code is released into the public domain
# Modified by Johannes "Knight of Pi" Bergs for module usage.

from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# setup pwm LED
LED = 17

GPIO.setup(LED, GPIO.OUT)

pwm_LED = GPIO.PWM(LED, 100)
pwm_LED.start(0)


# freely chosen SPI pins
SPICLK = 16  # BOARD 36
SPIMISO = 19  # BOARD 35
SPIMOSI = 20  # BOARD 38
SPICS = 25  # BOARD 35
 
# set up the SPI interface pins
GPIO.setup([SPIMOSI, SPICLK, SPICS], GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
 
# 10k trim pot connected to adc #0
potentiometer_adc = 0;

 
# read SPI data from MCP3008 (or MCP3002???) chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)
 
        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low
 
        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1
 
        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
 
def read_potentiometer():
    trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    return round(trim_pot / 1024.0, 2)
 

if __name__ == "__main__":
    """ Test reading the potentiomenter. """

    import time

    while True:
        trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        print("trim_pot:", trim_pot)
        print("normalized: ", round(trim_pot / 1024.0, 2))
        pwm_LED.ChangeDutyCycle(int(trim_pot/10.2))
        time.sleep(0.5)
