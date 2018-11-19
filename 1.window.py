#Assignment-1
'''Write a program to demonstrate window management with OpenGL/OpenCV and 
   display 400*300 window at position (50,100) relative to top left corner'''
import cv2
import numpy as np
img = np.zeros((255,255,3),np.uint8)
cv2.imshow("Window",img)
cv2.moveWindow('Window',50,100)
cv2.waitKey(0)
cv2.destroyWindow('Window')
