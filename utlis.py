nijeosk
platinum7765
Invisible

See Luuu — 07/08/2023 22:00
Hajul
Eluu — 07/08/2023 22:00
Hidden love Kati cuteeee:lalu:
See Luuu — 07/08/2023 22:43
Heriiii?:riverpepe:
I am not over Duan Jiaxu and Sang Zhi :riverpepe: 
Eluu — 07/08/2023 22:58
Epi 4:kyuddie:
Eluu — 07/08/2023 22:58
Suru mai kasto cuteeee k
See Luuu — 07/08/2023 22:59
That's just trailer:lalu:
Eluu — 11/08/2023 20:50
Image
K ho feri
See Luuu — 11/08/2023 21:00
Ari collect ni garne
Aaja lyauna hunthyo ta hyatteri
Tara feri k update garera pdf halne ho
:isaac:
Ful babu — 11/08/2023 21:18
Lau naa
:huh:
Ful babu — 12/08/2023 15:46
@See Luuu kei vaneki ho?
See Luuu — 12/08/2023 15:47
:huh:
Ful babu — 12/08/2023 16:01
:array:
Kina mention garya
Eluu — 16/08/2023 11:32
@Ful babu
Timle k tyo WT  ma last ma aauthyo ni php and sql connect garera lekhne euta code tyo garyathyau?
Ful babu — 16/08/2023 11:40
Maile birse 
Tara j hos euta sir le lekhaideko wala thyo ni php connect garne code ani maile tyo matra padera j sodey ni tei lekhdethe
Eluu — 18/09/2023 08:00
@gals________
Assessment question cha ra?
See Luuu — 18/09/2023 08:04
Chaina:imotional:
See Luuu — 18/09/2023 08:05
Design ta code bujhi?
Simple simple ta garna aaucha aru ta kk ho
Video ni gatilo bhetina
Eluu — 18/09/2023 08:35
Balla padhna suru garya :imotional:
Tya ta kaile pugnu:isaac:
See Luuu — 18/09/2023 08:51
:huh:
Ful babu — 18/09/2023 10:13
:NotMe:
@See Luuu maam ko drive  ko notes link
Ful babu — 18/09/2023 10:21
Ehh vete vete
Ful babu — 01/01/2024 19:05
https://youtu.be/SWaYRyi0TTs?si=2lJ3jww3O8tuDCyz
YouTube
Murtaza's Workshop - Robotics and AI
Traffic Signs Classification Using Convolution Neural Networks CNN ...
Image
https://youtu.be/8gPONnGIPgw?si=NbMdHArCJQmmPwgU
YouTube
Murtaza's Workshop - Robotics and AI
AI Virtual Mouse | OpenCV Python | Computer Vision
Image
https://youtu.be/0IqCOPlGBTs?si=9uEQfIneJiDVEYqd
YouTube
Murtaza's Workshop - Robotics and AI
OPTICAL MARK RECOGNITION (OMR) MCQ Automated Grading- OpenCV Python
Image
Ful babu — 06/01/2024 18:02
https://github.com/Udayraj123/OMRChecker?tab=readme-ov-file
GitHub
GitHub - Udayraj123/OMRChecker: Read OMRs fast and accurately using...
Read OMRs fast and accurately using a scanner 🖨 or your phone 🤳. - GitHub - Udayraj123/OMRChecker: Read OMRs fast and accurately using a scanner 🖨 or your phone 🤳.
GitHub - Udayraj123/OMRChecker: Read OMRs fast and accurately using...
See Luuu — 06/01/2024 18:04
oye maile ni yei herdai the
arko openMCR bhanne ni raicha
Ful babu — 06/01/2024 18:08
eh eh okk
See Luuu — 06/01/2024 19:15
@Ful babu
yo omrchecker ma python matra ho kya ho
Ful babu — 06/01/2024 19:29
ahh hola
Ful babu — 09/01/2024 19:52
https://github.com/murtazahassan/Optical-Mark-Recognition-OPENCV
GitHub
GitHub - murtazahassan/Optical-Mark-Recognition-OPENCV
Contribute to murtazahassan/Optical-Mark-Recognition-OPENCV development by creating an account on GitHub.
GitHub - murtazahassan/Optical-Mark-Recognition-OPENCV
@See Luuu
See Luuu — 09/01/2024 19:53
Hajur
Ful babu — Yesterday at 16:22
https://github.com/abuanwar072/Welcome-Login-Signup-Page-Flutter
GitHub
GitHub - abuanwar072/Welcome-Login-Signup-Page-Flutter: Mobile app ...
Mobile app onboarding, Login, Signup page with #flutter. - GitHub - abuanwar072/Welcome-Login-Signup-Page-Flutter: Mobile app onboarding, Login, Signup page with #flutter.
GitHub - abuanwar072/Welcome-Login-Signup-Page-Flutter: Mobile app ...
Ful babu — Yesterday at 22:10
https://github.com/Zubairrdev/Login_Signup_pages
GitHub
GitHub - Zubairrdev/Login_Signup_pages
Contribute to Zubairrdev/Login_Signup_pages development by creating an account on GitHub.
Ful babu — Today at 08:17
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
    imgCanny = cv2.Canny(imgBlur,10,70) # APPLY CANNY 

    try:
        ## FIND ALL COUNTOURS
        imgContours = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
        imgBigContour = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
        contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # FIND ALL CONTOURS
        cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10) # DRAW ALL DETECTED CONTOURS
        rectCon = utlis.rectContour(contours) # FILTER FOR RECTANGLE CONTOURS
        biggestPoints= utlis.getCornerPoints(rectCon[0]) # GET CORNER POINTS OF THE BIGGEST RECTANGLE
        gradePoints = utlis.getCornerPoints(rectCon[1]) # GET CORNER POINTS OF THE SECOND BIGGEST RECTANGLE

        

        if biggestPoints.size != 0 and gradePoints.size != 0:

            # BIGGEST RECTANGLE WARPING
            biggestPoints=utlis.reorder(biggestPoints) # REORDER FOR WARPING
            cv2.drawContours(imgBigContour, biggestPoints, -1, (0, 255, 0), 20) # DRAW THE BIGGEST CONTOUR
            pts1 = np.float32(biggestPoints) # PREPARE POINTS FOR WARP
            pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
            matrix = cv2.getPerspectiveTransform(pts1, pts2) # GET TRANSFORMATION MATRIX
            imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg)) # APPLY WARP PERSPECTIVE

            # SECOND BIGGEST RECTANGLE WARPING
            cv2.drawContours(imgBigContour, gradePoints, -1, (255, 0, 0), 20) # DRAW THE BIGGEST CONTOUR
            gradePoints = utlis.reorder(gradePoints) # REORDER FOR WARPING
            ptsG1 = np.float32(gradePoints)  # PREPARE POINTS FOR WARP
            ptsG2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])  # PREPARE POINTS FOR WARP
            matrixG = cv2.getPerspectiveTransform(ptsG1, ptsG2)# GET TRANSFORMATION MATRIX
            imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150)) # APPLY WARP PERSPECTIVE

            # APPLY THRESHOLD
            imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY) # CONVERT TO GRAYSCALE
            imgThresh = cv2.threshold(imgWarpGray, 170, 255,cv2.THRESH_BINARY_INV )[1] # APPLY THRESHOLD AND INVERSE

            boxes = utlis.splitBoxes(imgThresh) # GET INDIVIDUAL BOXES
            cv2.imshow("Split Test ", boxes[3])
            countR=0
            countC=0
            myPixelVal = np.zeros((questions,choices)) # TO STORE THE NON ZERO VALUES OF EACH BOX
            for image in boxes:
                #cv2.imshow(str(countR)+str(countC),image)
                totalPixels = cv2.countNonZero(image)
                myPixelVal[countR][countC]= totalPixels
                countC += 1
                if (countC==choices):countC=0;countR +=1

            # FIND THE USER ANSWERS AND PUT THEM IN A LIST
            myIndex=[]
            for x in range (0,questions):
                arr = myPixelVal[x]
                myIndexVal = np.where(arr == np.amax(arr))
                myIndex.append(myIndexVal[0][0])
            #print("USER ANSWERS",myIndex)

            # COMPARE THE VALUES TO FIND THE CORRECT ANSWERS
            grading=[]
            for x in range(0,questions):
                if ans[x] == myIndex[x]:
                    grading.append(1)
                else:grading.append(0)
            #print("GRADING",grading)
            score = (sum(grading)/questions)*100 # FINAL GRADE
            #print("SCORE",score)

            # DISPLAYING ANSWERS
            utlis.showAnswers(imgWarpColored,myIndex,grading,ans) # DRAW DETECTED ANSWERS
            utlis.drawGrid(imgWarpColored) # DRAW GRID
            imgRawDrawings = np.zeros_like(imgWarpColored) # NEW BLANK IMAGE WITH WARP IMAGE SIZE
            utlis.showAnswers(imgRawDrawings, myIndex, grading, ans) # DRAW ON NEW IMAGE
            invMatrix = cv2.getPerspectiveTransform(pts2, pts1) # INVERSE TRANSFORMATION MATRIX
... (38 lines left)
Collapse
OMR_Main.py
7 KB
import cv2
import numpy as np

## TO STACK ALL THE IMAGES IN ONE WINDOW
def stackImages(imgArray,scale,lables=[]):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        #print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver

def reorder(myPoints):

    myPoints = myPoints.reshape((4, 2)) # REMOVE EXTRA BRACKET
    print(myPoints)
    myPointsNew = np.zeros((4, 1, 2), np.int32) # NEW MATRIX WITH ARRANGED POINTS
    add = myPoints.sum(1)
    print(add)
    print(np.argmax(add))
    myPointsNew[0] = myPoints[np.argmin(add)]  #[0,0]
    myPointsNew[3] =myPoints[np.argmax(add)]   #[w,h]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] =myPoints[np.argmin(diff)]  #[w,0]
    myPointsNew[2] = myPoints[np.argmax(diff)] #[h,0]

    return myPointsNew

def rectContour(contours):

    rectCon = []
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if len(approx) == 4:
                rectCon.append(i)
    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=True)
    #print(len(rectCon))
    return rectCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True) # LENGTH OF CONTOUR
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True) # APPROXIMATE THE POLY TO GET CORNER POINTS
    return approx

def splitBoxes(img):
    rows = np.vsplit(img,5)
    boxes=[]
    for r in rows:
        cols= np.hsplit(r,5)
        for box in cols:
            boxes.append(box)
    return boxes

def drawGrid(img,questions=5,choices=5):
    secW = int(img.shape[1]/questions)
    secH = int(img.shape[0]/choices)
    for i in range (0,9):
        pt1 = (0,secH*i)
        pt2 = (img.shape[1],secH*i)
        pt3 = (secW * i, 0)
        pt4 = (secW*i,img.shape[0])
        cv2.line(img, pt1, pt2, (255, 255, 0),2)
        cv2.line(img, pt3, pt4, (255, 255, 0),2)

    return img

def showAnswers(img,myIndex,grading,ans,questions=5,choices=5):
     secW = int(img.shape[1]/questions)
... (25 lines left)
Collapse
utlis.py
5 KB
﻿
import cv2
import numpy as np

## TO STACK ALL THE IMAGES IN ONE WINDOW
def stackImages(imgArray,scale,lables=[]):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        #print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver

def reorder(myPoints):

    myPoints = myPoints.reshape((4, 2)) # REMOVE EXTRA BRACKET
    print(myPoints)
    myPointsNew = np.zeros((4, 1, 2), np.int32) # NEW MATRIX WITH ARRANGED POINTS
    add = myPoints.sum(1)
    print(add)
    print(np.argmax(add))
    myPointsNew[0] = myPoints[np.argmin(add)]  #[0,0]
    myPointsNew[3] =myPoints[np.argmax(add)]   #[w,h]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] =myPoints[np.argmin(diff)]  #[w,0]
    myPointsNew[2] = myPoints[np.argmax(diff)] #[h,0]

    return myPointsNew

def rectContour(contours):

    rectCon = []
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if len(approx) == 4:
                rectCon.append(i)
    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=True)
    #print(len(rectCon))
    return rectCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True) # LENGTH OF CONTOUR
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True) # APPROXIMATE THE POLY TO GET CORNER POINTS
    return approx

def splitBoxes(img):
    rows = np.vsplit(img,5)
    boxes=[]
    for r in rows:
        cols= np.hsplit(r,5)
        for box in cols:
            boxes.append(box)
    return boxes

def drawGrid(img,questions=5,choices=5):
    secW = int(img.shape[1]/questions)
    secH = int(img.shape[0]/choices)
    for i in range (0,9):
        pt1 = (0,secH*i)
        pt2 = (img.shape[1],secH*i)
        pt3 = (secW * i, 0)
        pt4 = (secW*i,img.shape[0])
        cv2.line(img, pt1, pt2, (255, 255, 0),2)
        cv2.line(img, pt3, pt4, (255, 255, 0),2)

    return img

def showAnswers(img,myIndex,grading,ans,questions=5,choices=5):
     secW = int(img.shape[1]/questions)
     secH = int(img.shape[0]/choices)

     for x in range(0,questions):
         myAns= myIndex[x]
         cX = (myAns * secW) + secW // 2
         cY = (x * secH) + secH // 2
         if grading[x]==1:
            myColor = (0,255,0)
            #cv2.rectangle(img,(myAns*secW,x*secH),((myAns*secW)+secW,(x*secH)+secH),myColor,cv2.FILLED)
            cv2.circle(img,(cX,cY),50,myColor,cv2.FILLED)
         else:
            myColor = (0,0,255)
            #cv2.rectangle(img, (myAns * secW, x * secH), ((myAns * secW) + secW, (x * secH) + secH), myColor, cv2.FILLED)
            cv2.circle(img, (cX, cY), 50, myColor, cv2.FILLED)

            # CORRECT ANSWER
            myColor = (0, 255, 0)
            correctAns = ans[x]
            cv2.circle(img,((correctAns * secW)+secW//2, (x * secH)+secH//2),
            20,myColor,cv2.FILLED)
