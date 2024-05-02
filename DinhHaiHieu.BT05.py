import cv2
#Đọc ảnh màu lena.jpg vào biến ma trận Img. Hiển thị lên màn hình
img = cv2.imread(r"C:\Users\vunha\Downloads\lena.jpeg")
cv2.imshow("Original Picture", img)

#Xác định chiều cao, chiều rộng ảnh ImgX
imgX = img.shape[:2]
print("Chiều Cao: ", imgX[0])
print("Chiều rộng: ", imgX[1])

#Tạo ra ảnh mới ImgS từ ảnh Img bằng cách đổi size có độ cao 256 rộng 256. Hiển thị
imgS = cv2.resize(img, dsize=(256, 256))

#Chuyển ảnh sáng hệ HSV được ImgHSV. Hiển thị kênh S.
imgHSV = cv2.cvtColor(imgS, cv2.COLOR_BGR2HSV)
cv2.imshow("S-Channel", imgHSV[:, :, 1])

#Làm trơn kênh V Biến đổi ngược lại về RGB được ImgS. Hiển thị kết quả
kernel = cv2.GaussianBlur(imgHSV[:, :, 2], (5, 5), 0)
imgS = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR)
cv2.imshow("Results", imgS)

cv2.waitKey(15000)