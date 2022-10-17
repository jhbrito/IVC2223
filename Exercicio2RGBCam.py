import cv2

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


cap = cv2.VideoCapture()

while True:
    if not cap.isOpened():
        cap.open(0)
    ret, image = cap.read()
    cv2.imshow("Image", image)

    image_sem_red = ivc_rgb_remove_red(image)
    image_sem_green = ivc_rgb_remove_green(image)
    image_sem_blue = ivc_rgb_remove_blue(image)

    cv2.imshow("Image sem red", image_sem_red)
    cv2.imshow("Image sem green", image_sem_green)
    cv2.imshow("Image sem blue", image_sem_blue)

    cv2.waitKey(1)

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
