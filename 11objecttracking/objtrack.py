import cv2
import numpy as np

#default called trackbar function
def setValues(x):
    print("")

#creating the trackbars needed for adjusting the marker colour
cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue","Color detectors",153,180,setValues)
cv2.createTrackbar("Upper Saturation","Color detectors",255,255,setValues)
cv2.createTrackbar("Upper Value","Color detectors",255,255,setValues)
cv2.createTrackbar("Lower Hue","Color detectors",64,180,setValues)
cv2.createTrackbar("Lower Saturation","Color detectors",72,255,setValues)
cv2.createTrackbar("Lower Value","Color detectors",49,255,setValues)

#Captue the input from wb cam
def get_frame(cap,scaling_factor):
    ret,frame=cap.read()
    #Resize the frame
    frame=cv2.resize(frame,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
    return frame

if __name__=='__main__':
    cap=cv2.VideoCapture(0)
    scaling_factor=0.9
    #Iterate untill the user press esc
    while True:
        frame=get_frame(cap,scaling_factor)
        #convert to hsv color space
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        u_hue=cv2.getTrackbarPos("Upper Hue","Color detectors")
        u_saturation=cv2.getTrackbarPos("Upper Saturation","Color detectors")
        u_value=cv2.getTrackbarPos("Upper Value","Color detectors" )
        l_hue=cv2.getTrackbarPos("Lower Hue","Color detectors" )
        l_saturation=cv2.getTrackbarPos("Lower Saturation","Color detectors")
        l_value=cv2.getTrackbarPos("Lower Value","Color detectors")

        #define color range in the hsv color space
        Upper_hsv=np.array([u_hue,u_saturation,u_value])
        Lower_hsv=np.array([l_hue,l_saturation,l_value])
        #threshold the HSV image to get only selected color
        mask=cv2.inRange(hsv,Lower_hsv,Upper_hsv)
        # Bitwise-AND amsk and original image
        res=cv2.bitwise_and(frame,frame,mask=mask)
        res=cv2.medianBlur(res,5)
        cv2.imshow("Original image",frame)
        cv2.imshow("Color Detector",res)
        #check is the use has pressed esc key
        c=cv2.waitKey(5)
        if c==27:
            break
    cv2.destroyAllWindows()
