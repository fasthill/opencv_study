import cv2 as cv
import numpy as np

img = cv.imread('resources/Photos/park.jpg') # small image
cv.imshow('Park', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#-x --> Left, -y --> Up, x --> Right, y --> Down

translated = translate(img, 100, 300)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)

    return cv.warpAffine(img, rotMat, dimentions)

rotated = rotate(img, 30) # CCW 30 degrees
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -60) # CW 60 degrees
cv.imshow('Rotated-rotated', rotated_rotated) # Check the picture shape

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
resized = cv.resize(img, (0,0), fx=1, fy=0.7, interpolation=cv.INTER_LINEAR)
# cv.INTER_CUBIC: cubic is slower but high quality, 확대할 경우 사용
# cv.INTER_LINEAR: 축소, 확대 일반적으로 사용
# cv.INTER_AREA: 축소시 일반적으로 사용
cv.imshow('Resize', resized)

# Flipping
flip = cv.flip(img, 0) # 0: x-axis 으로 대칭, 1 : y-axis, -1, x,y axis
cv.imshow('Flip', flip)

# Cropping
cropped = img[100:300, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)