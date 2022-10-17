import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

folder = "Files"

image = cv2.imread(os.path.join(folder, "baboon.png"))
# image = cv2.imread(os.path.join(folder, "cao.png"))
# image = cv2.imread(os.path.join(folder, "lena.png"))
# image = cv2.imread(os.path.join(folder, "moedas.jpg"))
# image = cv2.imread(os.path.join(folder, "PET-Body-02.jpg"))
# image = cv2.imread(os.path.join(folder, "rockefeller-center-1932-RGB.png"))
# image = cv2.imread(os.path.join(folder, "Sharbat_Gula.jpg"))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def ivc_gray_histogram(src):
    h = np.zeros((256,), dtype=np.uint16)
    for i in range(256):
        i_n = np.sum(src==i)
        h[i] = i_n
    return h


# histograma = ivc_gray_histogram(image_gray)
histograma = cv2.calcHist([image_gray], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

pdf = histograma/(image_gray.shape[0]*image_gray.shape[1])

cdf = np.zeros(pdf.shape, dtype=np.float64)
cdf[0] = pdf[0]
for i in range(1, 256):
    cdf[i] = pdf[i] + cdf[i-1]

image_gray_equalized = np.zeros(image_gray.shape, dtype=np.uint8)
cdfmin = cdf[0]

for y in range(image_gray.shape[0]):
    for x in range(image_gray.shape[1]):
        image_gray_equalized[y, x] = ((cdf[image_gray[y, x]] - cdfmin)/ (1 - cdfmin) ) * (255)

histograma_equalized = cv2.calcHist([image_gray_equalized], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
pdf_equalized = histograma_equalized/(image_gray_equalized.shape[0]*image_gray_equalized.shape[1])

cdf_equalized = np.zeros(pdf_equalized.shape, dtype=np.float64)
cdf_equalized[0] = pdf_equalized[0]
for i in range(1, 256):
    cdf_equalized[i] = pdf_equalized[i] + cdf_equalized[i-1]

cv2.imshow("Image", image)
cv2.imshow("Image Gray", image_gray)

plt.subplot(2, 4, 1)
plt.imshow(image_gray, cmap='gray')
plt.title("Image")
plt.axis("off")

plt.subplot(2, 4, 2)
plt.plot(histograma)

plt.subplot(2, 4, 3)
plt.plot(pdf)

plt.subplot(2, 4, 4)
plt.plot(cdf)

plt.subplot(2, 4, 5)
plt.imshow(image_gray_equalized, cmap='gray')
plt.title("Image equalized")
plt.axis("off")

plt.subplot(2, 4, 6)
plt.plot(histograma_equalized)

plt.subplot(2, 4, 7)
plt.plot(pdf_equalized)

plt.subplot(2, 4, 8)
plt.plot(cdf_equalized)

plt.show()
cv2.waitKey(0)
