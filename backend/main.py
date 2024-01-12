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
gradePoints = functions.getCornerPoints(rectCon[1]) #get corner points
#print(biggestContour)

if biggestContour.size != 0 and gradePoints.size != 0:
    #wrapping biggest rctangle
    cv2.drawContours(imgBiggestContours, biggestContour, -1, (0, 255, 0), 20) 
    cv2.drawContours(imgBiggestContours, gradePoints, -1, (255, 0, 0), 20)

    biggestContour= functions.reorder(biggestContour)
    gradePoints = functions.reorder(gradePoints)
    pts1 = np. float32(biggestContour)  #preparing points for wrap
    pts2 = np. float32([[0,0],[widthImg, 0], [0, heightImg], [widthImg, heightImg]]) #prepare points for wrap
    matrix = cv2.getPerspectiveTransform(pts1, pts2) #get transformation matrix
    imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg)) #apply wrap perspective

    #wrapping second largest rectangle
    gradePoints = functions.reorder(gradePoints) # REORDER FOR WARPING
    ptsG1 = np.float32(gradePoints)  # PREPARE POINTS FOR WARP
    ptsG2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])  # PREPARE POINTS FOR WARP
    matrixG = cv2.getPerspectiveTransform(ptsG1, ptsG2)# GET TRANSFORMATION MATRIX
    imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150)) # APPLY WARP PERSPECTIVE

    #for threshold
    

imgBlank = np.zeros_like(img)
imageArray = ([img, imgGray,imgBlur,imgCanny],
            [imgContours,imgBiggestContours,imgBlank, imgBlank])
imgStacked = functions.stackImages(imageArray,0.2)
cv2.imshow("Stacked", imgStacked)
cv2.waitKey(0)

