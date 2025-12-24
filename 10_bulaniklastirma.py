import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")


# blurring (detayı azaltır, gürültüyü engeller)
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("orijinal") 
plt.show()



# ortalama bulanıklaştırma yöntemi
dst2 = cv2.blur(img, ksize=(3,3))
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("ortalama blur")



# gaussian blur 
gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gaussian blur")



# medyan blur
mb = cv2.medianBlur(img, ksize=3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("medyan blur")


def gaussianNoise(image):  # gürültüye sahip resim
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var ** 0.5
    
    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy



# içe aktar normalize et (0 ile 1 arası)
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("orijinal")
plt.show()



gaussianNoisyImage = gaussianNoise(img)  # gürültülü resim
plt.figure()
plt.imshow(gaussianNoisyImage)
plt.axis("off")
plt.title("Gauss Noisy")
plt.show()



# gürültüyü azalt
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize=(3,3), sigmaX=7)
plt.figure()
plt.imshow(gb2)
plt.axis("off")
plt.title("with gauss blur")
 


# median blur
def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004

    noisy = np.copy(image)

    # SALT (beyaz noktalar)
    num_salt = int(np.ceil(amount * row * col * s_vs_p))
    coords = (
        np.random.randint(0, row, num_salt),
        np.random.randint(0, col, num_salt)
    )
    noisy[coords[0], coords[1], :] = 1

    # PEPPER (siyah noktalar)
    num_pepper = int(np.ceil(amount * row * col * (1 - s_vs_p)))
    coords = (
        np.random.randint(0, row, num_pepper),
        np.random.randint(0, col, num_pepper)
    )
    noisy[coords[0], coords[1], :] = 0

    return noisy


spImage = saltPepperNoise(img)
plt.figure()
plt.imshow(spImage)
plt.axis("off")
plt.title("SP Image")
plt.show()

mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize=3)
plt.figure()
plt.imshow(mb2)
plt.axis("off")
plt.title("with medyan blur")


     