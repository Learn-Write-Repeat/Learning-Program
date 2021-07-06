import numpy as np
import cv2
import time
import mediapipe as mp
import math


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectConf=0.5, trackConf=0.5 ):
        self.mode = mode 
        self.maxHands = maxHands
        self.detectConf = detectConf
        self.trackConf = trackConf
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectConf, self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4,8,12,6,20]


    def findHands(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img


    def findPosition(self, img, draw=True, handNo=0):
        self.lmList = []
        xlist = []
        ylist = []
        bbox = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                xlist.append(cx)
                ylist.append(cy)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,255), cv2.FILLED)
            xmin, xmax = min(xlist), max(xlist)
            ymin, ymax = min(ylist), max(ylist)
            bbox = xmin, ymin, xmax, ymax
            if draw:
                cv2.rectangle(img, (xmin-20, ymin-20), (xmax+20, ymax+20), (0,255,0), 2)
        return self.lmList, bbox


    def displayFeatures(self, img):
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    cv2.circle(img, (cx,cy), 15, (0,0,255), cv2.FILLED)
                    cv2.putText(img, str(id), (cx-5,cy+5), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0),2)
        return img

    def fingersUp(self):
        finger = []
        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0]-1][1]:
            finger.append(1)
        else:
            finger.append(0) 
        # Fingers
        for id in range(1,5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]:
                finger.append(1)
            else:
                finger.append(0)
        # print(finger)
        # total = finger.count(1)
        return finger


    def findDistance(self, p1,p2,img, draw=True, r=15, t=3):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        c1, c2 = (x1+x2)//2, (y1+y2)//2
        if draw:
            cv2.circle(img, (x1,y1), 10, (255,0,255),cv2.FILLED )
            cv2.circle(img, (x2,y2), 10, (255,0,255),cv2.FILLED )
            cv2.line(img, (x1,y1),(x2,y2), (255,0,255), 3)
            cv2.circle(img,(c1,c2), 10, (255,0,255),cv2.FILLED)
            length = int(math.hypot(x2-x1,y2-y1))
        
        return length, img, [x1,y1,x2,y2,c1,c2]


def main(cam_add=0):
    ptime=0
    ctime=0
    cap = cv2.VideoCapture(cam_add)
    detector = handDetector()

    while True:
        success, img = cap.read()
        if cam_add==0:
            img = cv2.flip(img,1)
        img = detector.findHands(img, True)
        lmList, bbox = detector.findPosition(img, True, 0)
        # if len(lmList) != 0:
        #     print(lmList[4])
        # img = detector.displayFeatures(img)
        ctime = time.time()
        fps = 1//(ctime-ptime)
        ptime = ctime

        cv2.putText(img, f"FPS : {fps}", (10,30), cv2.FONT_HERSHEY_PLAIN, 1.5 , (255,0,255),3)

        cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':
    # main("http://192.168.0.103:8080/video")
    main()