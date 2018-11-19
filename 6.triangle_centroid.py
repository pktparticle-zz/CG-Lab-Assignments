#Assignment-6
# WAP to draw a triangle on the screen
import cv2
import numpy as np

image = np.ones((600, 600, 3), np.uint8) * 255

#Coordinates of the Vertices of the triangle
pt1 = (100, 400)
pt2 = (250, 200)
pt3 = (400, 400)

cv2.circle(image, pt1, 2, (0,0,255), -1)
cv2.circle(image, pt2, 2, (0,0,255), -1)
cv2.circle(image, pt3, 2, (0,0,255), -1)
triangle_cnt = np.array( [pt1, pt2, pt3] )

cv2.drawContours(image, [triangle_cnt], 0, (0,255,0), 4)
x1=(pt1[0]+pt2[0]+pt3[0])//3
x2=(pt1[1]+pt2[1]+pt3[1])//3

print('Centroid of the triangle is:',x1,x2)

#Centroid is (250,333.33)

cv2.circle(image, (x1, x2), 4, (255, 0, 255), -1) 
cv2.imshow("Triangle with Centroid", image)
cv2.waitKey()
