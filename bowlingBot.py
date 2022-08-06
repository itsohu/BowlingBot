import pyautogui as pgui
import os
import time
path=os.getcwd()
#The above line gets the path so I can give it to the locate on screen function
path=path+"\\bowlingball.PNG"
Boxcoord=time.sleep(1);pgui.locateOnScreen(path)
coord=pgui.center(Boxcoord)
