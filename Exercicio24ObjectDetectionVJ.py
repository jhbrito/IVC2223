# Face Detection
import cv2
import os.path
import urllib.request as urllib_request


folder = "Files"
# if not os.path.isfile(os.path.join(folder, "lena.png")):
#     urllib_request.urlretrieve("https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png",
#                                os.path.join(folder, "lena.png"))
image = cv2.imread(os.path.join(folder, "lena.png"))

cap = cv2.VideoCapture(1)

# haarcascade_folder = 'venv/Lib/site-packages/cv2/data/'
haarcascade_folder = 'D:/envs/IVCenv/Library/etc/haarcascades/'
face_cascade = cv2.CascadeClassifier(haarcascade_folder + 'haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier(haarcascade_folder + 'haarcascade_frontalface_alt.xml')
# face_cascade = cv2.CascadeClassifier(haarcascade_folder + 'haarcascade_eye.xml')

faces = face_cascade.detectMultiScale(image)
print("Lena with {} faces detected".format(len(faces)))
image_faces = image.copy()
for (x, y, w, h) in faces:
    cv2.rectangle(image_faces, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Lena with {} faces detected".format(len(faces)), image_faces)
cv2.waitKey(0)
cv2.destroyAllWindows()

while True:
    # Read a new frame
    ret, frame = cap.read()
    if not ret:
        break

    faces = face_cascade.detectMultiScale(frame)
    image_faces = frame.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(image_faces, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Faces", image_faces)
    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

