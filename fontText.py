import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('hello world')

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

# playing sounds
soundObj = pygame.mixer.Sound('beep1.ogg')
soundObj.play()
import time
time.sleep(1)
soundObj.stop()
'''
To begin playing the loaded sound file as the background music, call the
pygame.mixer.music.play(-1, 0.0) function. The -1 argument makes the
background music forever loop when it reaches the end of the sound file. If you set it to an integer
0 or larger, then the music will only loop that number of times instead of looping forever
'''
'''
code for playing music in the background
soundObj = pygame.mixer.Sound('beep1.ogg')
soundObj.play()

# loading and playing bg music
pygame.mixer.music.load(backgroundmusic.mp3)
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.stop()
'''


while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
