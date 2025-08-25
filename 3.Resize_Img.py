import cv2
import numpy as np

## Resizing images

# img = cv2.imread("resources/lambo.png")
# print(img.shape)
# 
# resized_img = cv2.resize(img, (300,200))
# print(resized_img.shape)
# 
# cv2.imshow("Output", img)
# cv2.imshow("Output_resized", resized_img)
# cv2.waitKey(0)

## cropping images

img = cv2.imread("resources/lambo.png")
print(img.shape)
crop_img = img[0:200, 200:450]

print(crop_img.shape)
cv2.imshow("Output", img)
cv2.imshow("Crop_Output", crop_img)
cv2.waitKey(0)

