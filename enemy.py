import pygame
from pygame.sprite import Sprite

class Enemy1(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/enemy/enemy.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.speed_enemy1

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y