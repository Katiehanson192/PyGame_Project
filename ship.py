import pygame

class Ship:
    #this classes manages all of the code for the ship element
    def __init__(self, ai_game):
        #initialize game ship + set starting location
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom 

        def blitme(self):
            #draw the ship at its current location
            self.screen.blit(self.image, self.rect)