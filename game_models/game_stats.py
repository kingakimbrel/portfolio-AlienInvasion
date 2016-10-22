class GameStats():
    """Track statistick for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialiaze statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        # High score
        self.high_score = 0

    def reset_stats(self):
        """Reset game stats"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
