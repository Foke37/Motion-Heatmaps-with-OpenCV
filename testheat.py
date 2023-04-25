import numpy as np
import cv2
import copy
import os
capture = cv2.VideoCapture('vtest.avi')
background_subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()
length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
# select just people
# for i in range(length):
#     ret, frame = capture.read()
#     fgmask = background_subtractor.apply(frame)
#     cv2.imshow('frame',fgmask)
#     cv2.imshow('frame2',frame)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
# capture.release()
# cv2.destroyAllWindows()
num_frames = 350
first_iteration_indicator = 1
for i in range(0, length):

    ret, frame = capture.read()

    # If first frame
    if first_iteration_indicator == 1:

        first_frame = copy.deepcopy(frame)
        height, width = frame.shape[:2]
        accum_image = np.zeros((height, width), np.uint8)
        first_iteration_indicator = 0
    else:
        filter = background_subtractor.apply(frame)  # remove the background

        threshold = 2
        maxValue = 2 
        ret, th1 = cv2.threshold(filter, threshold, maxValue, cv2.THRESH_BINARY)
        #show vdo in background
    

        accum_image = cv2.add(accum_image, th1)
        
        color_image_video = cv2.applyColorMap(accum_image, cv2.COLORMAP_JET)
        overlay  = cv2.addWeighted(frame, 0.3, color_image_video, 0.7, 0)
        cv2.imshow('frame2', overlay)
        cv2.imshow('frame', color_image_video)
        cv2.imshow('frame3', accum_image)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

capture.release()
cv2.destroyAllWindows()




# image_folder = 'image_data'
# video_name = 'video.avi'

# images = [img for img in os.listdir(image_folder)]
# images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape

# fourcc = cv2.VideoWriter_fourcc(*"MJPG")

# video = cv2.VideoWriter(video_name, fourcc, 30.0, (width, height))

# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))
       

# cv2.destroyAllWindows()
# video.release()

#         cv2.imshow('frame', color_image_video)
#         k = cv2.waitKey(30) & 0xff
#         if k == 27:
#             break

# capture.release()
# cv2.destroyAllWindows()
# # //////

# image_folder = 'image_data'
# images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
# fourcc = cv2.VideoWriter_fourcc(*'XVID')


# video = cv2.VideoWriter('output.avi', fourcc, 30.0, (width, height))
# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))

# cv2.destroyAllWindows()
# cv2.destroyAllWindows()
 

    