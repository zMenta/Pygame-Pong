import pygame
import sys

# General Setup
pygame.init()
clock = pygame.time.Clock()


# Setting up the main window
screen_size = [1280,960]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Name')


# Game Loop
while True:
    # Input Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Updating the window
    pygame.display.flip()
    clock.tick(60)