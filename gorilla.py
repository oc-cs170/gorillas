"""Gorilla class"""

## Both gorilla images are created here.
## Upadate controls when to change the gorilla image from standing to throwin.

import pygame
import random

class Gorilla(pygame.sprite.Sprite):
    def __init__(self, buildings, player = 1):
        self.buildings = buildings
        self.sheet = pygame.image.load("donkeykong_enemies_sheet.png").convert_alpha()

        # The three gorilla images
        self.throw_left = self.sheet.subsurface(pygame.Rect(48, 56, 48, 32))
        self.stand = self.sheet.subsurface(pygame.Rect(104, 56, 40, 32))
        self.throw_right = self.sheet.subsurface(pygame.Rect(152, 56, 48, 32))

       
        # This is where the gorilla stands
        self.rect = pygame.Rect(0, 0, 40, 32)
        self.image = self.stand
        
        # Gorilla image for player1 is randomly placed on the left of the screen.
        if player == 1:
            position = random.randint(1,2)
        # Gorilla image for player2 is randomly placed on the right of the screen.
        elif player == 2:
            position = random.randint(-3,-2)
            
        # Move function
        self.move = random.randint(1,2) or random.randint(-3,-2)
        
        # The center of the gorilla is the center of the building
        self.rect.centerx = self.buildings[position].rect.centerx
        # The bottom of the gorilla is the top of the building
        self.rect.bottom = self.buildings[position].rect.top

        
    def update(self, phase):

        # When phase = 3, player1's gorlla image is changed to throwing
        if phase == 3:
            self.image = self.throw_right
        # When phase = 6, player2's gorlla image is changed to throwing
        elif phase == 6:
            self.image = self.throw_left
        # When phase = 1, 2, 4, 5, both gorilla images are standing.   
        else:
            self.image = self.stand



