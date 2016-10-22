import pygame
from pygame.sprite import Group

from settings import Settings
from game_models.ship import Ship
from game_functions.core import *
from game_models.game_stats import GameStats
from game_models.button import Button


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Store game statistics
    stats = GameStats(ai_settings)

    # Ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    # Aliens
    aliens = Group()
    create_fleet(ai_settings, screen, ship, aliens)

    while True:
        check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            update_bullets(ai_settings, screen, ship, bullets, aliens)
            update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
