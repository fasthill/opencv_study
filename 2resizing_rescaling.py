import cv2 as cv

def rescale_frame(frame, scale=0.75):
    # work for images, videos & live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def change_resolution(width, height):
    # only work for Live Videos
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread('resources/Photos/cat_large.jpg')  # bigger image
cv.imshow('Cat', img)
img_resized = rescale_frame(img, scale=0.5)
cv.imshow('Cat Resized', img_resized)

cv.waitKey(0)

capture = cv.VideoCapture('resources/Videos/dog.mp4')  # in this, we use video file

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame, scale=0.5)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
