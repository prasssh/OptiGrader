import numpy as np 
import cv2
import functions

#####################################
path = "1.jpg"
widthImg = 600
heightImg = 600



########################################
img = cv2.imread(path)
img2 = cv2.resize(img, (widthImg, heightImg))  #image resizing
imgContours = img.copy()
imgBiggestContours = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny= cv2.Canny(imgBlur,10,50)

imageArray = ([img, imgGray,imgBlur,imgCanny])

cv2.imshow("Stacked", )
cv2.waitKey(0)






