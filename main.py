import cv2
import numpy as np
import pyautogui
cap = cv2.VideoCapture(0)

green_lower = np.array([36, 25, 25])
green_upper = np.array([70, 255,255])

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

prev_y1 = 0
prev_y2 = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_1 = cv2.inRange(hsv, green_lower, green_upper)
    mask_2 = cv2.inRange(hsv, lower_red, upper_red)
    contours_1, hierarchy_1 = cv2.findContours(mask_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_2, hierarchy_2 = cv2.findContours(mask_2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c1 in contours_1:
        area_1 = cv2.contourArea(c1)
        if area_1 > 3000:
            x1, y1, w1, h1 = cv2.boundingRect(c1)
            cv2.rectangle(frame, (x1,y1), (x1+w1, y1+h1), (255, 255, 255), 2)
            if y1+20 < prev_y1:
                pyautogui.press('up')
            prev_y1 = y1

    for c2 in contours_2:
        area_2 = cv2.contourArea(c2)
        if area_2 > 4000:
            x2, y2, w2, h2 = cv2.boundingRect(c2)
            cv2.rectangle(frame, (x2,y2), (x2+w2, y2+h2), (0,0,0), 2)
            if y2 + 20 < prev_y1:
                pyautogui.press('down')
            prev_y1 = y2

    cv2.imshow("Controling Up and Down Key",frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()