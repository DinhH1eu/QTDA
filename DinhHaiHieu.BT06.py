import cv2
import numpy as np
import matplotlib.pyplot as plt

#Đọc ảnh màu lena.jpg vào biến ma trận Img. Hiển thị lên màn hình
img = cv2.imread(r"C:\Users\vunha\Downloads\lena.jpeg")
cv2.imshow("Picture", img)
cv2.waitKey(12000)

# Chuyển ảnh sang hệ HSV hiển thị kênh S
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
S = imgHSV[:, :, 2]
cv2.imshow("Kenh S", S)
cv2.waitKey(10000)

# Xác định mức xám lớn nhất của kênh S
maxS = np.amax(S)

# Xác định histogram của kênh V, Vẽ histogram
hist = cv2.calcHist([S], [0], None, [0, maxS], [0, 255])
plt.plot(hist)
plt.show()

# Làm trơn kênh S theo bộ lọc median với cửa sổ 7x7. Hiển thị kết quả làm trơn
ST = cv2.medianBlur(S, (7, 7))
cv2.imshow("Kenh S sau khi lam tron", ST)
cv2.waitKey(13000)