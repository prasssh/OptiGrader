from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np
import functions
import datetime

app = Flask(__name__)

webCamFeed = True
pathImage = "ThirdSheet.jpg"
cap = cv2.VideoCapture(0)
cap.set(10, 160)
heightImg = 700
widthImg = 700
questions = 5
choices = 5
ans = [1, 2, 0, 2, 4]

count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    global count
    try:
        if webCamFeed:
            success, img = cap.read()
        else:
            img = cv2.imread(pathImage)

        img = cv2.resize(img, (widthImg, heightImg))  # RESIZE IMAGE
        imgFinal = img.copy()
        imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)  # CREATE A BLANK IMAGE FOR TESTING DEBUGGING IF REQUIRED
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # CONVERT IMAGE TO GRAY SCALE
        imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # ADD GAUSSIAN BLUR
        imgCanny = cv2.Canny(imgBlur, 10, 70)  # APPLY CANNY

        # ... (rest of your existing image processing code)

        # SECOND BIGGEST RECTANGLE WARPING
        cv2.drawContours(imgBigContour, gradePoints, -1, (255, 0, 0), 20)  # DRAW THE BIGGEST CONTOUR
        gradePoints = functions.reorder(gradePoints)  # REORDER FOR WARPING
        ptsG1 = np.float32(gradePoints)  # PREPARE POINTS FOR WARP
        ptsG2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])  # PREPARE POINTS FOR WARP
        matrixG = cv2.getPerspectiveTransform(ptsG1, ptsG2)  # GET TRANSFORMATION MATRIX
        imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150))  # APPLY WARP PERSPECTIVE

        # APPLY THRESHOLD
        imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)  # CONVERT TO GRAYSCALE
        imgThresh = cv2.threshold(imgWarpGray, 170, 255, cv2.THRESH_BINARY_INV)[1]  # APPLY THRESHOLD AND INVERSE

        boxes = functions.splitBoxes(imgThresh)  # GET INDIVIDUAL BOXES
        cv2.imshow("Split Test ", boxes[3])
        countR = 0
        countC = 0
        myPixelVal = np.zeros((questions, choices))  # TO STORE THE NON ZERO VALUES OF EACH BOX
        for image in boxes:
            totalPixels = cv2.countNonZero(image)
            myPixelVal[countR][countC] = totalPixels
            countC += 1
            if countC == choices:
                countC = 0
                countR += 1

        # FIND THE USER ANSWERS AND PUT THEM IN A LIST
        myIndex = []
        for x in range(0, questions):
            arr = myPixelVal[x]
            myIndexVal = np.where(arr == np.amax(arr))
            myIndex.append(myIndexVal[0][0])
        # print("USER ANSWERS",myIndex)

        # COMPARE THE VALUES TO FIND THE CORRECT ANSWERS
        grading = []
        for x in range(0, questions):
            if ans[x] == myIndex[x]:
                grading.append(1)
            else:
                grading.append(0)
        # print("GRADING",grading)
        score = (sum(grading) / questions) * 100  # FINAL GRADE
        # print("SCORE",score)

        # DISPLAYING ANSWERS
        functions.showAnswers(imgWarpColored, myIndex, grading, ans)  # DRAW DETECTED ANSWERS
        functions.drawGrid(imgWarpColored)  # DRAW GRID
        imgRawDrawings = np.zeros_like(imgWarpColored)  # NEW BLANK IMAGE WITH WARP IMAGE SIZE
        functions.showAnswers(imgRawDrawings, myIndex, grading, ans)  # DRAW ON NEW IMAGE
        invMatrix = cv2.getPerspectiveTransform(pts2, pts1)  # INVERSE TRANSFORMATION MATRIX
        imgInvWarp = cv2.warpPerspective(imgRawDrawings, invMatrix, (widthImg, heightImg))  # INV IMAGE WARP

        # DISPLAY GRADE
        imgRawGrade = np.zeros_like(imgGradeDisplay, np.uint8)  # NEW BLANK IMAGE WITH GRADE AREA SIZE
        cv2.putText(imgRawGrade, str(int(score)) + "%", (70, 100),
                    cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255), 3)  # ADD THE GRADE TO NEW IMAGE
        invMatrixG = cv2.getPerspectiveTransform(ptsG2, ptsG1)  # INVERSE TRANSFORMATION MATRIX
        imgInvGradeDisplay = cv2.warpPerspective(imgRawGrade, invMatrixG, (widthImg, heightImg))  # INV IMAGE WARP

        # SHOW ANSWERS AND GRADE ON FINAL IMAGE
        imgFinal = cv2.addWeighted(imgFinal, 1, imgInvWarp, 1, 0)
        imgFinal = cv2.addWeighted(imgFinal, 1, imgInvGradeDisplay, 1, 0)

        # IMAGE ARRAY FOR DISPLAY
        imageArray = ([img, imgGray, imgCanny, imgContours],
                      [imgBigContour, imgThresh, imgWarpColored, imgFinal])
        cv2.imshow("Final Result", imgFinal)

    except Exception as e:
        imageArray = ([img, imgGray, imgCanny, imgContours],
                      [imgBlank, imgBlank, imgBlank, imgBlank])

        # LABELS FOR DISPLAY
        labels = [["Original", "Gray", "Edges", "Contours"],
                  ["Biggest Contour", "Threshold", "Warped", "Final"]]

        # STACK IMAGES FOR DISPLAY
        image_array = ([img, imgGray, imgCanny, imgContours],
                       [imgBigContour, imgThresh, imgWarpColored, imgFinal])

        stacked_image = functions.stackImages(image_array, 0.5, labels)

        cv2.imshow("Result", stacked_image)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # Generate timestamp
            file_path = f"F:\\hackathon\\ScannedImages\\myImage_{timestamp}.jpg"
            print(f"Saving image to: {file_path}")
            cv2.imwrite(file_path, imgFinal)
            cv2.rectangle(stacked_image, ((int(stacked_image.shape[1] / 2) - 230), int(stacked_image.shape[0] / 2) + 50),
                          (1100, 350), (0, 255, 0), cv2.FILLED)
            cv2.putText(stacked_image, "Scan Saved", (int(stacked_image.shape[1] / 2) - 200,
                                                      int(stacked_image.shape[0] / 2)),
                        cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 5, cv2.LINE_AA)
            cv2.imshow('Result', stacked_image)
            cv2.waitKey(300)
            count += 1

            file_path = f"F:\\hackathon\\ScannedImages\\myImage{count}.jpg"
            print(f"Saving image to: {file_path}")
            cv2.imwrite(file_path, imgFinal)
            count += 1
            print("Image saved successfully")
            count += 1

    except Exception as e:
        print(f'Error processing image: {e}')

    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True)
   