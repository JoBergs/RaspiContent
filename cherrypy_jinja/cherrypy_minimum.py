#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/better-rpi-remote-controls-cherrypy-and-jinja-for-html-templating/
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import cherrypy

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

# Template ./templates/index.html contains
# We are the knights that always say <h1>{{ saying }}</h1>

class MinimumServer:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render(saying="Ni!")


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(MinimumServer())