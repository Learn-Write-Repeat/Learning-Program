import cv2
import numpy as np
import mediapipe
import wx
from pynput.mouse import Controller, Button
import handtrackermodule as htm
import time

mouse = Controller()
app = wx.App(False)
wScr, hScr = wx.GetDisplaySize() 
wCam, hCam = 640, 480
frameR = 150
dampner = 3
mLocOld = np.array([0,0])
mLocNew = np.array([0,0])
clicked = 0
##############

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detector = htm.handDetector(maxHands=1)
ptime = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)
    cv2.rectangle(img,(frameR, frameR), (wCam-frameR, hCam-frameR), (0,0,255),2)
    if len(lmList)!=0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]
        
        fingers = detector.fingersUp()

        if fingers[1]==1 and fingers[0]==0:
            if clicked==1:
                clicked=0
                mouse.release(Button.left)
            if x1 in range(frameR,wCam-frameR) and y1 in range(frameR,hCam-frameR):
                cv2.circle(img, (x1,y1), 7, (255,255,255), cv2.FILLED)
                cv2.rectangle(img,(frameR, frameR), (wCam-frameR, hCam-frameR), (0,255,0),2)
                mLocNew = mLocOld+((x1,y1)-mLocOld)/dampner
                X = np.interp(mLocNew[0],(frameR,wCam-frameR),(0,wScr))
                Y = np.interp(mLocNew[1],(frameR,hCam-frameR),(0,hScr))
                mouse.position=(X, Y)
                if mouse.position != (X,Y):
                    pass
                mLocOld = mLocNew

        elif fingers[1]==1 and fingers[0]==1:
            cv2.rectangle(img,(frameR, frameR), (wCam-frameR, hCam-frameR), (255,0,0),2)
            if clicked==0:
                # if 
                clicked=1
                mouse.press(Button.left)
            else:
                cv2.circle(img, (x1,y1), 7, (255,255,255), cv2.FILLED)
                mLocNew = mLocOld+((x1,y1)-mLocOld)/dampner
                X = np.interp(mLocNew[0],(frameR,wCam-frameR),(0,wScr))
                Y = np.interp(mLocNew[1],(frameR,hCam-frameR),(0,hScr))
                if X in range(frameR,wCam-frameR) and Y in range(frameR,hCam-frameR):
                    cv2.rectangle(img,(frameR, frameR), (wCam-frameR, hCam-frameR), (0,255,0),2)
                    mouse.position = X, Y
                    if mouse.position != (X,Y):
                        pass
                mLocOld = mLocNew
    


    ctime = time.time()
    fps = 1//(ctime-ptime)
    ptime = ctime
    cv2.putText(img, f'FPS : {int(fps)}', (10,30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0,255), 3)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
