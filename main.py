import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard

from button import Button
from ship import Ship
from alien import Alien
from enemy import Enemy1

import create_enemys as ce

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
    # create the scoreboard
    sb = Scoreboard(ai_settings, screen, stats)
    # set bkg color
    bg_color = ai_settings.bg_color
    # create a ship
    ship = Ship(ai_settings, screen)
    # create some bullets
    bullets = Group()
    aliens = Group()
    enemy1s = Group()

    # create the fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # create fleet of enemy1
    ce.create_fleet_e1(ai_settings, screen, enemy1s)

    # animation
    animation = 0

    # main loop
    while True:

        # listen event
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, enemy1s)

        if stats.game_active:
            # reposition the ship
            ship.update()

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

            ce.update_enemy1(enemy1s)

        # refresh the screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, animation, enemy1s)

        animation += 1
        animation %= 5

run_game()