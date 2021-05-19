import pygame, sys
from pygame.locals import *

pygame.init()
'''
Colors     RGB(values)
Aqua ( 0, 255, 255)
Black ( 0, 0, 0)
Blue ( 0, 0, 255)
Fuchsia (255, 0, 255)
Gray (128, 128, 128)
Green ( 0, 128, 0)
Lime ( 0, 255, 0)
Maroon (128, 0, 0)
Navy Blue ( 0, 0, 128)
Olive (128, 128, 0)
Purple (128, 0, 128)
Red (255, 0, 0)
Silver (192, 192, 192)
Teal ( 0, 128, 128)
White (255, 255, 255)
Yellow (255, 255, 0)
'''

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

while True: # main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
print('hello is working!')
