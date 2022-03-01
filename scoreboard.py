import pygame.font

class Scoreboard:
    #class to report scoring informaiton
    def __init__(self, ai_game):
        #initialize scorekeeping attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats=ai_game.stats

        #font settings
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Prepare initial score igame
        self.prep_score()

    def prep_score(self):
        #turn scoreboard into rendered image
        rounded_score = round(self.stats.score, -1) #-1 for round tells python to round to the nearest 10
        score_str="{:,}".format(rounded_score) #adds commas to large numbers
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def show_score(self):
        #draw scoreboard to screen
        self.screen.blit(self.score_image, self.score_rect)

    