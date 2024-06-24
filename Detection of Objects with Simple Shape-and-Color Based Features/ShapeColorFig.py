import numpy as np
import cv2
import time
img = cv2.imread(r"D:\Study\Mini-project\Detection of Objects with Simple Shape-and-Color Based Features\IMGA.jpg")
cv2.imshow("Original Image", img)
font = cv2.FONT_HERSHEY_COMPLEX
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
L = np.array([0, 150, 255],np.uint8)                #ORANGE
H = np.array([25, 255, 255],np.uint8)
#L=np.array([26, 150, 255],np.uint8)                 #YELLOW
#H=np.array([35, 255, 255],np.uint8)
#L=np.array([36, 150, 255],np.uint8)                 #GREEN
#H=np.array([75, 255, 255],np.uint8)
#L=np.array([76, 150, 255],np.uint8)                 #LIGHT BLUE
#H=np.array([95, 255, 255],np.uint8)
#L=np.array([96, 150, 255],np.uint8)                 #DARK BLUE
#H=np.array([130, 255, 255],np.uint8)
#L=np.array([131, 150, 255],np.uint8)                #PURPLE
#H=np.array([155, 255, 255],np.uint8)
#L=np.array([156, 150, 255],np.uint8)                #RED PURPLE
#H=np.array([170, 255, 255],np.uint8)
#L=np.array([171, 150, 255],np.uint8)                #RED
#H=np.array([180, 255, 255],np.uint8)
text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime()) 
mask = cv2.inRange(hsv, L, H) 

cv2.imshow("Yellow Shapes", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()