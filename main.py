import cv2
import numpy as np
import utlis

webCamFeed = True
pathImage = "2.jpg"
# cap = cv2.VideoCapture(0)
# cap.set(10,160)
heightImg = 700
widthImg  = 700
questions=5
choices=5
ans= [1,2,0,2,4]

count=0

while True: