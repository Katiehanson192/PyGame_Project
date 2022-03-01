import pygame
from pygame.sprite import Sprite #to create group of ships for upper left corner

class Ship(Sprite):
    #this classes manages all of the code for the ship element
    def __init__(self, ai_game):   #ai is from the game instance created in the class file for Alien Invasion
        #initialize game ship + set starting location
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings  #create this so we can use it update(). Need to assign position to variable that can store a decimal value
        self.screen_rect = ai_game.screen.get_rect() #so we can place ship at correct location of screen

        #load ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom 

        #store decimal value for ship's horizontal position
        self.x = float(self.rect.x) #this assigns value of self.rect.x to a float

        #Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update the ship's position based on the movement flags
        #updating ship's value, not the rect.x position
        if self.moving_right and self.rect.right < self.screen_rect.right: #ensures ship isn't going past right side of screen
            self.x += self.settings.ship_speed #udpate self.x first and then update self.rect.x b/c self.x stores decimal value
        if self.moving_left and self.rect.left >0: #ensures ship isn't going past left side of screen
            self.x -= self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x
        '''
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:  #use 2 If stmts bc that puts them at equal priority. Elif always prioritizes the first stmt? Makes movements more accurate in case player hits both keys
            self.rect.x -=1
        '''       

    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)    #Draws image on screen @ position specified by self.rect

    def center_ship(self):
        #centers ship on screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)