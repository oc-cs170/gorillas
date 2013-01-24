#!/usr/bin/env python

"""Main file with game loop for Gorillas.pyth
"""

import pygame
import random
from gorilla import Gorilla

WINDOW_TITLE = 'Gorillas'
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 30

class Gorillas(object):
    """Create a game of Gorillas."""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background = self.create_buildings(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # Use a clock to control frame rate
        self.clock = pygame.time.Clock()


    def create_buildings(self, width, height):
        # Use screen height and width to generate buildings
        self.buildings = []
        self.left = 0
        sky = self.screen.copy()
        sky.fill(pygame.Color('lightblue'))
        color = pygame.Color('black')
        
        while self.left < width:
            building_width = int(random.uniform(width * .1, width * .2))
            building_height = int(random.uniform(height *.15, height * .5))
            building_width = min(building_width, width-self.left)
            building = pygame.Rect(self.left, height - building_height, building_width, building_height)
            self.left += building_width
            self.buildings.append(building)
            pygame.draw.rect(sky, color, building, 3)
        
        return sky
        
    def play(self):
        """Start Gorillas program.
        """
        self.gorilla = Gorilla(self.buildings, 1)
        self.gorilla2 = Gorilla(self.buildings, 2)
        running = True
        while running:
            self.clock.tick(FPS)  # Max frames per second

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # Draw the scene
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.gorilla.art, self.gorilla.rect)
            self.screen.blit(self.gorilla2.art, self.gorilla2.rect)
            pygame.display.flip()


if __name__ == '__main__':
    game = Gorillas()
    game.play()
