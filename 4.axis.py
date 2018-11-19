#Assignment-4
#Draw X-Y-Z Coordinate axis system

import numpy as np
import cv2 as cv

img=np.zeros((512,512,3),np.uint8)

cv.line(img,(150,150),(150,350),(255,0,0),3)
cv.line(img,(150,350),(350,350),(0,255,0),3)
cv.line(img,(150,350),(60,450),(0,0,255),3)


cv.imshow('3-D Coordinate Axis',img)
cv.waitKey(0)
