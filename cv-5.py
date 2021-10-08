import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower bound, upper bound of a color in reference to hsv
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # any color in this range will be display

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # mask is return us an new image which has only the blue pixels existing
    # mask is an array of 0's and 1's only, 1->matched(white), 0->not-matched(black)

    # bitwise operators required hsv images
    result = cv2.bitwise_and(frame, frame, mask=mask)
    # result only keeps the pixels of our mask image(mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
