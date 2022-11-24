import cv2 as cv2
import numpy as np

imagem1 = cv2.imread("Files/Boat1.jpg")
imagem2 = cv2.imread("Files/Boat2.jpg")

s1 = imagem1.shape
s2 = imagem2.shape

imagem_dual = np.zeros((s1[0], s1[1]+s2[1], s1[2]), dtype=np.uint8)
imagem_dual[:,0:s1[1],:] = imagem1
imagem_dual[:,s2[1]:,:] = imagem2

cv2.namedWindow("Imagem", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Imagem", imagem_dual)
cv2.waitKey(0)
