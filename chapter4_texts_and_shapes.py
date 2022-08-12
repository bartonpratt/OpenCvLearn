import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img.shape) #check dimension
# img[:] = 255,0,0 #color whole matrix/image

                    #width of matrix[1], height[0]
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),5) #start, end, color, thickness
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) #fill shape
cv2.circle(img,(450,50),30,(255,255,0),5)  #center point,radius,color
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1) #origin,font,scale,color, thickness

cv2.imshow("Image",img)

cv2.waitKey(0)