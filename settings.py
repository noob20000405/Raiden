class Settings():
    def __init__(self):
        """initial settings"""

        # screen settings
        self.screen_width = 512
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 5
        self.ship_limit = 1

        # bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1