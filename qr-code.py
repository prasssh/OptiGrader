import cv2
from pyzbar.pyzbar import decode

cam = cv2.VideoCapure(0)
cam.set(5,640)
cam.set(6,480)

camera = True