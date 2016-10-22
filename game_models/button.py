import pygame.font


class Button():
    def __init__(self, ai_settings, screen, msg):
        """Initialiaze button"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Dimensions and properties of the buttons
        self.width, self.heigth = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Button's object
        self.rect = pygame.Rect(0, 0, self.width, self.heigth)
        self.rect.center = self.screen_rect.center

        # Button's message
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn message into a rendered unage and center text ib the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
