import cv2

cap = cv2.VideoCapture()

while True:
    if not cap.isOpened():
        cap.open(0)
    ret, image = cap.read()
    cv2.imshow("Image", image)
    cv2.waitKey(1)

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
