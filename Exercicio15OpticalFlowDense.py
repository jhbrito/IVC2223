import numpy as np
import cv2 as cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.',
                    default=os.path.join('Files', 'vtest.avi'))
args = parser.parse_args()

cap = cv2.VideoCapture(args.input)
ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame2 = cap.read()
    if not ret:
        print('No frames grabbed!')
        break
    cv2.imshow('frame', frame2)

    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prev=prvs, next=next, flow=None,
                                        pyr_scale=0.25,  # 0.5,
                                        levels=1,  # 3,
                                        winsize=5,  # 15,
                                        iterations=1,  # 3,
                                        poly_n=5,
                                        poly_sigma=1.2,
                                        flags=0)
    # flow_abs = np.abs(flow[:, :, 0]) + np.abs(flow[:, :, 1])
    # flow_abs_norm = cv2.normalize(flow_abs, None, 0.0, 1.0, cv2.NORM_MINMAX)
    # cv2.imshow('flow_abs_norm', flow_abs_norm)
    flow_norm = np.sqrt(flow[:, :, 0] ** 2 + flow[:, :, 1] ** 2)
    flow_norm_norm = cv2.normalize(flow_norm, None, 0.0, 1.0, cv2.NORM_MINMAX)
    cv2.imshow('flow_norm_norm', flow_norm_norm)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    prvs = next

cv2.destroyAllWindows()
