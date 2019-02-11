import smbus, struct, time

channel = 2
address = 0x61  # find address with sudo i2cdetect -y -r 2

bus = smbus.SMBus(channel)

# set measurement interval to 2 seconds
bus.write_byte_data(address, 0x4600, 2)

time.sleep(2)

# trigger contionuous measurement
bus.write_byte_data(address, 0x0010, 0)

time.sleep(0.5)

data = bus.read_i2c_block_data(address, 0x0300, 18)  # same result

del data[2::3]
# split into seperate data chunks and convert to float from Big Endian
co2, temp, hum = [struct.unpack('>f', bytes(data[i:i + 4]))[0]
                            for i in range(0, len(data), 4)]


print('CO2: ', co2, 'Temp: ', temp, 'Hum: ', hum)





