import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("odev1.jpg", 0)
plt.figure()
plt.imshow(img, cmap="gray")
plt.title("orijinal resim")


print(img.shape)  # (568,860)


# resmi boyutlandır
resize_img = cv2.resize(img, (int(img.shape[1]*4/5), int(img.shape[0]*4/5)))
plt.figure()
plt.imshow(resize_img, cmap="gray")
plt.title("boyutlandirilmis resim")


# yazı ekle
cv2.putText(img, "Kopek ve Kedi", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,255))
cv2.imshow("Metin", img)            



# orijinal resmin 50 threshold değeri üzerindekileri beyaz, altındakileri siyah yapma
_, thresh_img = cv2.threshold(img, thresh=50, maxval=255, type=cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.title("threshold")
plt.show()



# gaussian bulanıklaştırma
gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure()
plt.imshow(gb, cmap="gray")
plt.axis("off")
plt.title("bulanıklastirma")



# laplacian gradyan 
laplacian = cv2.Laplacian(img, ddepth=cv2.CV_64F)
cv2.imshow("laplacian", laplacian)


# histogram
img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(img_hist)