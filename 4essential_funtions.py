import cv2 as cv

img = cv.imread('resources/Photos/cat.jpg')  # small image
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cat Gray', gray)

img = cv.imread('resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Park Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)  # use odd numbers only for blur
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges blur', canny)

# Dilating the image
dilated = cv.dilate(canny, (1, 1), iterations=2)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
