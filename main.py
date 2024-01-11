import numpy as np 
import cv2
import functions
path = "1.jpg"
widthImg = 500
heightImg = 500

img = cv2.imread(path)

#image pre-processing
img2 = cv2.resize(img, (widthImg, heightImg))  #image resizing
imgContours = img.copy()
imgBiggestContours = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny= cv2.Canny(imgBlur,10,50)

#finding contours
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # to find all contours
cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)


#finding rectangles
rectCon = functions.rectContour(contours)
biggestContour = functions.getCornerPoints(rectCon[0])


imgBlank = np.zeros_like(img)
imageArray = ([img, imgGray,imgBlur,imgCanny],
            [imgContours,imgBiggestContours,imgBlank, imgBlank])
imgStacked = functions.stackImages(imageArray,0.2)
cv2.imshow("Stacked", imgStacked)
cv2.waitKey(0)






