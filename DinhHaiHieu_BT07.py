import cv2
import numpy as np
import matplotlib.pyplot as plt

#1 Đọc ảnh màu lena.jpg vào biến ma trận Img. Hiển thị lên màn hình
img = cv2.imread(r"lena.png")
cv2.imshow("Picture", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#2 Chuyển ảnh sang hệ HSV ; Lấy kênh v và hiển thị
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
V = imgHSV[:, :, 2]
cv2.imshow("Kenh V", V)
cv2.waitKey(0)
cv2.destroyAllWindows()
#3 Xác định chiều cao, chiều rộng ảnh Img
h, w , c = img.shape
print("Chiều cao và rộng của ảnh - Height: {}, Width: {}".format(h, w))
#4 Tạo ảnh nhị phân theo ngưỡng Otsu thành ảnh ImgO.
# Chuyển ảnh màu sang ảnh grayscale
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng ngưỡng Otsu để tạo ảnh nhị phân
_, ImgO = cv2.threshold(gimg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Hiển thị ảnh nhị phân
cv2.imshow("Ảnh nhị phân Otsu", ImgO)
cv2.waitKey(0)
cv2.destroyAllWindows()
#5 Làm trơn ảnh theo bộ lọc trung bình cộng với cửa sổ 5x5 được ảnh ImgT, Hiển thị kết quả
img_blurred = cv2.blur(img, (5, 5))

# Hiển thị kết quả
cv2.imshow("Ảnh đã làm trơn", img_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
#6 Dùng Canny lấy biên ảnh, tạo thành ảnh nhị phân nền đen ImgB. Hiển thị kết quả
# Lấy biên ảnh bằng phương pháp Canny
edges = cv2.Canny(img, 100, 200)

# Tạo ảnh nhị phân với nền đen
ImgB = cv2.threshold(edges, 128, 255, cv2.THRESH_BINARY)[1]

# Hiển thị kết quả
cv2.imshow("Binary Image with Black Background", ImgB)
cv2.waitKey(0)
cv2.destroyAllWindows()
#7 Vẽ các đường contour lên trên ảnh gốc Img. Hiển thị lên màn hình
# Tìm các contour trong ảnh biên
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ các contour lên ảnh gốc
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Hiển thị ảnh gốc với các contour
cv2.imshow("Ảnh với Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()