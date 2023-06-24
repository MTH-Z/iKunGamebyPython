import pygame
from pygame.sprite import Sprite


class IKun(Sprite):
    def __init__(self, ikun_game):
        super().__init__()
        self.screen = ikun_game.screen

        self.image = pygame.image.load('Data/images/iKun.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        self.rect.y += 200
