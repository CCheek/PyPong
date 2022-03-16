# Second try at creating a pong game (relies on 101computing.net;s tutorial for a significant amount of the logic)
# Author: Corey Cheek
"""
    Controls:
        - Up and Down arrow keys for the right side (Player A)
        - W for up and S for down for the left side (Player B)
        - Space for pause UNIMPLEMENTED
        - X (both the key and the window bar) for quit
    Objective of the game:
        Use your respective keys to move the paddle up and down and block the ball from hitting the side wall closest to
        your paddle.
"""

# Imports and in`1its
import pygame
from paddle import Paddle
from ball import Ball
import constants
pygame.init()


# Initial variables
screen = pygame.display.set_mode(constants.size)
pygame.display.set_caption("Corey's Pong Game")
timer = pygame.time.Clock()

right_paddle = Paddle(constants.foreground_color, 10, 100)
right_paddle.rect.x = constants.size[0] - 30
right_paddle.rect.y = int((constants.size[1]-100)/2)
# Sets the initial position of the paddle to be roughly in the middle of the screen

left_paddle = Paddle(constants.foreground_color, 10, 100)
left_paddle.rect.x = 20
left_paddle.rect.y = int((constants.size[1]-100)/2)
# Sets the initial position of the paddle to be roughly in the middle of the screen

ball = Ball(constants.foreground_color, 10, 10)
ball.rect.x = int(constants.size[0]/2)
ball.rect.y = int(constants.size[1]/2)-55

all_sprites_list = pygame.sprite.Group()  # Creates a sprite list and adds the paddles and ball to it.
all_sprites_list.add(right_paddle)
all_sprites_list.add(left_paddle)
all_sprites_list.add(ball)


# Main Loop
while constants.loop:
    if constants.right_paddle_up:
        right_paddle.move_up(constants.step)
    elif constants.right_paddle_down:
        right_paddle.move_down(constants.step)

    for event in pygame.event.get():  # For all events (click, keyboard, controller, etc..)
        if event.type == pygame.QUIT:  # If user clicked close
            constants.loop = False  # Exit the loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x key will quit the game
                constants.loop = False
            elif event.key == pygame.K_SPACE:  # Pressing the space key will pause the game UNIMPLEMENTED
                constants.paused = not constants.paused
            elif event.key == pygame.K_UP:
                right_paddle.move_up(constants.step)
                constants.right_paddle_up = True
            elif event.key == pygame.K_DOWN:
                right_paddle.move_down(constants.step)
                constants.right_paddle_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                constants.right_paddle_up = False
            elif event.key == pygame.K_DOWN:
                constants.right_paddle_down = False

    all_sprites_list.update()

    # Check if the ball is bouncing against any of the walls:
    if ball.rect.x >= constants.size[0] - 10:
        constants.right_score += 1
        ball.reset()
    if ball.rect.x <= 0:
        constants.left_score += 1
        ball.reset()
    if ball.rect.y > constants.size[1] - 10:
        ball.speed[1] = -ball.speed[1]
    if ball.rect.y < 0:
        ball.speed[1] = -ball.speed[1]

    if ball.rect.colliderect(right_paddle.rect):
        ball.bounce_right()
    if ball.rect.colliderect(left_paddle.rect):
        ball.bounce_left()

    left_paddle.move_to_pos(ball.rect.y - 50)

    screen.fill(constants.background_color)
    pygame.draw.line(screen, constants.foreground_color, [int(constants.size[0]/2)-1, 0],
                     [int(constants.size[0]/2)-1, constants.size[1]])
    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(constants.right_score), True, constants.foreground_color)
    screen.blit(text, (int(constants.size[0]/4) - 5, 10))
    text = font.render(str(constants.left_score), True, constants.foreground_color)
    screen.blit(text, (int(constants.size[0]/2) + int(constants.size[0]/4) - 5, 10))

    pygame.display.flip()

    timer.tick(60)
    print(str(int(timer.get_fps())) + ", " + str(ball.speed[0]))

pygame.quit()