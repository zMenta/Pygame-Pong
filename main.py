import pygame
import sys
from random import choice

# Functions
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball_restart()
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def ball_start():
    global ball_speed_x, ball_speed_y
    ball_speed_x *= -1
    ball_speed_y *= choice((1, -1))

    ball.x = SCREEN_MIDDLE[0]
    ball.y = SCREEN_MIDDLE[1]

def ball_restart():
    global opponent_score, player_score
    if ball.left <= 0:
        ball_start()
        player_score += 1
    if ball.right >= screen_width:
        ball_start()
        opponent_score += 1

def opponent_animation():
    opponent_ai()
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def quit(event):
    if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def player_movement(event):
    global player_speed
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

def opponent_ai():
    if ball.x <= screen_width-400:
        if opponent.top < ball.y:
            opponent.y  += paddle_speed
        if opponent.bottom > ball.y:
            opponent.y -= paddle_speed

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


# Text 
player_score = 0
opponent_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)


# Colors

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

# Game Loop
while True:
    # Input Handling
    for event in pygame.event.get():
        quit(event)
        player_movement(event)
        

    ball_animation()
    player_animation()
    opponent_animation()
    

    #Visual
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (SCREEN_MIDDLE[0],0), (SCREEN_MIDDLE[0],screen_height))

    player_text = game_font.render(f"{player_score}", False, light_grey)
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(player_text, (SCREEN_MIDDLE[0] + 20, 150))
    screen.blit(opponent_text, (SCREEN_MIDDLE[0] - 30, 150))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)