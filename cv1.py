import cv2

img = cv2.imread('begin/open.png', 0)
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('new_img.jpg', img)

# -1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# 0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

cv2.imshow('Image', img)         
cv2.waitKey(0)
cv2.distroyAllWindows()
