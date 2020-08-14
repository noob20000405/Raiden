class Settings():
    def __init__(self):
        """initial settings"""

        # screen settings
        self.screen_width = 512
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 1

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10
        self.alien_points = 50

        # enemy settings
        self.speed_enemy1 = 5

        # speed up settings
        self.speedup_scale = 1.1

        # points up
        self.score_scale = 1.5

        # initialize the speed settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 5

        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # increase alien points
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)