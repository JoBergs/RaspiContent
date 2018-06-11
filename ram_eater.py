#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/[FILL OUT]
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import sys, time

WAIT = 10

def eat_RAM(depth=300):
    tmp = [[x for x in range(0, depth)] for y in range(0, depth) for z in range(0, depth)]
    time.sleep(WAIT)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        eat_RAM(int(sys.argv[1]))
    else:
        eat_RAM()