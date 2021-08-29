import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # uint8 : image
cv.imshow('Blank', blank)

img = cv.imread('resources/Photos/cat.jpg')  # small image
cv.imshow('Cat', img)

# 1. paint the image a certain color
blank[:, :, :] = 0, 255, 0  # green
blank[100:200, 100:300] = 0, 0, 255
blank[300:450, 300:450] = 255, 0, 0
cv.imshow('Green', blank)

# 2. Draw a Rectangle
blank[:] = 20, 20, 20
cv.rectangle(blank, (0, 0), (250, 400), (255, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

blank[:] = 50, 50, 50
cv.rectangle(blank, (0, 0), (250, 400), (100, 255, 0), thickness=cv.FILLED)  # == thickness=-1
cv.imshow('Rectangle Filled', blank)

blank[:] = 70, 70, 70
cv.rectangle(blank, (0, 0), (blank.shape[1]//3, int(blank.shape[0]/1.5)), (255, 100, 0), thickness=cv.FILLED)
# == thickness=-1
cv.imshow('Rectangle Filled with relative size', blank)

# 3 Draw a circle
blank[:] = 100, 100, 100
cv.circle(blank, (250, 250), 100, (30, 200, 30), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
blank[:] = 130, 130, 70
cv.line(blank, (300, 300), (450, 450), (105, 100, 0), thickness=4)
cv.imshow('line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (100, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=3)
cv.imshow('line', blank)
#
cv.putText(img, 'My Cat', (100, 250), cv.FONT_HERSHEY_PLAIN, 1.0, (10, 100, 0), thickness=3)
cv.imshow('Cat', img)

cv.waitKey(0)
