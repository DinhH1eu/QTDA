
import cv2
import numpy as np

# Đọc ảnh lena.jpg vào biến ma trận Img
img = cv2.imread('D:/XuLyAnh/NhapMonXuLyAnh.08.Contour Detection, Filtering, and Drawing/images.jpg')



# Hiển thị ảnh gốc
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Chuyển ảnh sang không gian màu HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Hiển thị kênh V
v_channel = img_hsv[:,:,2]
cv2.imshow('V Channel', v_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Xác định chiều cao, chiều rộng của ảnh
height, width = img.shape[:2]
print('Chiều cao của ảnh:', height)
print('Chiều rộng của ảnh:', width)

# Tạo ảnh nhị phân theo ngưỡng Otsu
ret, img_otsu = cv2.threshold(v_channel, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Hiển thị ảnh nhị phân theo ngưỡng Otsu
cv2.imshow('Otsu Threshold Image', img_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Làm trơn ảnh bằng bộ lọc trung bình cộng với cửa sổ 5x5
img_blur = cv2.blur(img, (5, 5))

# Hiển thị ảnh đã làm trơn
cv2.imshow('Blurred Image', img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

