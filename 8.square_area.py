#Assignment-8
#WAP a program to draw a square and calculate the area
import numpy as np 
import cv2 
import math

img = np.zeros((400, 400, 3), dtype = "uint8") 

# Creating rectangle of eqaual side length 
cv2.rectangle(img, (50, 50), (250, 250), (0, 255, 0), 2) 

cv2.imshow('Square', img) 

#Diagonal Length = d
d=math.sqrt(200**2+200**2)
#Area = d*d/2
print ('Area of the Square: ',d*d/2)

# Allows us to see image 
# untill closed forcefully 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
