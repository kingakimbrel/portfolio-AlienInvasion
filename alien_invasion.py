import pygame

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
    # Alien
    alien = Alien(screen)

    while True:
        check_events(ship)
        ship.update()
        update_screen(ai_settings, screen, ship)


run_game()
