class GameStats():
    """Track statistick for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialiaze statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Reset game stats"""
        self.ships_left = self.ai_settings.ship_limit
