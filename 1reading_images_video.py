import cv2 as cv

img = cv.imread('resources/Photos/cat.jpg') # small image
# img = cv.imread(ImagePATH + 'cat_large.jpg') # bigger image

cv.imshow('Cat', img)

cv.waitKey(0)
# reading videos

# NUM = 0 # webcam 1: second camera, 2: third camera you can define accordingly
# capture = cv.VideoCapture(NUM)

capture = cv.VideoCapture('resources/Videos/dog.mp4') # in this, we use video file

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
