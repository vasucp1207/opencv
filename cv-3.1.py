import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Sometimes, cap may not have initialized the capture. In that case, this code shows an error.
#  You can check whether it is initialized or not by the method cap.isOpened()
if not cap.isOpened():
    print('cannot opne camera')
    exit()

while True:
    # Capture frame by frame
    # cap.read() returns a bool (True/False)
    ret, frame = cap.read()

    # if frame is read then ret = true
    if not ret:
        print("can't receives frames....")
        break

    # convert into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    # display the resulting frame
    cv2.imshow('frame', gray)
    if(cv2.waitKey(1) == ord('q')):
        break

# release the camera, when everything is done
cap.release()
cv2.destroyAllWindows()
