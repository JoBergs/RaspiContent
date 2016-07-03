#!/usr/bin/python
#encoding:utf-8

# This program implements a simple intrusion detection.
# If a bluetooth device (e.g. a mobile phone) is detected, no alarm is
# set off. But, if the device is not present and movement is detected,
# a piezo buzzer is set off for 5 seconds.

# This script is part of my tutorial at
# www.knight-of-pi.org/intrusion-detection-with-a-raspberry-pi-and-a-smartphone-over-bluetooth


import time
import bluetooth
import RPi.GPIO as GPIO

phone = "E4:32:CB:FE:96:B8"

pin_data = 3
pin_LED = 11
pin_buzzer = 12

at_home = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.output(pin_buzzer, GPIO.LOW)  # make very sure that the beeper is off

def action(pin):
    print 'Sensor detected action!'
    if not at_home:
        print "Alert! Intruder detected!"
        GPIO.output(pin_buzzer, GPIO.HIGH)
        time.sleep(5)
    GPIO.output(pin_buzzer, GPIO.LOW)
    return
 
GPIO.add_event_detect(7, GPIO.RISING)
GPIO.add_event_callback(7, action)

def search():         
    devices = bluetooth.discover_devices(duration=5, lookup_names = True)
    print devices
    return devices

try:  
    while True:   
        GPIO.output(pin_LED, GPIO.LOW) 
        if at_home:
            GPIO.output(pin_LED, GPIO.HIGH)

        at_home = False

        print "Scanning for bluetooth devices..."
        results = search()

        for addr, name in results:
            if addr == phone:
                at_home = True
                print time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), ": ... detected phone ", name     
              
        time.sleep(5)
    
except KeyboardInterrupt:
    GPIO.cleanup()
