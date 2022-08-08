# BowlingBot
This program is a bot I built using python, for a Bowling game available at https://www.crazygames.com/game/the-bowling-club and on facebook games as well.
## Steps
0. Install python's pyautogui using pip or conda from the cmd or anaconda terminal respectively.
1. Clone this repo to your PC and extract the zip file. (Note the picture shall be used to get the coordinates.)(Note:I'm using os import so you wont have to find path of any file) I made this for windows, I'm not sure if directory paths are different in other operating systems.
2. Go to the website and start the game.
3. Run the script by typing in terminal the following text "python bowlingBot.py", and as soon as you run it go back to the game within 7 seconds (I mean the ball of the game must be visible while the script is running.) Since I shall be using the clicking function to move the ball assuming you are on the game.

## How does the script work?
I am using pyautogui to control the cursor, as well as find the image of the ball and use it to move the cursor on the ball.
(Note:Currently the program is having detecting the first time the ball appears, so try to do play the first ball yourself and run the program for the rest of the turns.)
