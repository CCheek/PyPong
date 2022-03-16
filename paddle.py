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

    def move_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > constants.size[1] - 100:
            self.rect.y = constants.size[1] - 100

    def set_position(self, new_y_value):
        if new_y_value >= constants.size[1] - 100:
            self.rect.y = constants.size[1] - 100
        elif new_y_value <= 0:
            self.rect.y = 0
        else:
            self.rect.y = new_y_value

    def move_to_pos(self, new_y_value):
        if new_y_value < self.rect.y:
            if (self.rect.y - int(constants.step/1.3)) <= 0:
                self.rect.y = 0
            else:
                if self.rect.y - new_y_value <= int(constants.step/2):
                    self.rect.y -= int(constants.step/3)
                elif self.rect.y - new_y_value <= int(constants.step/1.3):
                    self.rect.y -= int(constants.step/2)
                else:
                    self.rect.y -= int(constants.step/1.3)
        elif new_y_value > self.rect.y:
            if (self.rect.y + int(constants.step/1.3)) >= constants.size[1] - 100:
                self.rect.y = constants.size[1] - 100
            else:
                if new_y_value - self.rect.y <= int(constants.step / 2):
                    self.rect.y += int(constants.step / 3)
                elif new_y_value - self.rect.y <= int(constants.step / 1.3):
                    self.rect.y += int(constants.step / 2)
                else:
                    self.rect.y += int(constants.step / 1.3)