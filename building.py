"""Building Class"""

## Bulidngs are created here. 
## The buildings are black.
## Buildings are created with a random width, height and location.

import pygame
import random

class Building():
    def __init__(self, location, width, height):
        self.location = location
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.location, (self.width, self.height))
        
        self.image = pygame.Surface(self.rect.size)
        # self.image.set_colorkey(pygame.Color('black'))
        self.color = pygame.Color('red')
        
        pygame.draw.rect(self.image, self.color, self.rect)
        