class Setting:
    def __init__(self):
        """initialize game settings"""
        # screen settings
        self.screen_w = 1200
        self.screen_h = 700
        self.bg_color = (230, 230, 230)

        # ship sett
        self.ship_speed = 1.5

        # bullet sett
        self.bullet_speed = 2.0
        self.bullet_w = 3
        self.bullet_h = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10

        # game settings
        self.difficulty_scale = 1.0

        # points and features
        self.points_for_feature = 200
        self.feature_cost = 200
