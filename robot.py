from jetbot import *
class Robit:
    robot = 0

    def __init__(self):
        self.robot = Robot()

    def stop(self):
        self.robot.stop

    def turn_left(self):
        self.robot.set_motors(-.75,.75)
    def turn_right(self):
        self.robot.set_motors(.75,-.75)