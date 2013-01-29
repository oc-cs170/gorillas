#!/usr/bin/env python

## Authors: Josh Reynolds, Lindsey Winters, and Rafael Figueroa
## Date: January 22, 2013
## Description: Another pygame program. Similar to the gorillas game.
## Two players, (gorilla1, and gorilla2), each input an angle and velocity
## at which they would like their banana to be thrown. If banana is thrown by player1
## and hits their openent, then player1 receives a point and a new round starts and vice versa.
## If a builing is hit, a seciton in the builidng is removed and play conitnues until
## either player hits thier oppenent with the banna. 
## Tip: There is also a wind vector both players should be aware of, and don't forget about gravity!



"""Main file with game loop for Gorillas.pyth
"""

import pygame
import random
from gorilla import Gorilla
from building import Building
from banana import Banana

WINDOW_TITLE = 'Gorillas'
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 738
FPS = 30

class Gorillas(object):
    """Create a game of Gorillas."""
    def __init__(self):
        pygame.init()
        # Gorillas is displayed as Window Title
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background = self.new_round(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # Use a clock to control frame rate
        self.clock = pygame.time.Clock()


    def new_round(self, width, height, score=[0, 0]):
        # Use screen height and width to generate buildings

        # Setting bananna = None here and calling it to be drawn later
        self.banana = None
        self.wind = random.uniform(-1, 1) / 10
        self.score = score
        self.phase = 1
        
        self.angle = ''
        self.velocity = ''
        
        # Crater = spot in building to be removed after banana has made contact with buiding.
        self.craters = []
        self.buildings = []
        self.left = 0

        sky = self.screen.copy()
        sky.fill(pygame.Color('lightblue'))
        
        # Buildings are created here
        while self.left < width:
            building_width = int(random.uniform(width * .1, width * .15))
            building_height = int(random.uniform(height *.15, height * .5))
            building_width = min(building_width, width-self.left)
            building = Building((self.left, WINDOW_HEIGHT - building_height), building_width, building_height)
            self.left += building_width
            self.buildings.append(building)
        

        self.gorilla = Gorilla(self.buildings, 1)
        self.gorilla2 = Gorilla(self.buildings, 2)

        return sky
        
    def play(self):
        """Start Gorillas program.
        """
        running = True
        

        font = pygame.font.SysFont("monospace", 15)

        while running:
            # Max frames per second
            self.clock.tick(FPS)  

            # Phase 1: player1's angle input                  # Phase 4: player2's angle input
            # Phase 2: player2's velocity input               # Phase 5: players2's velcity input
            # Phase 3: player1's banana being thrown          # Phase 6: player2's banana being thrown
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    
                    # When Backspace button is pressed
                    elif event.key == pygame.K_BACKSPACE:
                        if self.phase == 1 or self.phase == 4:
                            self.angle = self.angle[0:-1]
                        elif self.phase == 2 or self.phase == 5:
                            self.velocity = self.velocity[0:-1]
                    
                    # When Enter button is pressed
                    elif event.key == pygame.K_RETURN:
                        self.phase += 1
                        # Player1's banana is thrown, Phase = 3
                        if self.phase == 3:
                            self.banana = Banana(int(self.angle), int(self.velocity) / 3, self.wind, self.gorilla.rect.topleft)
                        # Player2's banana is thrown, Phase = 6
                        if self.phase == 6:
                            self.banana = Banana(180 - int(self.angle), int(self.velocity) / 3, self.wind, self.gorilla2.rect.topleft)    

                    else:
                        if self.phase == 1 or self.phase == 4:
                            self.angle += str(event.key - 48)
                            
                        elif self.phase == 2 or self.phase == 5:
                            self.velocity += str(event.key - 48)
                     
            # Draws the background
            self.screen.blit(self.background, (0, 0))

            # If banana is called (phase 3 or 6), drawn to screen
            if self.banana:
                self.screen.blit(self.banana.image, self.banana.rect)
                
                # Sees if banana has left the screen.
                # If banana has left the screen, banana is removed, angle and velocity are cleared, and moves to next phase.
                if self.banana.rect.right > WINDOW_WIDTH or self.banana.rect.left < 0 or self.banana.rect.top < 0:
                    self.phase += 1
                    self.banana = None
                    self.angle = ''
                    self.velocity = ''


                # Determines if banana rect has collided with one of the gorilla rects.
                # If collided, adds one to score for player1 and new round is being called
                elif self.banana.rect.colliderect(self.gorilla) and self.phase == 6:
                    self.score[1] += 1
                    self.background = self.new_round(WINDOW_WIDTH, WINDOW_HEIGHT, self.score)

                # Determines if banana rect has collided with one of the gorilla rects.
                # If collided, adds one to score for player2 and new round is being called
                elif self.banana.rect.colliderect(self.gorilla2) and self.phase == 3:
                    self.score[0] += 1
                    self.background = self.new_round(WINDOW_WIDTH, WINDOW_HEIGHT, self.score)

                # Determines if banana rect has collided with one of the building rects in the list.
                # If banana rect collides with a building rect, a secitoin in the building is removed. 
                # Angle and Velcity are reset and moves onto the next phase.
                for building in self.buildings:
                    try:    
                        if building.rect.collidepoint(self.banana.rect.center):
                            self.phase += 1
                            self.angle = ''
                            self.velocity = ''
                            crater = pygame.Rect((0, 0) ,(26, 26))
                            crater.center = self.banana.rect.center
                            self.craters.append(crater)
                            self.banana = None
                            break
                    except:
                        pass

            # Buildings are drawn to the screen.
            for building in self.buildings:
                self.screen.blit(building.image, building.rect.topleft)
            
            # When phase reaches 3 or 4, gorilla image is changed
            if self.phase == 3 or self.phase == 4:
                self.gorilla.update(self.phase)
            # When phase reaches 6 or 1, gorilla image is changed
            elif self.phase == 6 or self.phase == 1:
                self.gorilla2.update(self.phase)

            # When phase reaches 3 or 6, banana is thrown.
            if self.phase == 3 or self.phase == 6:
                self.banana.update()

            # The crater is being drawn to the screen here, which is the section of the building to be removed. 
            for crater in self.craters:
                art = pygame.Surface(crater.size)
                art.set_colorkey(pygame.Color('black'))
                pygame.draw.circle(art, pygame.Color('lightblue'), (13, 13), 13)
                self.screen.blit(art, crater.center)
                
            
            # Gorillas are drawn to the screen.
            self.screen.blit(self.gorilla.image, self.gorilla.rect.topleft)
            self.screen.blit(self.gorilla2.image, self.gorilla2.rect.topleft)

            # Sun is created and drawn to the screen. 
            sun = pygame.Surface((50, 50))
            pygame.draw.circle(sun, pygame.Color('Yellow'), (25, 25), 25)
            sun.set_colorkey(pygame.Color('Black'))
            self.screen.blit(sun, (WINDOW_WIDTH/2, WINDOW_HEIGHT*.1))

            
            # Once phase reaches 7, Phase is now reset to one so game can continue
            if self.phase == 7:
                self.phase = 1
            
            # This is where player input (angle, velocity) is being displayed on screen.
            # Wind vector and score is also displayed on screen. 
            angle = font.render("Angle " + self.angle, 2, (255,255,0))
            self.screen.blit(angle, (0, 14))
            velocity = font.render("Velocity " + self.velocity, 2, (255,255,0))
            self.screen.blit(velocity, (0, 28))
            score = font.render("Score: " + str(self.score[0]) + ' ' + str(self.score[1]), 2, (255,255,0))
            self.screen.blit(score, (0, 42))
            wind = font.render("Wind: " + str(self.wind*10)[0:5], 2, (255,255,0))
            self.screen.blit(wind, (0, 56))

            pygame.display.flip()


if __name__ == '__main__':
    game = Gorillas()
    game.play()
