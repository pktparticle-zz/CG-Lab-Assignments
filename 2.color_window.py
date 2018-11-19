#Assignment-2
#Write a program to change color of window/screen.
import numpy as np
import cv2

img = np.zeros((500,700,3), np.uint8)
cv2.rectangle(img,(250,125),(500,250),(0,255,0),cv2.FILLED)
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.imshow('Different coloured window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
