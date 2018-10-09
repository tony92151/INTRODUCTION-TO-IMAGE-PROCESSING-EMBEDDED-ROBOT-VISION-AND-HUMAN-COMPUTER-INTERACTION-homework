import numpy as np
import cv2

img = cv2.imread('color.png')
cv2.imshow('dog',img)
#print(len(img[0,0,:]))

img2 = img
img2[:,:,[0,1,2]] = img2[:,:,[1,2,0]]


cv2.imshow('dog2',img2)

cv2.waitKey(0)
