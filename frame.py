
class Frame:
    frame = 0

    def __init__(self,frame):
        self.frame = frame
    
    def setFrame(self,camera):
        frame = camera.getFrame()
