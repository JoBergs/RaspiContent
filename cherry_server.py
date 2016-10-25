import random, string
from time import sleep

import cherrypy

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class RaspiServer(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="blink">
              <input type="text" value="13" name="pin_str" />
              <button type="submit">Blink now!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def blink(self, pin_str="13"):
        pin = int(pin_str)
        GPIO.setup(pin, GPIO.OUT)        
        sleep(0.5)
        GPIO.output(pin, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(pin, GPIO.LOW)

        return "Blinked on Pin " + str(pin) 



if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(RaspiServer())

