import numpy as np
import cv2
import matplotlib.pyplot as plt


img=cv2.imread('car.jpg')
cv2.imshow('img',img)
cv2.waitKey(0)
#cv2.distroyAllWindows() # when you press q it will close all windows
plt.show()

gray_img=cv2.imread('car.jpg',0)
cv2.imshow('gray_img',gray_img)
cv2.waitKey(0)
#cv2.distroyAllWindows() # when you press q it will close all windows
plt.show()

#to save the image
cv2.imwrite('carcolur.jpg',img)
cv2.imwrite('cargray.jpg',gray_img)

# plt.imshow(img) #cv2 in bgr format and matplotlib in rgb format
# plt.show()

#To draw any shapes on the image
rectangle=cv2.rectangle(img,(100,0),(200,100),(0,255,0),2)
#(img,(100,0),(200,0),(0,255,0),2)
#top left corner(x,y), bottom right corner(x,y),pen color(b,g,r), line thickness

cv2.imshow('rectangle',rectangle)
cv2.waitKey(0)
plt.show()


#draw a circle on the image

circle=cv2.circle(img,(100,100),50,(255,0,0),3)
cv2.imshow('circle',circle)
cv2.waitKey(0)
plt.show()

cv2.imshow('img',img)
cv2.waitKey(0)
plt.show()

#to put text on the image
font=cv2.FONT_ITALIC
text=cv2.putText(img,'Hello World',(100,100),font,1,(100,45,55),3)
cv2.imshow('text',text)
cv2.waitKey(0)
plt.show()