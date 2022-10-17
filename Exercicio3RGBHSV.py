
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

# image_hsv = np.zeros(image.shape, dtype=np.float32)
# V = np.max(image, axis=2)
# image_hsv[:,:,2] = V/255.0
# Min = np.min(image, axis=2)
# S = (V - Min) / V
# S[V==0] = 0
# image_hsv[ :, :, 1] = S
# S[V==0] = 0
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_hsv_h = image_hsv.copy()
image_hsv_s = image_hsv.copy()
image_hsv_v = image_hsv.copy()

image_hsv_h[ :, :, 0] = 240.0
image_hsv_s[ :, :, 1] = image_hsv_s[ :, :, 1]/2.0
image_hsv_v[ :, :, 2] = image_hsv_v[ :, :, 2]/2.0

image_hsv_h_bgr = cv2.cvtColor(image_hsv_h, cv2.COLOR_HSV2BGR)
image_hsv_s_bgr = cv2.cvtColor(image_hsv_s, cv2.COLOR_HSV2BGR)
image_hsv_v_bgr = cv2.cvtColor(image_hsv_v, cv2.COLOR_HSV2BGR)

cv2.imshow("Image", image)
cv2.imshow("Image HSV H BGR", image_hsv_h_bgr)
cv2.imshow("Image HSV S BGR", image_hsv_s_bgr)
cv2.imshow("Image HSV V BGR", image_hsv_v_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
