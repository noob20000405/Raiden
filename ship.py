import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """initial the ship and its position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship picture and shape it in a rectangle
        self.image = pygame.image.load('images/plane/hero01.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # load the energy picture
        self.image_energy = pygame.image.load('images/plane/hero_bullet4.png')
        self.energy_rect = self.image_energy.get_rect()

        # position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - self.energy_rect.height
        self.energy_rect.centerx = self.rect.centerx
        self.energy_rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.center_energy = self.center

        # move
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship position"""
        # update the 'center' instead of rect.centerx
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            self.center_energy = self.center
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            self.center_energy = self.center

        self.rect.centerx = self.center
        self.energy_rect.centerx = self.center_energy

    def blitme(self):
        """redraw the ship"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.center_energy = self.center