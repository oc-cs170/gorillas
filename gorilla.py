import pygame
import random

class Gorilla(pygame.sprite.Sprite):
    def __init__(self, buildings, player=1):
        self.buildings = buildings
        self.rect = pygame.Rect(104, 56, 40, 32)
        self.art = pygame.Surface(self.rect.size)
        self.art.set_colorkey(pygame.Color('black'))
        self.sheet = pygame.image.load("donkeykong_enemies_sheet.png")
        self.art.blit(self.sheet, (0, 0), self.rect)
        
        if player == 1:
            position = random.randint(1,3)
        elif player == 2:
            position = random.randint(-4,-2)
        self.rect.centerx = self.buildings[position].centerx
        self.rect.bottom = self.buildings[position].top
        
        