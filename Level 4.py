for x in [0, 1, 2, 3, 4]:
    for y in ['a', 'b', 'c']:
        print(x, y)

import rando, pygame, sys
from pygame.locals import*

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boces for pairs of matches.'
XMARGIN = int((WINDOWWIDTH -(BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
XMARGIN = int((WINDOWWIDTH -(BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

GRAY = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE = (255, 255, 255)
