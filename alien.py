import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #class to represent a single alien in the fleet

    def __init__(self, ai_game):
        #initialize alien + set starting position
        super().__init__()
        self.screen = ai_game.screen

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alient near the top left of the screen
        self.rect.x = self.rect.width #sets alien's location to top left corner @ and create a space the same size of the alien's height and weight
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position
        self.x = float(self.rect.x) #tracks horizontal speed 