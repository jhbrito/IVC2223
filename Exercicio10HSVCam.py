import cv2

cv2.namedWindow("Image")
h_min = 90/2  # 210/2  # 90/2  #
h_max = 150/2  # 270/2  # 150/2  #
s_min = 128

cap = cv2.VideoCapture(0)

while True:
    if not cap.isOpened():
        cap.open(0)
    ret, image = cap.read()
    image = image[:,::-1,:]
    cv2.imshow("Image", image)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ret, above_h_min = cv2.threshold(image_hsv[:,:,0], h_min, 1, cv2.THRESH_BINARY)
    ret, below_h_max = cv2.threshold(image_hsv[:,:,0], h_max, 1, cv2.THRESH_BINARY_INV)

    within_h_min_and_h_max = above_h_min * below_h_max

    ret, above_s_min = cv2.threshold(image_hsv[:,:,1], s_min, 1, cv2.THRESH_BINARY)
    within_h_min_and_h_max_and_s_min = within_h_min_and_h_max * above_s_min

    # cv2.imshow("H min", above_h_min*255)
    # cv2.imshow("H max", below_h_max*255)
    cv2.imshow("Within H min and H max and S min", within_h_min_and_h_max_and_s_min*255)

    image_show = image.copy()
    image_show[:,:,0] = image_show[:,:,0] * within_h_min_and_h_max
    image_show[:,:,1] = image_show[:,:,1] * within_h_min_and_h_max
    image_show[:,:,2] = image_show[:,:,2] * within_h_min_and_h_max

    # cv2.imshow("Object", image_show)

    cv2.waitKey(1)

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
