#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/decorator-for-easy-access-to-protected-raspberry-pi-system-files/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import os, subprocess

from stat import ST_MODE
from pwd import getpwuid

# temporarily changes file permissions for write access to protected files
def write_access(func):
    def func_wrapper(path, *args):           
        if not os.path.isfile(path):  # create file if it doesn't exist
            subprocess.call(['touch ' + path], shell=True)   

        owner = getpwuid(os.stat(path).st_uid).pw_name
        perms = oct(os.stat(path)[ST_MODE])[-3:]
        subprocess.call(['sudo chgrp pi ' + path], shell=True)
        subprocess.call(['sudo chmod g=rw ' + path], shell=True)

        return_value = func(path, *args)

        subprocess.call(['sudo chmod ' + perms + ' ' + path], shell=True)
        subprocess.call(['sudo chgrp ' + owner + ' ' + path], shell=True)

        return return_value

    return func_wrapper


@write_access
def read_protected_file(path):
    with open(path, 'r') as f:
        return f.read()

if __name__ == "__main__":
    print(read_protected_file('/etc/wpa_supplicant/wpa_supplicant.conf'))