from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceMeshModule import FaceMeshDetector
import cv2
from cvzone.SerialModule import SerialObject

wCam, hCam= 1680,1050
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detector = HandDetector(detectionCon=0.8, maxHands=2)
detector2 = FaceMeshDetector(maxFaces=2)
arduino = SerialObject("COM4")


while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    #img, faces = detector2.findFaceMesh(img)
    # hands = detector.findHands(img, draw=False)  # without draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        if fingers1.count(1) == 0:
            arduino.sendData([0])
        elif  fingers1.count(1) == 1:
            arduino.sendData([1])
        elif  fingers1.count(1) == 2:
            arduino.sendData([2])
        elif  fingers1.count(1) == 3:
            arduino.sendData([3])
        elif  fingers1.count(1) == 4:
            arduino.sendData([4])
        elif  fingers1.count(1) == 5:
            arduino.sendData([5])
        else:
            arduino.sendData([0])
        
        totalFingers = fingers1.count(1)
        cv2.rectangle(img, (1020, 50), (1160, 230), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (1045, 200), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)
        print(fingers1.count(1))

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)
            cv2.putText(img, str(int(fingers2.count(1))), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

            # Find Distance between two Landmarks. Could be same hand or different hands
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
            #length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
    # Display
    
    cv2.imshow("Image", img)
    key=cv2.waitKey(25)   
    if key == ord('n') or key == ord('p'):
        break 