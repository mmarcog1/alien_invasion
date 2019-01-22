class Settings():
    """A class to store all settings for Alien invasion."""

    def __init__(self):
        """Initialize the game settings."""

        #Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Ship settings, modifies the pixels the ship is moved when the position is updated.
        self.ship_speed_factor = 1.5
        
        #Bullet settings, the bullet is a rectangle.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =  60,60,60
        self.bullets_allowed = 5

        #Alien settings
