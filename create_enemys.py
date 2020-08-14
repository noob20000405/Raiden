import random

import pygame

from enemy import Enemy1

def get_number_enemy1_x(ai_settings, enemy1_width):
    available_space_x = ai_settings.screen_width
    number_enemy1_x = int(available_space_x / (2 * enemy1_width))
    return number_enemy1_x

def create_enemy1(ai_settings, screen, enemy1s, enemy1_number):
    enemy1 = Enemy1(ai_settings, screen)
    enemy1_width = enemy1.rect.width
    enemy1.x = enemy1_width + 2 * enemy1_width * enemy1_number
    enemy1.rect.x = enemy1.x
    enemy1.y = -10
    enemy1.rect.y = enemy1.y
    enemy1s.add(enemy1)

def create_fleet_e1(ai_settings, screen, enemy1s):
    enemy1 = Enemy1(ai_settings, screen)
    enemy1_width = enemy1.rect.width
    number_enemy1_x = get_number_enemy1_x(ai_settings, enemy1.rect.width)

    for enemy1_number in range(number_enemy1_x):
        create = random.randint(0, 1)
        if create == 1:
            create_enemy1(ai_settings, screen, enemy1s, enemy1_number)

def update_enemy1(enemey1s):
    enemey1s.update()

def check_e1_bottom(screen, enemy1s):
    screen_rect = screen.get_rect()
    for enemy1 in enemy1s.sprites():
        if enemy1.rect.top > screen_rect.bottom:
            enemy1.y = -10
            enemy1.rect.y = enemy1.y