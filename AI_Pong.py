# Second try at creating a pong game (relies on 101computing.net;s tutorial for a significant amount of the logic)
# Author: Corey Cheek
"""
    Controls:
        - Up and Down arrow keys for the right side (Player A)
        - W for up and S for down for the left side (Player B)
        - Space for pause UNIMPLEMENTED
        - X (both the key and the window bar) for quit
    Objective of the game:
        Use your respective keys to move the paddle up and down and block the constants.ball from hitting the side wall closest to
        your paddle.
"""

# Imports and in`1its
import pygame
import constants
import init


# Main Loop
def mainloop():
    while constants.loop:
        if constants.right_paddle_up:
            init.right_paddle.moveUp(constants.step)
        elif constants.right_paddle_down:
            init.right_paddle.moveDown(constants.step)

        for event in pygame.event.get():  # For all events (click, keyboard, controller, etc..)
            if event.type == pygame.QUIT:  # If user clicked close
                constants.loop = False  # Exit the loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x key will quit the game
                    constants.loop = False
                elif event.key == pygame.K_SPACE:  # Pressing the space key will pause the game UNIMPLEMENTED
                    constants.paused = not constants.paused
                elif event.key == pygame.K_UP:
                    init.right_paddle.moveUp(constants.step)
                    constants.right_paddle_up = True
                elif event.key == pygame.K_DOWN:
                    init.right_paddle.moveDown(constants.step)
                    constants.right_paddle_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    constants.right_paddle_up = False
                elif event.key == pygame.K_DOWN:
                    constants.right_paddle_down = False

        init.all_sprites_list.update()

        # Check if the constants.ball is bouncing against any of the walls:
        if init.ball.rect.x >= constants.size[0] - 10:
            constants.right_score += 1
            init.ball.reset()
        if init.ball.rect.x <= 0:
            constants.left_score += 1
            init.ball.reset()
        if init.ball.rect.y > constants.size[1] - 10:
            init.ball.speed[1] = -init.ball.speed[1]
        if init.ball.rect.y < 0:
            init.ball.speed[1] = -init.ball.speed[1]

        init.left_paddle.move_to_pos(init.ball.rect.y-50)

        if init.ball.rect.colliderect(init.right_paddle.rect):
            init.ball.bounce_right()
        if init.ball.rect.colliderect(init.left_paddle.rect):
            init.ball.bounce_left()

        init.screen.fill(constants.background_color)
        pygame.draw.line(init.screen, constants.foreground_color, [int(constants.size[0]/2)-1, 0],
                         [int(constants.size[0]/2)-1, constants.size[1]])
        init.all_sprites_list.draw(init.screen)

        font = pygame.font.Font(None, 74)
        text = font.render(str(constants.right_score), True, constants.foreground_color)
        init.screen.blit(text, (int(constants.size[0]/4) - 5, 10))
        text = font.render(str(constants.left_score), True, constants.foreground_color)
        init.screen.blit(text, (int(constants.size[0]/2) + int(constants.size[0]/4) - 5, 10))

        pygame.display.flip()

        init.timer.tick(60)
        print(str(int(init.timer.get_fps())) + ", " + str(init.ball.speed[0]))

    pygame.quit()