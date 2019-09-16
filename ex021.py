#Tocar um arquivo .mp3
import pygame
music = 'You Need to Calm Down (Acoustic Version)'
artist = 'Taylor Swift'
pygame.mixer.init()
pygame.mixer.music.load('calmdown.mp3')
pygame.mixer.music.play()
print('Você está escutando {} por {}.'.format(music, artist))
input()
pygame.event.wait()

