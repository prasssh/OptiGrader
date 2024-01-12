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
    #if webCamFeed:success, img = cap.read()
    # else:
    img = cv2.imread(pathImage)
    
    img = cv2.resize(img, (widthImg, heightImg)) # RESIZE IMAGE
    imgFinal = img.copy()
    imgBlank = np.zeros((heightImg,widthImg, 3), np.uint8) # CREATE A BLANK IMAGE FOR TESTING DEBUGGING IF REQUIRED
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # CONVERT IMAGE TO GRAY SCALE
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1) # ADD GAUSSIAN BLUR
    imgCanny = cv2.Canny(imgBlur,10,70) # APPLY CANNYyy