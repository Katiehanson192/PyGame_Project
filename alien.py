import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #class to represent a single alien in the fleet

    def __init__(self, ai_game):
        #initialize alien + set starting position
        super().__init__()
        self.screen = ai_game.screen
        
        #working on alien speed
        self.settings = ai_game.settings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alient near the top left of the screen
        self.rect.x = self.rect.width #sets alien's location to top left corner @ and create a space the same size of the alien's height and weight
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position
        self.x = float(self.rect.x) #tracks horizontal speed 

    def check_edges(self):
        #return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0: #if alien position to the right is less than or equal to the right screen position value 
                                                                        #or the the left position value is 0, give answer True--> tell aliens to move right
            return True

    def update(self):
        #move alien to the right or left
        self.x +=(self.settings.alien_speed *
                        self.settings.fleet_direction) #alien_speed * fleet_direction b/c determines if fleet moves left or right
        self.x +=self.settings.alien_speed #update alien's position each time by moving it the right by amt stored in alien_speed
        self.rect.x = self.x #updates value of rect.x, which is the alien's position (self.x can store decimals and rect.x can't)