#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/[FILL OUT]
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
def start_thread(current):
    try:
       _thread.start_new_thread( print_time, ("Thread-" + str(current), 2, ) )
    except:
       print ("Error: unable to start thread")

thread_count = 1000
current = 0
while current < thread_count:
    current += 1
    start_thread(current)