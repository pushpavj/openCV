import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


#To capture the images from the webcam
cap=cv2.VideoCapture(0) #0 means webcam

count=0
while True:
    #capture frame-by-frame
    _,frame=cap.read() #read the frame from the webcam

    #put tesxt on the frame image
    # print("frame shape",frame.shape)
    font=cv2.FONT_ITALIC
    text=cv2.putText(frame,'Hello World',(480//2,640//2),font,1,(100,45,55),3)
    cv2.imshow('text',text)
    cv2.waitKey(0)
    plt.show()
    # cv2.imshow('frame',frame)
    # cv2.waitKey(0) #wait for 1ms
    # plt.show() 
    count=count+1

    if count==5:
        break
    #even we can save teh captured frame to a file

cap.release()
cap=cv2.VideoCapture(0)
count=0
while True:
    #capture frame-by-frame
    _,frame=cap.read() #read the frame from the webcam
    sample_class="bottle"
    os.makedirs(f"samples/{sample_class}",exist_ok=True)
    cv2.waitKeyEx(60)
    cv2.imwrite(f"samples/{sample_class}/bottle_{count}.jpg",frame)
    count=count+1

    if count==20:
        break
    #even we can save teh captured frame to a file
    
cap.release()    


#To save this as video
cap=cv2.VideoCapture(0)
#define the codec and create VideoWriter object
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

count=0
while (cap.isOpened()):
    #capture frame-by-frame
    return1,frame=cap.read() #read the frame from the webcam
    if return1== True:
        output.write(frame) 
    
        count=count+1

        if count==20:
            break
    else: 
        break
    #even we can save teh captured frame to a file
    
cap.release()    

