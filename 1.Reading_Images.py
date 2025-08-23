import cv2

## Reading images

img = cv2.imread("resources/lena.png")

print(img.shape)
cv2.imshow("Output", img)   # showing the image in console, with out waitkey it will close immediately.
cv2.waitKey(0)

## Reading videos

cv2.videoCapture(0)  # 0 means webcam, 1 means external camera