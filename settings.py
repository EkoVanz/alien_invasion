class Settings():
    #this is our settings class for our game

    def __init__(self):
        #screen settings
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (20,203,230)

        #Ship settings
        self.ship_speed_factor = 1.5

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3
