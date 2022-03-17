import pygame
from paddle import Paddle
from ball import Ball
import constants

screen = 0
timer = 0

left_paddle = Paddle(constants.foreground_color, 10, 100)
left_paddle.rect.x = 20
left_paddle.rect.y = int((constants.size[1] - 100) / 2)
# Sets the initial position of the paddle to be roughly in the middle of the screen

right_paddle = Paddle(constants.foreground_color, 10, 100)
right_paddle.rect.x = constants.size[0] - 30
right_paddle.rect.y = int((constants.size[1] - 100) / 2)
# Sets the initial position of the paddle to be roughly in the middle of the screen

ball = Ball(constants.foreground_color, 10, 10)
ball.rect.x = int(constants.size[0] / 2)
ball.rect.y = int(constants.size[1] / 2) - 55

all_sprites_list = pygame.sprite.Group()  # Creates a sprite list and adds the paddles and ball to it.

def init():
    global screen
    global timer
    # Imports and in`1its
    pygame.init()

    # Initial variables

    screen = pygame.display.set_mode(constants.size)
    timer = pygame.time.Clock()

    pygame.display.set_caption("Corey's Pong Game")

    all_sprites_list.add(left_paddle)
    all_sprites_list.add(right_paddle)
    all_sprites_list.add(ball)