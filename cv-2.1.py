import cv2
import numpy

img = cv2.imread('opencv.png')

# You can access a pixel value by its row and column coordinates. For BGR image, it returns an array of Blue, Green, Red values

px = img[100, 100]
print(px)
# [157 166 200]

# accessing only blue pixel
blue = img[100, 100, 0]
print(blue)
# 157

# You can modify the pixel values the same way
img[100, 100] = [255, 255, 255]
print(img[100, 100])
# [255, 255, 255]

# Numpy is an optimized library for fast array calculations. So simply accessing each and every pixel value and modifying it will be very slow and it is discouraged
# The above method is normally used for selecting a region of an array, say the first 5 rows and last 3 columns. For individual pixel access, the Numpy array methods, array.item() and array.itemset() are considered better

# accessing RED value
img.item(100, 100, 2)
# 59

# modifying RED value
img.itemset((100, 100, 2), 100)
img.item(100, 100, 2)
# 100

print(img.shape)
# (rows, cols, channels(if img is color)) ->(342, 548, 3)

print(img.size)
# total no of pixels -> something like 23456


# ROI(region of image)
# Sometimes, you will have to play with certain regions of images. For eye detection in images,
# first face detection is done over the entire image. When a face is obtained, 
# we select the face region alone and search for eyes inside it instead of searching the whole image
# ROI is again obtained using Numpy indexing
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball


# adding and subtracting of images

img1 = cv2.imread('input1.jpg')
img2 = cv2.imread('input2.jpg')

weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.5)
# cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
# Remember, both images should be of equal size and depth in subtraction also

cv2.imshow('Weighted Image', weightedSum)

if cv2.waitKey(0) == 'q':
    cv2.destroyAllWindows()


# weightSub = cv2.subtract(img1, img2)
# cv2.imshow('Weighted Image', weightedSub)

# if cv2.waitKey(0) == 'q':
#     cv2.destroyAllWindows() 
