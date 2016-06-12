#!/usr/bin/python2.7
 
# Program for testing Haar Features; as is, searches for a whole face only!

import sys 
import picamera
from SimpleCV import Image
import time

def extract_features(foto):
    print(foto.listHaarFeatures())
    features = foto.findHaarFeatures('face.xml')
    if features:
       for feature in features:
           print "Feature found at coordinate: " + str(feature.coordinates())
           feature.draw() 
    else:
       print "No features!"

    foto.save('foto1.jpg') 
    foto.show()
    time.sleep(5)

def features_from_snapshot(): 
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        time.sleep(10)
        camera.capture('foto.jpg')
        foto=Image("foto.jpg")

        camera.stop_preview()

        return foto

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        foto=Image(sys.argv[1])
    else:
        foto = features_from_snapshot()

    extract_features(foto)
