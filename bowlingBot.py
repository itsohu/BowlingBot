import pyautogui as pgui
import os
import time
path=os.getcwd()
#The above line gets the path so I can give it to the locate on screen function
path=path+"\\bowlingball2.PNG"
time.sleep(2);Boxcoord=pgui.locateOnScreen(path)
coord=pgui.center(Boxcoord)
coord2=(coord.x-1,coord.y-19)
time.sleep(2);pgui.moveTo((coord2[0]-2),(coord2[1]));time.sleep(5);pgui.dragTo((coord2[0]+3), (coord2[1]-305),0.2, button='left')
