import pygame

class Ship:
    #this classes manages all of the code for the ship element
    def __init__(self, ai_game):   #ai is from the game instance created in the class file for Alien Invasion
        #initialize game ship + set starting location
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() #so we can place ship at correct location of screen

        #load ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom 

        #Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update the ship's position based on the movement flags
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:  #use 2 If stmts bc that puts them at equal priority. Elif always prioritizes the first stmt? Makes movements more accurate in case player hits both keys
            self.rect.x -=1       


    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)    #Draws image on screen @ position specified by self.rect