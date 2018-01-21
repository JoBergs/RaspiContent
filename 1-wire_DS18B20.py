#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/measuring-and-logging-temperature-with-the-1-wire-sensor-ds18b20-and-a-raspberry-pi/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import glob, os, sys, time
import numpy as np


class TemperatureSensor:
    def __init__(self, base_path= '/sys/bus/w1/devices/', 
                     file_name='/w1_slave', default=25.0):

        self.default = default

        try:
            self.sensor_path = glob.glob(base_path + '28*')[0] + file_name 
        except:
            print("Bad sensor path")

    def get_temperature(self):
        temperature = self.default

        try:           
            with open(self.sensor_path, 'r') as f:
                data = f.read()

                if 'YES\n' not in data:
                    raise Exception()
                temperature = round(float(data.rsplit('t=',1)[1])/1000, 1)    
        except:          
            print("Can't read temperature sensor!")   

        return float(temperature) 

    def log_temperature(self, interval=5.0):
        temperatures = []
        
        while True:
            time.sleep(interval)
            temperatures.append(self.get_temperature())
            print('Temperature: ' + str(temperatures[-1]))
            np.save('temperatures', np.array(temperatures))
            
        # load stored temperatures with
        # np.load('temperatures.npy')

if __name__ == "__main__":
    sensor = TemperatureSensor()

    if sys.argv[-1] == "log":
        sensor.log_temperature()
    else:
        print(sensor.get_temperature())
