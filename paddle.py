# Paddle class created by 101computing.net

import pygame
import constants


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(constants.background_color)
        self.image.set_colorkey(constants.background_color)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > constants.size[1] - 100:
            self.rect.y = constants.size[1] - 100

    def setPosition(self, new_y_value):
        if new_y_value > constants.size[1] - 100:
            self.rect.y = constants.size[1] - 100
        else:
            self.rect.y = new_y_value
