import pygame
import sys

# General Setup
pygame.init()
clock = pygame.time.Clock()


# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption('Name')

# Constants 
SCREEN_MIDDLE = [screen_width/2, screen_height/2]

# Game Rects
ball = pygame.Rect(SCREEN_MIDDLE[0] - 15, SCREEN_MIDDLE[1] - 15, 30,30)
player = pygame.Rect(screen_width - 40, SCREEN_MIDDLE[1] -70 ,10,140)
opponent = pygame.Rect(40, SCREEN_MIDDLE[1] -70 ,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

# Game Loop
while True:
    # Input Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Visual
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (SCREEN_MIDDLE[0],0), (SCREEN_MIDDLE[0],screen_height))


    # Updating the window
    pygame.display.flip()
    clock.tick(60)