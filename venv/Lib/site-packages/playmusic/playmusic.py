print("This is the source code")
import time
import tkinter
import math
import pygame
import tkinter
import tkinter.filedialog
import time
def music():
	print("python 3.5 and pygame must be loaded on system as well as the python3-tk package")
	print("Browse to file. File must be a .ogg file in order for playmusic library to work")
	file = tkinter.filedialog.askopenfilename()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	volume = input("Type volume amount (must be float)")
	pygame.mixer.music.set_volume(float(volume))
	pygame.mixer.music.play()
	time.sleep(30*60)
def ad():
	while(1):
		print("\n I am going to \n bug \s you")
		time.sleep(0.1)
		while(1):
			bugmusic = tkinter.filedialog.askopenfilename()
			pygame.mixer.init()
			pygame.mixer.music.set_volume(1.0)

