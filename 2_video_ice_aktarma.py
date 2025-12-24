import cv2
import time

video_name = "MOT17-04-DPM.mp4"

cap = cv2.VideoCapture(video_name)

print("Genişlik: ", cap.get(3))
print("Yükseklik", cap.get(4))





# video açılmadığında hata yazdır
if cap.isOpened() == False:
    print("Hata")


while True:
    ret, frame = cap.read()  # ret=return, frame=resim


    if ret == True: # return doğruysa 
    
        time.sleep(0.01)  # kullanmazsak çok hızlı akar.
        cv2.imshow("Video", frame) # resimleri görselleştir
        
    else: break
    
    if cv2.waitKey(1) & 0xFF == ord("q"): # q ya tıklayınca kapat
        break
    
    
cap.release()  # durdur
cv2.destroyAllWindows() # tüm açık pencereleri kapat


  