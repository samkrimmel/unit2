#Sam Krimmel
#2/2/18
#coloredSquare.py - displays a colored square

from ggame import *
from random import randint
num = randint(1,3)
blue = Color(0x0000ff,1)
red = Color(0xff0000,1)
yellow = Color(0xffff00,1)

if num==1:
    line = LineStyle(3,yellow)
    rectangle = RectangleAsset(250,250,line,red)
    Sprite(rectangle)
    myApp = App()
    myApp.run()
elif num==2:
    line = LineStyle(3,red)
    rectangle = RectangleAsset(250,250,line,blue)
    Sprite(rectangle)
    myApp = App()
    myApp.run()
else:
    line = LineStyle(3,blue)
    rectangle = RectangleAsset(250,250,line,yellow)
    Sprite(rectangle)
    myApp = App()
    myApp.run()


