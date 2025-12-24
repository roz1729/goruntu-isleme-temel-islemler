import cv2

# içe aktarma
img = cv2.imread("vesikalik.png", 0)


# görselleştir
cv2.imshow("ilk resim", img)


k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("vesikalik_gray.png", img)
    cv2.destroyAllWindows()