import cv2 as cv
import numpy as np

img = cv.imread("Resources/love.jpg")
kernel = np.ones((5,5),np.uint8) #ones, 5*5 ,unsigned int 8bits

# define in color spaces
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray,(7,7),0) #must be odd numbers
imgCanny = cv.Canny(img,150,200)  #edges
imgDilation =cv.dilate(imgCanny,kernel,iterations = 1)
imgEroded = cv.erode(imgDilation,kernel,iterations = 1)

cv.imshow("Gray Image",imgGray)
cv.imshow("Blur Image",imgBlur)
cv.imshow("Canny Image",imgCanny)
cv.imshow("Dilation Image",imgDilation)
cv.imshow("Eroded Image",imgEroded)

cv.waitKey(0)





