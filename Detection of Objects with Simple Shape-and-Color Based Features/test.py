import cv2
import numpy as np

# Load the image
img = cv2.imread(r"D:\Study\Mini-project\Detection of Objects with Simple Shape-and-Color Based Features\IMGA.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
L=np.array([36, 150, 0],np.uint8)                 #GREEN
H=np.array([75, 255, 200],np.uint8)
mask = cv2.inRange(hsv, L, H)
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to obtain a binary image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find the contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
approx = cv2.approxPolyDP(contours, 0.01* cv2.arcLength(contours, 1), 1)
cv2.drawContours(mask, [approx], 0, (0, 0, 0), 5)
x = approx.ravel()[0]
y = approx.ravel()[1] - 5
# Display the image
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
