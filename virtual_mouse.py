import cv2
import numpy as np
import autopy
from cvzone.HandTrackingModule import HandDetector

wCam, hCam = 640, 480
frameR = 100
smoothening = 7
wScreen, hScreen = autopy.screen.size()

pX, pY = 0, 0
cX, cY = 0, 0
is_clicking = False

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = HandDetector(detectionCon=0.7, maxHands=1)

print(f"Ekran Çözünürlüğü: {wScreen}x{hScreen}")

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

    if hands:
        hand = hands[0]
        lmList = hand['lmList']
        x1, y1 = lmList[8][0], lmList[8][1]
        fingers = detector.fingersUp(hand)

        if fingers[1] == 1 and sum(fingers) == 1:
            is_clicking = False
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScreen))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScreen))
            cX = pX + (x3 - pX) / smoothening
            cY = pY + (y3 - pY) / smoothening
            autopy.mouse.move(cX, cY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            pX, pY = cX, cY

        elif fingers[1] == 1 and fingers[2] == 1 and sum(fingers) == 2:
            if not is_clicking:
                autopy.mouse.click()
                print("Tıklandı! (İşaret ve Orta Parmak)")
                is_clicking = True
            cv2.circle(img, (x1, y1), 15, (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "TIKLAMA HAZIR", (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        else:
            is_clicking = False
            cv2.putText(img, "Diger Mod", (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    else:
        is_clicking = False

    cv2.imshow("Virtual Mouse - Kamera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
