#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/python-webframework-django-on-the-raspberry-pi
# Taken from the ebook Test-Driven Development with Python by Harry Percival:
# https://github.com/hjwp/book-example
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

from django.shortcuts import redirect, render
from lists.models import Item, List

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GREEN_PIN = 38
BLUE_PIN = 40
GPIO.setup([GREEN_PIN, BLUE_PIN],GPIO.OUT)

def blink(color='blue'):
    LED_PIN = BLUE_PIN
    if color == 'green':
        LED_PIN = GREEN_PIN

    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(0.5)    
    GPIO.output(LED_PIN,GPIO.LOW)


def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    blink('green')
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    blink()
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

