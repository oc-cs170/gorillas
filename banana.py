"""Banana Class"""

## Banana is created here.
## Velocity of the banana is set in polar form for x and y.
## Angle is convereted into radians



import pygame
import math


class Banana(pygame.sprite.Sprite):
    def __init__(self, angle, velocity, wind, location):
        # Banana snippet (creation)
        self.angle = angle
        self.velocity = velocity
        radians = math.radians(self.angle)                                                       
        self.vx = self.velocity * math.cos(radians)
        self.vy = self.velocity * math.sin(radians)
        self.wind = wind
        self.location = location
        self.rotation = 0
        
        # New surface
        self.art = pygame.Surface((15, 30))

        # Draw the banana & set transparency
        pygame.draw.circle(self.art, pygame.Color('Yellow'), (15, 15), 15)
        pygame.draw.circle(self.art, pygame.Color('Black'), (24, 15), 18)
        self.art.set_colorkey(pygame.Color('Black'))

        # Set banana location
        self.rect = self.art.get_rect()
        self.rect.bottomleft = self.location
        self.image = self.art


    def update(self):
        # x velocity is adding the wind vector to it.
        self.vx += self.wind
        # y velocity is adding the gravity vector to it.
        self.vy += -.3

        # Rotate the image
        self.rotation += 90
        if self.rotation == 360:
            self.rotation = 0
        self.image = pygame.transform.rotate(self.art, self.rotation)

        self.rect = self.image.get_rect(center = self.rect.center)
        # The banana rect is moved in place based on what the new x and y velocities are.
        self.rect.move_ip(self.vx, -self.vy)


        
        