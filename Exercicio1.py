import numpy as np
import cv2


im = np.ndarray((576, 704), dtype=np.uint8)
cv2.imshow("Im", im)

im1 = 255 * np.ones((576, 704), dtype="uint8")
cv2.imshow("Im1", im1)

im0 = np.zeros((576, 704), dtype="uint8")
cv2.imshow("Im0", im0)

cv2.waitKey(0)
