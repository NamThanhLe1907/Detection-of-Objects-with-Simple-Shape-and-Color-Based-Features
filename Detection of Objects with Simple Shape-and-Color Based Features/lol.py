import numpy as np
import cv2

img = cv2.imread(r"D:\Study\Mini-project\Detection of Objects with Simple Shape-and-Color Based Features\IMGA.jpg")
cv2.imshow("Original Image", img)
font = cv2.FONT_HERSHEY_COMPLEX
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
#L = np.array([0, 150, 0],np.uint8)                #ORANGE
#H = np.array([25, 255, 200],np.uint8)
#L=np.array([26, 150, 0],np.uint8)                 #YELLOW
#H=np.array([35, 255, 200],np.uint8)
L=np.array([36, 150, 0],np.uint8)                 #GREEN
H=np.array([75, 255, 200],np.uint8)
#L=np.array([76, 150, 0],np.uint8)                 #LIGHT BLUE
#H=np.array([95, 255, 200],np.uint8)
#L=np.array([96, 150, 0,np.uint8)                 #DARK BLUE
#H=np.array([130, 255, 200],np.uint8)
#L=np.array([131, 150, 0],np.uint8)                #PURPLE
#H=np.array([155, 255, 200],np.uint8)
#L=np.array([156, 150, 0],np.uint8)                #RED PURPLE
#H=np.array([170, 255, 200],np.uint8)
#L=np.array([171, 150, 0],np.uint8)                #RED
#H=np.array([180, 255, 255],np.uint8)

mask = cv2.inRange(hsv, L, H) 


imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, 1), 1)
    cv2.drawContours(mask, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv2.putText(mask, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    elif len(approx) == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(mask, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
        else:
          cv2.putText(mask, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    elif len(approx) == 5:
        cv2.putText(mask, "Pentagon", (x-20, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    elif len(approx) == 6:
        cv2.putText(mask, "Hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    else:
        cv2.putText(mask, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))


cv2.imshow("Red Shapes", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()