#!/usr/bin/env python
import freenect
import cv, cv2
import numpy
import frame_convert

cv2.namedWindow('Test')
#cv.NamedWindow('Video')
print('Press ESC in window to stop')


def get_depth():
    return frame_convert.pretty_depth_cv(freenect.sync_get_depth()[0])


def get_video():
    return frame_convert.video_cv(freenect.sync_get_video()[0])


while 1:
    #cv.ShowImage('Test', get_depth())
    #cv.ShowImage('Video', get_video())
    (depth, boogers) = freenect.sync_get_depth();
    (image,_) = freenect.sync_get_video();
    #(_,dest) = cv2.threshold(depth.astype(numpy.uint8),100,255,cv2.THRESH_BINARY_INV)
    #image = image.astype(numpy.float32);
    #final = cv2.bitwise_and(image,image,mask = dest.astype('B'));

    depth = depth.astype(numpy.uint8)

    #print("depth[",len(depth),"][",len(depth[0]),"]:", depth[100][100])
    #print("image[",len(image),"][",len(image[0]),"][",len(image[0][0]),"[:", image[100][100])

    #Fuck it we will do this the hard way!
    #for i in xrange(depth.shape[0]):
    #    for j in xrange(depth.shape[1]):
    #        if depth.item(i,j) < 255:
    #           image.itemset(i,j,0,0)
#		image.itemset(i,j,1,0)
#		image.itemset(i,j,2,0)


    cv2.imshow('Test', depth)
    if cv.WaitKey(10) == 27:
        break
