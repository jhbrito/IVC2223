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

image = cv2.imread(os.path.join(folder, "lena.png"))
cv2.imshow("Image", image)
cv2.waitKey(0)

image_new = image/255.0
cv2.imshow("Image New", image_new)
cv2.waitKey(0)



cv2.destroyAllWindows()

