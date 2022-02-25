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