import cv2
import random

img = cv2.imread('begin/opencv.png', 0)

tag = img[500:700, 600:900, -1]
img[100:300, 650:950] = tag

# print(img)
# print(img.shape)
# print(img[0])
# print(img[34][43])


# Change first 100 rows to random pixels
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.distroyAllWindows()
