import pygame
import random

class Gorilla(pygame.sprite.Sprite):
    def __init__(self, buildings, player=1):
        self.buildings = buildings
        self.sheet = pygame.image.load("donkeykong_enemies_sheet.png").convert_alpha()

        # The images
        self.throw_left = self.sheet.subsurface(pygame.Rect(48, 56, 48, 32))
        self.stand = self.sheet.subsurface(pygame.Rect(104, 56, 40, 32))
        self.throw_right = self.sheet.subsurface(pygame.Rect(152, 56, 48, 32))

        # This is where we stand
        self.rect = pygame.Rect(0, 0, 40, 32)
#        self.image.set_colorkey(pygame.Color('black'))
        self.image = self.stand
        
        if player == 1:
            position = random.randint(1,2)
        elif player == 2:
            position = random.randint(-3,-2)
        self.rect.centerx = self.buildings[position].rect.centerx
        self.rect.bottom = self.buildings[position].rect.top
        
    def update(self, phase):
        if phase == 3:
            self.image = self.throw_right
            
        elif phase == 6:
            self.image = self.throw_left
            
        else:
            self.image = self.stand