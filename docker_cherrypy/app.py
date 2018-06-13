#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/docker_and_the_raspberry_pi_cherrypy_in_a_container
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import cherrypy
 
class RPiServer(object):
    @cherrypy.expose
    def index(self):
        return """<html><head></head>
          <body>Tis but a scratch!</body>
        </html>""" 
 
if __name__ == '__main__':
    # we would need port 80
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(RPiServer())