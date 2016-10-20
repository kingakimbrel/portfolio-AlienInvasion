import pygame


class Alien():
    def __init__(self, screen):
        """Initialize the alien and it's starting position"""
        self.screen = screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)