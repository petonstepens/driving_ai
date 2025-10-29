import pygame
import numpy as np

#init window
pygame.init()
screen = pygame.display.set_mode((800,600))

#define cube verticies
vertices = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
])

#loop
running = True
while running:
  screen.fill((0,0,0))
  pygame.display.flip()
 

  




