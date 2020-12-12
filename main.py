# %%
from cv2 import cv2 as cv   # NOTE: imported as such to disable linting errors due to C headers
from cv2.data import haarcascades   # Location of cascades used for object detection
import os
# %%

def faceDetect(frame, face_cascade=cv.CascadeClassifier()):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        frame = cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),4)

    #-- Detect faces
    cv.namedWindow('img', cv.WINDOW_KEEPRATIO)
    cv.imshow('img', frame)

img = cv.imread("./Selfie_pic.jpeg")
# %%

# Location of face adaboost for frontal face
face_cascade_loc = os.path.join(haarcascades, "haarcascade_frontalface_alt_tree.xml")
face_cascade = cv.CascadeClassifier()
if not face_cascade.load(cv.samples.findFile(face_cascade_loc)):
    print('--(!)Error loading face cascade')
    exit(0)

# MAIN function
while True:
    exit_key = ord('q')
    # waitKey returns an int, hence using bitwise AND
    if cv.waitKey(exit_key) & 255 == exit_key:
        cv.destroyAllWindows()
        break
    faceDetect(img, face_cascade)

# %%
