import cv2 as cv2
import numpy as np
import os

# load da imagem
folder = "Files"
img = cv2.imread(os.path.join(folder, "moedas.jpg"))
print(img.shape)
cv2.namedWindow("Moedas")
cv2.imshow("Moedas", img)
# cv2.waitKey()

# threshold da imagem
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_otsu = cv2.threshold(img_gray, 0, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("Otsu", img_otsu*255)
print(img_otsu.shape)
# cv2.waitKey()

# imagem segmentada = imagem original x mascara
imagem_segmentada = img_gray * (img_otsu)
cv2.imshow("Imagem segmentada", imagem_segmentada)
print(imagem_segmentada.shape)


contours, hierarchy = cv2.findContours(img_otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = np.zeros(img_gray.shape, dtype=np.uint8)
# cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]])
# cv2.drawContours(image=img_contours, contours=contours, contourIdx=-1, color=(255, 255, 255))

# cv2.drawContours(image=img_contours, contours=contours, contourIdx=-1, color=1, thickness=-1)
cv2.drawContours(image=img_contours, contours=contours, contourIdx=-1, color=1, thickness=-1, hierarchy=hierarchy, maxLevel=1)

cv2.imshow("Contours", img_contours*255)
print(len(contours))

imagem_segmentada = img_gray * (img_contours)
cv2.imshow("Imagem segmentada contours", imagem_segmentada)

img_contour0 = np.zeros(img.shape, dtype=np.uint8)
cv2.drawContours(image=img_contour0, contours=contours, contourIdx=0, color=(0, 0, 255), thickness=-1)
cv2.imshow("Contour 0", img_contour0)

cnt = contours[0]
M = cv2.moments(cnt)
print(M)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print("cx:", cx, ";  cy:", cy)
area = cv2.contourArea(cnt)
print("area:", area)
perimeter = cv2.arcLength(cnt, True)
print("perimeter:", perimeter)

cv2.waitKey()
