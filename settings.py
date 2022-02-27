class Settings:
    #class to store all settings for AI game

    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.scree_height = 800
        self.bg_color = (230, 230, 230)
        
        #Ship settings
        self.ship_speed = 1.5  #determines how far to move the ship on each pass through the loop
                                #need this b/c rect.x and rect.y only accept integers

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3