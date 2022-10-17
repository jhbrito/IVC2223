# Demo with a few examples of using OpenCV functions and UI
# uses lena: https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png

import numpy as np
import cv2
import os.path
import urllib.request as urllib_request

print("OpenCV Version:", cv2.__version__)


# Opening and Viewing an Image
folder = "Files"
if not os.path.isfile(os.path.join(folder, "lena.png")):
    urllib_request.urlretrieve("https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png",
                               os.path.join(folder, "lena.png"))

def ivc_rgb_remove_red(src):
    isr = src.copy()
    isr[:, :, 2] = 0
    return isr


def ivc_rgb_remove_green(src):
    isg = src.copy()
    isg[:, :, 1] = 0
    return isg


def ivc_rgb_remove_blue(src):
    isb = src.copy()
    isb[:, :, 0] = 0
    return isb


image = cv2.imread(os.path.join(folder, "lena.png"))

image_sem_red=ivc_rgb_remove_red(image)
image_sem_green = ivc_rgb_remove_green(image)
image_sem_blue = ivc_rgb_remove_blue(image)

cv2.imshow("Image", image)
cv2.imshow("Image sem red", image_sem_red)
cv2.imshow("Image sem green", image_sem_green)
cv2.imshow("Image sem blue", image_sem_blue)

R = image[:,:, 2]
G = image[:,:, 1]
B = image[:,:, 0]
image_grayscale = R * 0.299 + G * 0.587 + B * 0.114
# image_grayscale = image_grayscale / 255.0
image_grayscale = np.round(image_grayscale).astype(np.uint8)
cv2.imshow("Image grayscale", image_grayscale)

cv2.waitKey(0)
cv2.destroyAllWindows()

