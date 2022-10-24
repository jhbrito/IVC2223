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

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_3x3 = (1/9.) * np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])
filtro_passaalto = (1/6.) * np.array([[0, -1, 0],
                                      [-1, 4, -1],
                                      [0, -1, 0]])
filtro_passaaltoB = (1/9.) * np.array([[-1, -1, -1],
                                       [-1,  8, -1],
                                       [-1, -1, -1]])
filtro_passaaltoC = (1/16.) * np.array([[-1, -2, -1],
                                        [-2, 12, -2],
                                        [-1, -2, -1]])
image_filtered = cv2.filter2D(image_gray, -1, kernel=kernel_3x3)
image_filtered2 = cv2.filter2D(image_gray, -1, kernel=filtro_passaalto)
image_filtered2B = cv2.filter2D(image_gray, -1, kernel=filtro_passaaltoB)
image_filtered2C = cv2.filter2D(image_gray, -1, kernel=filtro_passaaltoC)

cv2.imshow("Image", image_gray)
cv2.imshow("Resultado Filtro Media", image_filtered)
cv2.imshow("Resultado Filtro Passa Alto", 3*image_filtered2)
cv2.imshow("Resultado Filtro Passa Alto B", image_filtered2B)
cv2.imshow("Resultado Filtro Passa Alto C", 3*image_filtered2C)

image_filtered_blur = cv2.blur(image_gray, (3, 3))
cv2.imshow("Resultado Blur", image_filtered_blur)

image_filtered_gaussian = cv2.GaussianBlur(image_gray, (5,5), 0)
cv2.imshow("Resultado Gaussian Blur", image_filtered_gaussian)

image_filtered_median = cv2.medianBlur(image_gray, 5)
cv2.imshow("Resultado Median Blur", image_filtered_median)

cv2.waitKey(0)
