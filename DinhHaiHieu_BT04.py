# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 22:10:16 2024

@author: DinhHieu
"""

# Import required packages:
import cv2
import numpy as np
import os



# Load image using cv2.imread:
img = cv2.imread('pxfuel.jpg')

cv2.imshow('test',img)
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

img= cv2.putText(img,'OpenCV',(15, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors['red'], 2,
            cv2.LINE_AA)
cv2.imshow('cochu', img)
luutru = r'C:\Users\DinhHieu\Desktop'
os.chdir(luutru)
# Print the list of files in the directory before saving the image
print("Before saving")   
print(os.listdir(luutru))
# Save the image with the filename "cat.jpg"
cv2.imwrite('anhcochu.jpg', img)    
# Print the list of files in the directory after saving the image
print("After saving")  
print(os.listdir(luutru))
cv2.waitKey(0)
cv2.destroyAllWindows()
