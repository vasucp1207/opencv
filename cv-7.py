import numpy as np
import cv2

img = cv2.resize(cv2.imread('begin/soccer_practice.png', 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('begin/shoe.png', 0), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    res = cv2.matchTemplate(img2, template, method)
    # cv.matchTemplate(), It simply slides the template image over the input image (as in 2D convolution)
    # and compares the template and patch of input image under the template image
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
