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
# image = cv2.imread(os.path.join(folder, "Sharbat_Gula.jpg"))

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = image / 255.

cv2.imshow("Image", image)

image_fft = np.fft.fft2(image)
image_fft_v = np.abs(image_fft) / np.mean(np.mean(np.abs(image_fft)))
cv2.imshow("Image FFT", image_fft_v)

image_fft_shift = np.fft.fftshift(image_fft)
image_fft_shift_v = np.abs(image_fft_shift) / np.mean(np.mean(np.abs(image_fft_shift)))
cv2.imshow("Image FFT shift", image_fft_shift_v)

tamanho = image_fft_shift.shape
H_lowpass = np.zeros(image_fft_shift.shape)
H_highpass = np.zeros(image_fft_shift.shape)

raio_maximo = tamanho[0]/2
raio = 0.25 * raio_maximo
centro_x = tamanho[1]/2
centro_y = tamanho[0]/2

for y in range(tamanho[0]):
    for x in range(tamanho[1]):
        d = np.sqrt((x-centro_x) ** 2 + (y-centro_y) ** 2)
        if d < raio:
            H_lowpass[y, x] = 1
            H_highpass[y, x] = 0
        else:
            H_lowpass[y, x] = 0
            H_highpass[y, x] = 1

cv2.imshow("Filtro FFT shift", H_lowpass)
# cv2.imshow("Filtro FFT shift", H_highpass)

image_fft_shift_filtered = image_fft_shift * H_lowpass
# image_fft_shift_filtered = image_fft_shift * H_highpass
image_fft_shift_filtered_v = np.abs(image_fft_shift_filtered) / np.mean(np.mean(np.abs(image_fft_shift_filtered)))

cv2.imshow("Filtro FFT shift filtered", image_fft_shift_filtered_v)
# a = b @ c

image_fft_shift_filtered_unshift = np.fft.ifftshift(image_fft_shift_filtered)
image_fft_shift_filtered_unshift_v = np.abs(image_fft_shift_filtered_unshift) /\
                                     np.mean(np.mean(np.abs(image_fft_shift_filtered_unshift)))
cv2.imshow("FFT shift filtered unshift", image_fft_shift_filtered_unshift_v)

image_fft_shift_filtered_unshift_ifft = np.fft.ifft2(image_fft_shift_filtered_unshift)
image_fft_shift_filtered_unshift_ifft = np.abs(image_fft_shift_filtered_unshift_ifft)
cv2.imshow("FFT shift filtered unshift ifft", image_fft_shift_filtered_unshift_ifft)


cv2.waitKey(0)
