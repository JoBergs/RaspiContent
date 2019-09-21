#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/terminal-control-with-pexpect-automate-bluetooth-connection
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import time

import pexpect


def scan_bluetooth_agents():
    devices = {}

    child = pexpect.spawn('sudo bluetoothctl')
    child.sendline ('scan on')
    time.sleep(10)
    child.sendline ('scan off')
    
    line = child.readline()
    while b'scan off' not in line:
        if b'Device' in line:            
            line = str(line.replace(b"\r\n", b'')).strip("b'").strip("'")
            address, name = line.split('Device ')[1].split(' ', 1)
            devices[name] = address

        line = child.readline()

    child.sendline ('exit')

    return devices


def trust_device(address):
    child = pexpect.spawn('sudo bluetoothctl')
    child.sendline ('agent off')
    time.sleep(0.5)
    child.sendline ('pairable on')
    time.sleep(0.5)
    child.sendline ('agent NoInputNoOutput')
    time.sleep(0.5)
    child.sendline ('default-agent')
    time.sleep(0.5)
    child.sendline ('pair ' + address)
    time.sleep(5)
    child.sendline ('trust ' + address)
    time.sleep(2)
    child.sendline ('exit')


if __name__ == "__main__":
    devices = scan_bluetooth_agents()
    print(devices)
    trust_device(list(devices.values())[0])

