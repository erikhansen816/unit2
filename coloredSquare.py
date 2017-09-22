#Erik Hansen
#9/18/2017
#coloredSquare.py - 

from ggame import *
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
yellow = Color(0xFFFF00,1)
linegreen = LineStyle(3,green)
greenrectangle = RectangleAsset(100,100,linegreen,green)
lineblue = LineStyle(3,blue)
bluerectangle = RectangleAsset(100,100,lineblue,blue)

Sprite(greenrectangle)
Sprite(bluerectangle)
myApp = App()
myApp.run()