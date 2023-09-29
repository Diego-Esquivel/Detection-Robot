#Import function library path
from IPython.display import display
from uuid import uuid1
import inspect
import ctypes
import os
from robot import *
from camera import *
from frame import *
import threading
import time
from red_object import *
import math

myobject = RedObject()
mycamera = RCamera(256,256)

myrobot = Robit()
def jetbot_motion_center_x():
    #red object detected the robot move
    if myobject.pos_x_px >= 148:
        #red object detected on right of camera rotate right
        myrobot.turn_right()
    elif myobject.pos_x_px <= 108:
        #red object detected on left of camera rotate left
        myrobot.turn_left()
    else :
        #red object on camera center stop moving straight
        myrobot.stop()
        
    time.sleep(.01)



def findminrow():
    xpxcm = 34.5929693
    if myframe.color_y > 127:
        yobj = myframe.color_y - 127.
        xcm = xpxcm * 128./yobj
        print("Real time distance (cm)" + str(xcm))
        print("Pixels below center: ",yobj)
        myobject.pos_z = xcm


myframe = Frame(mycamera,myobject.color_lower,myobject.color_upper)
display(mycamera.color_image)
def qcheck(thread2,thread3):
    if(thread2.is_alive() == False and thread3.is_alive() == False): ## Think i can do something here where I put this in a thread and .join() this thread instead of thread4. This way this thread is always getting reset and thread4 gets reset within it
        if myframe.status == 1:
            thread2 = threading.Thread(target=jetbot_motion_center_x)
            thread3 = threading.Thread(target=findminrow)
            myobject.pos_x_px = myframe.color_x
            myobject.pos_y_px = myframe.color_y
            thread2.start()
            thread3.start()

def dothecamthing():
        newframe = mycamera.getDisplay()
        myframe.setFrame(mycamera.camera.value,myobject.color_lower,myobject.color_upper)


thread2 = threading.Thread()
thread3 = threading.Thread()
thread4 = threading.Thread()