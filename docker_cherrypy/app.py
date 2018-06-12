import cherrypy
 
class RPiServer(object):
    @cherrypy.expose
    def index(self):
        return """<html><head></head>
          <body>Tis but a scratch!</body>
        </html>""" 
 
if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(RPiServer())