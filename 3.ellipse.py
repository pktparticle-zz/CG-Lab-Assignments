#Assignment-3
#Draw an ellipse.

import numpy as np
import cv2 as cv
 
img = np.zeros((512,512,3), np.uint8)

img = cv.ellipse(img, (256, 256), (150, 75), 0, 0, 360, (0,250,255), 2)
 
cv.imshow('Ellipse: Assignment-3',img)
cv.waitKey(0)