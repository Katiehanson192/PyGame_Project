import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): #Sprite  = group related elements of game + act on all grouped elements at once
    #class to manage bullets firing from ship
    
    def __init__(self, ai_game):
        #create bullet object at ship's current position
        super().__init__() #to inherit properly from Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet rect at (0,0) and set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) #building rect location based on pygame.Rect(). Arguments: x, y coordinates of the top-left corner + height and width
        self.rect.midtop = ai_game.ship.rect.midtop #midtop = matches ships. makes bullet emerge from top of ship

        #store bullet's position as decimal value
        self.y = float(self.rect.y) #decimal value to make finner adjustments

    def update(self):
        #move bullet up screen/manages position
        #update decimale position of bullet
        self.y -=self.settings.bullet_speed #bullet moves up screen, corresponds to decreasing y value (update position: subtract bullet speed from y position)
        #update the rect position
        self.rect.y = self.y #set new position for the location of bullet

    def draw_bullet(self):
        #draw bullet to scren
        pygame.draw.rect(self.screen, self.color, self.rect)