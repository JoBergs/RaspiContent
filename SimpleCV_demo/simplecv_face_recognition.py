#!/usr/bin/python 
 
import picamera
import time
from SimpleCV import Color, Image, np
import wiringpi2 as wiringpi
 
pin_base = 65
i2c_addr = 0x20
 
quality = 400     # Parametro "quality" per la funzione findKeypointMatch
minMatch = 0.3    # Parametro "minDist" per la funzione findKeypointMatch
 
try:
    password = Image("password.jpg")
except:
    password = None
 
mode = "unsaved"
saved = False
minDist = 0.25
 
wiringpi.wiringPiSetup()
wiringpi.mcp23017Setup(pin_base,i2c_addr)
wiringpi.pinMode(65, 1)         # imposta GPA0 come output  
wiringpi.digitalWrite(65, 0)    # imposta GPA0 a 0 (0V, off)
wiringpi.pinMode(72, 1)         # imposta GPA7 come output  
wiringpi.digitalWrite(72, 0)    # imposta GPA7 a 0 (0V, off)
 
with picamera.PiCamera() as camera:
 while True:
    camera.start_preview()
    time.sleep(10)
    camera.capture('pifacepw.jpg')
    image=Image("pifacepw.jpg")
    camera.stop_preview()
    faces = image.findHaarFeatures("face.xml") # Riconosce il viso mediante il file HaarCFeatures "face"
    if faces:
        if not password:
            faces.draw()
            face = faces[-1]
            password = face.crop().save("password.jpg")
            print "Salvataggio volto di riferimento eseguito"
            print "Termino il programma"
            break
        else:
            faces.draw()
            face = faces[-1]
            template = face.crop()
            template.save("passwordmatch.jpg")
            keypoints = password.findKeypointMatch(template,quality,minDist,minMatch)
            if keypoints:
                print "Bentornato - mi sembri il viso giusto"
                wiringpi.digitalWrite(65, 1)  
                wiringpi.digitalWrite(72, 0)
                domanda = raw_input("Desideri utilizzare l'ultima foto come password? Y/N").strip()
                if domanda == "Y":
                    image = cam.getImage().scale(320, 240)
                    faces = image.findHaarFeatures("face.xml")
                    tryit = 1
                    while not tryit == 10 or not faces:
                        image = cam.getImage().scale(320, 240)
                        faces = image.findHaarFeatures("face.xml")
                        tryit += 1
                    if not faces:
                        "Non trovo nessauna faccia"
                        break
                    else:
                        faces.draw()
                        face = faces[-1]
                        password = face.crop().save("password.jpg")
                        face.crop().show()
                        print "Salvataggio eseguito"
                        print "Termino il programma"
                        time.sleep(1)
                        break
                else:
                    print "OK..."
                    break
                     
            else:
                print "Non ti riconosco"
                print "Attivo l'allarme"
                wiringpi.digitalWrite(65, 0)  
                wiringpi.digitalWrite(72, 1)
                break
    else:
        break