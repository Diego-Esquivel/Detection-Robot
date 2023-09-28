import cv2
import traitlets
import ipywidgets.widgets as widgets
import pandas as pd
from jetbot import *

class RCamera:
    camera= width=height=color_image=camera_link=frame = 0

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.camera = Camera.instance(width=self.width,height=self.height)
        self.color_image = widgets.Image(format='jpeg',width=self.width*2, height=self.height)
        self.camera_link = traitlets.dlink((self.camera,'value'),(self.color_image,'value'),transform=bgr8_to_jpeg)
    
    def getFrame(self):
        self.frame = self.color_image.value

        return self.frame
    def getDisplay(self):
        return self.color_image