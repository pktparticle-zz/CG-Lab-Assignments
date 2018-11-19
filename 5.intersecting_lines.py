#Assignment-5
#Draw two intersecting straight-lines [Orthogonal]

import numpy as np
import cv2 as cv
 
img = np.zeros((512,512,3), np.uint8)

cv.line(img,(250,0),(250,511),(255,0,0),3)
cv.line(img,(0,250),(511,250),(255,255,0),3)

 
cv.imshow('Intersecting Lines',img)
cv.waitKey(0)
    
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) 

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    print(x)
    print(y)

line_intersection(((250, 0), (250, 511)), ((0, 250), (511, 250)))
