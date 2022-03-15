import pygame
import random
import constants


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(constants.background_color)
        self.image.set_colorkey(constants.background_color)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.speed = [random.choice((-5, 5)), random.randint(-8, 8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def bounce_left(self):
        self.speed[0] = abs(self.speed[0] + random.randint(-2, 0))
        if self.speed[0] >= 10:
            self.speed[0] = 10
        self.speed[1] = random.randint(-(self.speed[0]+2), -self.speed[0])

    def bounce_right(self):
        self.speed[0] = -abs(self.speed[0]+random.randint(0,2))
        if self.speed[0] <= -10:
            self.speed[0] = -10
        self.speed[1] = random.randint(-(self.speed[0]+2), -self.speed[0])

    def reset(self):
        self.rect.x = int(constants.size[0]/2)
        self.rect.y = int(constants.size[1]/2)-55
        self.speed = [random.choice((-5, 5)), random.randint(-8, 8)]