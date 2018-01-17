# WIP! DO NOT USE!

import glob, os

# modify this:
#   make a function that perpetually reads the temperature and stores it to a file

class TemperatureSensor:
    def __init__(self, base_path= '/sys/bus/w1/devices/', 
                     file_name='/w1_slave', default=25.0):

        self.default = default
        self.sensor_path = glob.glob(base_path + '28*')[0] + file_name 

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

        return float(temperature) 

if __name__ == "__main__":
    sensor = TemperatureSensor()
    print(sensor.get_value())