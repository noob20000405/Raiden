import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien

import game_functions as gf

def run_game():
    # screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raiden")
    # draw the start button
    play_button = Button(ai_settings, screen, "Play")
    # create a game stats object
    stats = GameStats(ai_settings)
    # set bkg color
    bg_color = ai_settings.bg_color
    # create a ship
    ship = Ship(ai_settings, screen)
    # create some bullets
    bullets = Group()
    aliens = Group()

    # create the fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # animation
    animation = 0

    # main loop
    while True:

        # listen event
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            # reposition the ship
            ship.update()

            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # refresh the screen
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, animation)

        animation += 1
        animation %= 5

run_game()