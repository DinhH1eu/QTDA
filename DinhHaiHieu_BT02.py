# Import required packages:
import cv2


# Load image using cv2.imread:
img = cv2.imread('pxfuel.jpg')
demension = img.shape
(h, w, c) = img.shape
print("Dimensions of the image - Height: {}, Width: {}, Channels: {}".format(h, w, c))

cv2.imshow('test',img)

# Get the value of the pixel (x=40, y=6):
(b, g, r) = img[40, 40]

# Print the values:
print("Pixel at (40,40) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
img[40, 40] = (0, 0, 0)
cv2.imshow('anhsua', img)
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
cv2.resize(img, dim ,30,30)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
