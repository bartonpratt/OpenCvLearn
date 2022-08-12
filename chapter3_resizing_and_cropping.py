import cv2
import numpy

img = cv2.imread("Resources/gogeta.png")
print(img.shape) #size of image in order(height, width, channels bgr)

imgResize = cv2.resize(img,(300,200)) #width before height
print(imgResize.shape)

imgCropped = img[0:200,200:500] #height before width

cv2.imshow("image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image cropped",imgCropped)

cv2.waitKey(0)