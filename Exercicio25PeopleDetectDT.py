import cv2 as cv2
import argparse
import os


def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh


def draw_detections(img, rects, thickness=1, color=(0, 255, 0)):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), color, thickness)


parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.',
                    default=os.path.join('Files', 'vtest.avi'))
args = parser.parse_args()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# cap = cv2.VideoCapture(args.input)
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

while True:
    # Read a new frame
    ret, frame = cap.read()
    if not ret:
        break

    found, _w = hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)
    found_filtered = []
    for ri, r in enumerate(found):
        for qi, q in enumerate(found):
            if ri != qi and inside(r, q):
                break
        else:
            found_filtered.append(r)
    draw_detections(frame, found, thickness=5, color=(0, 0, 255))
    draw_detections(frame, found_filtered, thickness=1, color=(0, 255, 0))
    print('%d (%d) found' % (len(found_filtered), len(found)))
    cv2.imshow('img', frame)

    # Exit if ESC pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
