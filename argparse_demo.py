#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/python-argparse-massively-simplifies-parsing-complex-command-line-parameters/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import argparse, sys

DESCRIPTION = '''This is a demo of the capabilities of argparse. '''

parser = argparse.ArgumentParser(description=DESCRIPTION)

parser.add_argument('-d', '--debug', nargs='?', metavar='1..5', type=int,
                                choices=range(1, 5), default=2,
                                help='Debug level is a value between 1 and 5')
parser.add_argument('-g', '--gui', action='store_true', 
                                      help='Start in graphical mode if given')
parser.add_argument('-o', '--output', nargs='?', metavar='path', 
                                     type=str, default="~/output.txt",
                                     help='Store program output in the file passed after -o')

arguments = parser.parse_args(sys.argv[1:])
print(arguments)
print("GUI enabled? ", arguments.gui)
