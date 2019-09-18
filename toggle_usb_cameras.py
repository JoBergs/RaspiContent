#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/activate-and-deactivate-linux-usb-cameras-with-python
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import glob, subprocess

def toggle_usb_cameras(state):
    cameras = []

    devices = glob.glob('/sys/bus/usb/devices/*/product')

    for device in devices:
        result = subprocess.run(['cat', device], stdout=subprocess.PIPE)
        if 'camera' in str(result.stdout).lower():
            identfifier = device.split('/')[-2]
            if state:
                subprocess.run(['echo', "'" + device + "'" + ' | sudo tee /sys/bus/usb/drivers/usb/bind'], stdout=subprocess.PIPE)
            else:
                subprocess.run(['echo', "'" + device + "'" + ' | sudo tee /sys/bus/usb/drivers/usb/unbind'], stdout=subprocess.PIPE)


if __name__ == "__main__":
    toggle_usb_cameras('off')