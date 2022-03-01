import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    #class to report scoring informaiton
    def __init__(self, ai_game):
        #initialize scorekeeping attributes
        self.ai_game = ai_game #assigning game instance to an attribute to make the ships for display in upper left corner
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats=ai_game.stats

        #font settings
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Prepare initial score images
        self.prep_score()
        self.prep_high_score()

        #Display current level
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        #turn scoreboard into rendered image
        rounded_score = round(self.stats.score, -1) #-1 for round tells python to round to the nearest 10
        score_str="{:,}".format(rounded_score) #adds commas to large numbers
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def prep_high_score(self):
        #turn high score into rendered image
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)   #formatting and rounding highscore to nearest 10, added commas
        self.high_score_image = self.font.render(high_score_str,True, self.text_color, self.settings.bg_color) #generate high score as image

        #Center highscore at top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx #center horizontally
        self.high_score_rect.top = self.score_rect.top #top of high score image will match top of score image

    def check_high_score(self):
        #check to see if there's a new high score
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        #turn level into rendered image
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str,True, self.text_color, self.settings.bg_color) #creates image from value stored stats.level

        #position level to show below the score
        self.level_rect = self.level_image.get_rect() 
        self.level_rect.right = self.score_rect.right #align with socre's right position
        self.level_rect.top = self.score_rect.bottom + 10 #puts at top, but 10 pixels lower than the high score

    def prep_ships(self):
        #show how many ships are left
        self.ships = Group() #creates an empty group of ships to hold ship instances
        for ship_number in range(self.stats.ships_left): #to fill the list, must run a loop for every ship player has left
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width #displaying ships for they're next to each other with a 10 pixel margin on left sideof the group
            ship.rect.y = 10 #y coordinates 10 pixels down from top of screen
            self.ships.add(ship) #add each new ship player has left to the group


    def show_score(self):
        #draw scoreboard to screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        #show level
        self.screen.blit(self.level_image, self.level_rect) #displays level on screen
        #show ships left on the screen
        self.ships.draw(self.screen)



    