import pyautogui as pgui
#import os
import time
#path=os.getcwd()
#The above line gets the path so I can give it to the locate on screen function
#path=path+"\\bowlingball2.PNG"
#A note for myself:To customize anaconda prompt type "prompt [text]" to reset type "prompt"
i=1
success=True
listOfImgPath=["bowlingball0.PNG","bowlingball1.PNG","bowlingball2.PNG","bowlingball3.PNG","bowlingball4.PNG","bowlingball5.PNG"]
try:
	time.sleep(1);Boxcoord=pgui.locateOnScreen(".\\"+listOfImgPath[0])
	coord=pgui.center(Boxcoord)
	coord2=(coord.x-1,coord.y-19)
	time.sleep(0.5);pgui.moveTo((coord2[0]-2),(coord2[1]));time.sleep(5);pgui.dragTo((coord2[0]+3), (coord2[1]-305),0.2, button='left')
	print("SUCCESS")
except:
	print("trying try number:"+str(1))
	success=False

#While loop looping through the image file paths so if first image not found on screen try others,
#While loop stops as soon as image found on screen by break statement or we have tried all images
if success==False:
	#print("line25")
	while (i<(len(listOfImgPath))):
		#print("line27")
		if(i==(len(listOfImgPath)-1)):
			print("last try")
		try:
			#print("line30")
			time.sleep(1);Boxcoord=pgui.locateOnScreen(".\\"+listOfImgPath[i])
			coord=pgui.center(Boxcoord)
			coord2=(coord.x-1,coord.y-19)
			time.sleep(0.5);pgui.moveTo((coord2[0]-2),(coord2[1]));time.sleep(5);pgui.dragTo((coord2[0]+3), (coord2[1]-305),0.2, button='left')
			print("SUCCESS")
			break
		except:
			#print("line37")
			i=i+1
			print("trying try number:"+str(i))