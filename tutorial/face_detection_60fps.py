from unittest import result
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("./yaghi.mp4")
pTime = 0
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)                            # by default (0.5) and you can change it for accuracy
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    # print(results)

    if results.detections:
        for id , detection in enumerate(results.detections):
            print(id, detection)
            # print(detection.score)                                           # its subvalue of detection
            # print(detection.location_data.relative_bounding_box)             #its show how get sub data's
            # mpDraw.draw_detection(img, detection)                            #draw face area and key points on show images
            
            # draw rectangle on face with our own formula
            bboxC = detection.location_data.relative_bounding_box
            ih , iw , ic = img.shape
            bbox = int (bboxC.xmin * iw), int(bboxC.ymin * ih), int (bboxC.width * iw) , int(bboxC.height * ih) 
            cv2.rectangle(img, bbox , (0,0,255),2)
            cv2.putText(img, f'{int(detection.score[0] * 100)} %', (int(bboxC.xmin * iw),int ((bboxC.ymin * ih)- 20)), cv2.FONT_HERSHEY_COMPLEX, 1 , (255,255,0), 1)

    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img , f'FPS : {int (fps)}' ,(10,30), cv2.FONT_HERSHEY_COMPLEX , .5 , (255,100,0) , 1 )
    cv2.imshow("image",img)
    cv2.waitKey(10)