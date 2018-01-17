# WIP! DO NOT USE!

import os

# Install 1-WIRE

#     sudo nano /boot/config.txt

# Add 

#     dtoverlay=w1-gpio

# Then do

#     sudo modprobe w1-gpio
#     sudo modprobe w1-therm
#     sudo reboot

# modify this:
#   remove logging
#   simplify file access (glob)
#   make a function that perpetually reads the temperature and stores it to a file

class TemperatureSensor:
    def __init__(self, base_path= '/sys/bus/w1/devices', 
                     file_name='w1_slave', default=25.0):

        self.default = default
        # self.logger = logging.getLogger('Error_Log')  
        self.sensor_path = self.get_sensor_path(base_path, file_name)  
            

    def get_sensor_path(self, base_path, sensor_file):
        """ Naive method to find the 1-wire sensors directory and
            return the assembled path to the sensor file. """

        sensor_dir = None

        # list comprehension should work, too
        for root, dirs, files in os.walk(base_path):
            for item in dirs:
                if item != 'w1_bus_master1':
                    sensor_dir = item

        if sensor_dir:
            return '/'.join((base_path, sensor_dir, sensor_file))
        else:           
            print("Can't find temperature sensor!")
            return None

    def get_value(self):
        temperature = self.default

        try:           
            with open(self.sensor_path, 'r') as f:
                line = f.readline()
                crc = line.rsplit(' ',1)
                
                if 'YES\n' in crc:
                    line = f.readline() # read 2nd line
                    temperature = round(float(line.rsplit('t=',1)[1])/1000, 1)    
                    print("Temperature is " + str(temperature) )
                else:
                    raise Exception()        
        except:          
            print("Can't read temperature sensor!")   
            # self.logger.error("Can't read temperature sensor!")

        return float(temperature) 

if __name__ == "__main__":
    sensor = TemperatureSensor()
    print(sensor.get_value())