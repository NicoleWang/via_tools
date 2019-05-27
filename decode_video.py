import sys, os, string
import cv2
import numpy as np

video_path = sys.argv[1]
start = string.atoi(sys.argv[2])
out_dir = sys.argv[3]
prefix = video_path.split('/')[-1].split('.')[0]
vidcap = cv2.VideoCapture(video_path)
success,image = vidcap.read()
cnt = -1
if success:
    print("Open %s Success~"%video_path)
else:
    print("Open %s Fail!"%video_path)
    sys.exit(0)
while success:
    cnt += 1
    success, frame = vidcap.read()
    if  success == False:
        continue
    print cnt
    if cnt % 2 != 0:
        continue

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    #frame = cv2.transpose(frame)
    #frame = cv2.flip(frame, 0)
    #hei, wid, _ = frame.shape
    #pading = int((wid - hei)/2)
    #border=cv2.copyMakeBorder(frame, top=pading, bottom=pading, left=0, right=0, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
    #cv2.imshow('frame',frame)
    #cv2.waitKey()
    #continue
    imname = "%s_%04d.jpg"%(prefix, cnt+start)
    image_path = os.path.join(out_dir, imname)
    cv2.imwrite(image_path, frame)
    #cv2.imwrite(image_path, frame)

