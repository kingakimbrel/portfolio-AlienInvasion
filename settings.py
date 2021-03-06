class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Alien settings
        self.fleet_drop_speed = 10
        self.top_offset = 20

        # How quickly the game speeds up
        self.speedup_factor = 1.5
        self.bullets_number_factor = 1.5
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Settings that change throughout the game"""

        self.bullets_allowed = 5

        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_factor
        self.bullet_speed_factor *= self.speedup_factor
        self.alien_speed_factor *= self.speedup_factor

        # Increase number of bullets
        self.bullets_allowed = int(self.bullets_number_factor * self.bullets_allowed)

        # Increase points
        self.alien_points =int(self.alien_points * self.score_scale)
        print(self.alien_points)
