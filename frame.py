import cv2
import pandas as pd
from jetbot import *
class Frame:
    frame = 0
    image = 0
    def __init__(self,camera,color_lower,color_upper):
        self.frame = camera.camera.value
        self.newmask = 0
        self.status = 0
        self.image = camera.color_image

    
    def setFrame(self,frame,color_lower,color_upper):
        self.frame = frame
    #######################################################################
        #add gaussian blur. this has yet to improve performace but it came stock
        self.frame=cv2.GaussianBlur(self.frame,(1,1),0)  
        mask=cv2.inRange(self.frame,color_lower,color_upper)
        # print the contents of the ndarray mask which stores 255 if a pixel is within the range specified or 0 if the pixel is not
        """print(mask)"""
        # search mask for the lowest row where there is an element with 255 as its value
        maskdf = pd.DataFrame(mask)
        self.newmask = 1
        mask=cv2.erode(mask,None,iterations=2)
        mask=cv2.dilate(mask,None,iterations=2)
        mask=cv2.GaussianBlur(mask,(1,1),0)     
        cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

        if len(cnts)>0:
            cnt = max (cnts,key=cv2.contourArea)
            (self.color_x,self.color_y),color_radius=cv2.minEnclosingCircle(cnt)
            if color_radius > 2:
                # Mark the detected color with circle
                #left is x=0; right is x = 255
                #high is y=0; low is y = 255

                cv2.circle(self.frame,(int(self.color_x),int(self.color_y)),int(color_radius),(255,0,255),2)
                self.color_y += int(color_radius)
                self.status = 1

                # Mark the detected color with rectangle
                """rot_rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rot_rect)
                box = np.int0(box)
                cv2.drawContours(frame,[box],0,(0,0,0,),2)"""
                #end mark detected color with rectangle
        else:
            self.status = 0
        self.image.value = bgr8_to_jpeg(self.frame)
        # Real-time return of image data for display

    #######################################################################