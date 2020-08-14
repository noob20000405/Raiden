import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """initial the ship and its position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship picture and shape it in a rectangle
        self.image = pygame.image.load('images/feiji/hero1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # move
        self.moving_right = False
        self.moving_left = False

        # animation
        self.animation = 0

    def update(self):
        """update the ship position"""
        # update the 'center' instead of rect.centerx
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

        self.animation += 1
        self.animation %= 2
        if self.animation == 0:
            self.image = pygame.image.load('images/feiji/hero2.png')
        else:
            self.image = pygame.image.load('images/feiji/hero1.png')

    def blitme(self):
        """redraw the ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx