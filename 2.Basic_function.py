
import cv2
import numpy as np


## Reading images

# img = cv2.imread("resources/lena.png")
# print(img.shape)
# cv2.imshow("Output", img) 

## converting into a gray Image.

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_gray.shape)
# cv2.imshow("Output Gray", img_gray)
# cv2.waitKey(0)

## converting to a blur Image.

# img_blur = cv2.GaussianBlur(img, (7,7), 0)
# cv2.imshow("Output Blur", img_blur)
# cv2.waitKey(0)


### converting to a blur Image.
# img = cv2.imread("resources/lena.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
# print("Color_img Shape:", img.shape)
# print("img_gray Shape:", img_gray.shape)
# cv2.imshow("Output Color", img)
# cv2.imshow("Output Gray", img_gray)
# cv2.imshow("Output Blur", img_blur)
# cv2.waitKey(0)


### converting to a cannyImage.
img = cv2.imread("resources/lena.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
img_canny = cv2.Canny(img_blur, 80, 80)

print("Color_img Shape:", img.shape)
print("img_gray Shape:", img_gray.shape)
cv2.imshow("Output Color", img)
cv2.imshow("Output Gray", img_gray)
cv2.imshow("Output Blur", img_blur)
cv2.imshow("Output Canny", img_canny)
cv2.waitKey(0)