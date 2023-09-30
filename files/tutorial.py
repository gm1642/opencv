# PS C:\Users\samkh> cd C:\Users\samkh\Documents\python\opencv  #changing where to create the environment
# PS C:\Users\samkh\Documents\python\opencv> virtualenv env_name    #to create the environment
# PS C:\Users\samkh\Documents\python\opencv> .\env1\Scripts\activate  # to activate the env
# (env1) PS C:\Users\samkh\Documents\python\opencv> pip install opencv-python  #to install opencvand python

import cv2
print(cv2.__version__)
# to open ediitor in terminal type python
#this is my repo for opencv projects
#default channel mode is BGR color mode
# image=cv2.imread('test.jpeg',cv2.IMREAD_COLOR)
# image=cv2.imread('test.jpeg',cv2.IMREAD_GRAYSCALE)
# #function to display
# cv2.imshow('test image',image)
# cv2.waitKey(5000)  #5000 milisec time
# #cv2.waitkey()  waits for the any key ffrom user to exit the dialog box
# # instancee of video capture
cap=cv2.VideoCapture(0) #0 for default video cam
opened=cap.isOpened()
# if(opened):
#  while(opened):
#         ret,frame=cap.read()
#         if(ret==True):
#             cv2.imshow('winname',frame)
#             if(cv2.waitKey(2)==27):
#                 break
#fourcc
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps=cap.get(cv2.CAP_PROP_FPS)
#video wwriter
out=cv2.VideoWriter('videoname1.avi',fourcc,fps,(int(width),int(height)))
print(height)



print(f"frames are {fps}")
#if(opened):
while(opened):
        ret,frame=cap.read()
        if(ret==True):
            cv2.imshow('winname',frame)
            out.write(frame)
            if(cv2.waitKey(2)==27):
                break
out.release()
cap.release()
cv2.destroyAllWindows()
