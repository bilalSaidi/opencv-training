import  cv2

# webcam
"""
video = cv2.VideoCapture(0)
while True :
    grabbed,frame= video.read()
    frame = cv2.resize(frame,(800,500))
    if cv2.waitKey(1) & 0xFF  == ord("q"):
        break
    cv2.imshow('vedio',frame)

video.release()
cv2.destroyAllWindows()
"""

# local video

"""
# Extract Information


localVideo = cv2.VideoCapture('Nature_Beautiful_short_video.mp4')
# fps => the number of image show by second
print("fps : ", int(localVideo.get(cv2.CAP_PROP_FPS)))
# number of frames in all the video
print("numberFrame: ", int(localVideo.get(cv2.CAP_PROP_FRAME_COUNT)))
# height of the frame
print("height: ", int(localVideo.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# width  of the frame
print("width: ", int(localVideo.get(cv2.CAP_PROP_FRAME_WIDTH)))
# duration of  thee video
print("duration: ", (int(localVideo.get(cv2.CAP_PROP_FRAME_COUNT)) // int(localVideo.get(cv2.CAP_PROP_FPS))))


# read the video
while localVideo.isOpened() :
    grabbed,frame = localVideo.read()
    if not grabbed :
        print("sorry :( can't read the video ")
    key = cv2.waitKey(1)
    # in case error in the video or the user press q end the video
    if(key & 0xFF) == ord("q") or not grabbed :
        break
    # when the user press 0 replay the video from the begining again
    if (key & 0xFF) == ord("0"):
        localVideo.set(cv2.CAP_PROP_POS_FRAMES, 0)

    cv2.imshow("localvideo",frame)
    cv2.waitKey(int(localVideo.get(cv2.CAP_PROP_FPS)))
"""




