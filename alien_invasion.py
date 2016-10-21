import pygame
from pygame.sprite import Group

from settings import Settings
from game_models.ship import Ship
from game_models.alien import Alien
from game_functions.core import *


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    # Alien
    alien = Alien(screen)

    while True:
        check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        update_screen(ai_settings, screen, ship, bullets)


run_game()
