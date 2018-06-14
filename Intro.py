import pygame, sys
from pygame.loca;s import*

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,  300))
pygame.display.set-caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


    
