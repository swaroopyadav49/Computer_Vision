import cv2

## Reading images

img = cv2.imread("resources/lena.png")
print(img.shape)
cv2.imshow("Output", img)   # showing the image in console, without waitkey it will close immediately.
cv2.waitKey(0)  # waitkey is used to hold the image for infinite or longer time until any key is pressed.



## Reading videos

#cap = cv2.videoCapture("resources/elon.mp4")  # 0 means webcam, 1 means external camera