import pygame, sys
from pygame.locals import*

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbol.tff', 32)
textSurfaceObj = fontObj.render('Hello World!', True, GREEN, BLUE)
textRectObg = textSurfaceObj.get_rect()
textRectObg.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObg)
    for event in pygame.event.get:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
