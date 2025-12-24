import cv2

img = cv2.imread("Lenna.png")
print("Resim boyutu: ", img.shape)
cv2.imshow("Orijinal", img)


# yeniden boyutlandır
imgResized = cv2.resize(img, (800,800))
print("Boyutlandirilmis resim", imgResized)
cv2.imshow("boyutlandirilmis resim", imgResized)

# kırp
imgCropped = img[:200, :300] # yükseklik, genişlik
cv2.imshow("kirpik resim", imgCropped)
