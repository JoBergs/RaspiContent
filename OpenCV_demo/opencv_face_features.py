#!/usr/bin/python2.7

import numpy as np
import cv2

# howto set the system path right?

# todo:
#   detect eyes, ears, mouth and nose (maybe with labels?)
#   if no parameter is given, a snapshot shall be made

def extract_features(image):
    face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/haarcascade_eye.xml')

    image = cv2.imread('poi_1.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def make_snapshot():
    image = cv2.imread('poi_1.jpg')
    return image

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        image = cv2.imread(sys.argv[1])
    else:
        image = make_snapshot()

    extract_features(image)