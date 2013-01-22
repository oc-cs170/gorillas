# Banana snippet (creation)
# New surface
banana_art = pygame.Surface((15, 30))

# Draw the banana & set transparency
pygame.draw.circle(banana_art, pygame.Color('Yellow'), (15, 15), 15)
pygame.draw.circle(banana_art, pygame.Color('Black'), (24, 15), 18)
banana_art.set_colorkey(pygame.Color('Black'))

# Set banana location
banana_rect = banana_art.get_rect()
banana_rect.center = 100, 100



# Banana snippet (use)
screen.blit(banana_art, banana_rect)
