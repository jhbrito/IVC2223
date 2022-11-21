# video from http://backgroundmodelschallenge.eu/#evaluation
import cv2 as cv2
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.',
                    default=os.path.join('Files', 'vtest.avi'))
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).',
                    default='KNN')
args = parser.parse_args()

#create Background Subtractor objects
if args.algo == 'MOG2':
    backSub = cv2.createBackgroundSubtractorMOG2()
    N = backSub.getNMixtures()
    print("using {} Gaussians".format(N))
    # backSub.setNMixtures(7)
    # N = backSub.getNMixtures()
    # print("using {} Gaussians".format(N))
else:
    backSub = cv2.createBackgroundSubtractorKNN()
    k = backSub.getkNNSamples()
    print("using K = {}".format(k))
    # backSub.setkNNSamples(4)
    # k = backSub.getkNNSamples()
    # print("using K = {}".format(k))
capture = cv2.VideoCapture(args.input)
if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    # update the background model
    fgMask = backSub.apply(frame)

    # get the frame number and write it on the current frame
    cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv2.putText(frame, str(capture.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
               cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))

    #show the current frame and the fg masks
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgMask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
