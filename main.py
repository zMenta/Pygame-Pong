import pygame
import sys

# Functions
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def quit(event):
    if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Constants 
SCREEN_MIDDLE = [screen_width/2, screen_height/2]

# Game Rects
ball = pygame.Rect(SCREEN_MIDDLE[0] - 15, SCREEN_MIDDLE[1] - 15, 30,30)
player = pygame.Rect(screen_width - 40, SCREEN_MIDDLE[1] -70 ,10,140)
opponent = pygame.Rect(40, SCREEN_MIDDLE[1] -70 ,10,140)

ball_speed_x = 7
ball_speed_y = 7

paddle_speed = 9
player_speed = 0


bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

# Game Loop
while True:
    # Input Handling
    for event in pygame.event.get():
        quit(event)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 9
            if event.key == pygame.K_UP:
                player_speed -= 9
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 9
            if event.key == pygame.K_UP:
                player_speed += 9


    # if player.y >= 0 or player.y <= screen_height:

    ball_animation()
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


    # Opponent Handling #
    opponent.y += paddle_speed

    if opponent.top <= 0 or opponent.bottom >= screen_height:
        paddle_speed *= -1

    #Visual
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (SCREEN_MIDDLE[0],0), (SCREEN_MIDDLE[0],screen_height))


    # Updating the window
    pygame.display.flip()
    clock.tick(60)