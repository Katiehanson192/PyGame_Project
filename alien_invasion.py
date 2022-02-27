from lib2to3 import pygram
import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    #overall class to manage game assets and behavior

    ##initialize game, and create game assests and behavior.
    def __init__(self):
        pygame.init() #why don't we need a "self." argument??
        #self.screen = pygame.display.set_mode((1200, 800))  #represents entire game window
        self.settings = Settings() #creating an instance of settings

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.scree_height))

        self.screen = pygame. display.set_mode((0,0), pygame.FULLSCREEN) #making full screen
        self.settings.screen_width = self.screen.get_rect().width #making full screen
        self.settings.screen_height = self.screen.get_rect().height #making full screen

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) #makes instance of the ship after screen has been created

        #Bullet 
        self.bullets = pygame.sprite.Group() #used to store live bullets 

        #change background color
        #self.bg_color = (230, 230, 230)

    def run_game(self):
        #starting main loop for the game!
        while True:  #looking for keyboard/mouse clicks from user
            self._check_events()
            self._update_screen()
            self.ship.update()  #this calls the update method in the ship file, it can correctly move right
            self.bullets.update() #update position of the bullets

    def _check_events(self):
        #respond to key presses and mouse clicks
        for event in pygame.event.get():  #returns list of events that have taken place since last time the function was called
            if event.type ==pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  #set the moving_right object? to False once key isn't pressed anymore
                self._check_keyup_events(event)

    def _check_keydown_events(self, event): #respond to key press
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  #if right arrow is pressed, chance the moving_right object? in Ship file to True!
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: #Q to Quit
            sys.exit()
        elif event.key == pygame.K_SPACE:  #call _fire_bullet when space bar is pressed (don't have to modify keyup events b/c nothing changes when the button is released)
            self._fire_bullet()
                
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            #move ship to the right when right arrow is pressed
            #self.ship.rect.x += 1  #moves ship to the right 1 pixel 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #create new bullet + add it to the bullets group
        new_bullet = Bullet(self) #instance of Bullet called new bullet
        self.bullets.add(new_bullet) #add that new instance the group bullets()

    def _update_screen(self):
            #redraw the screen during each pas through loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme() #this draws ship on screen and puts it on top of the bg color

            for bullet in self.bullets.sprites(): #sprites method returns list of al aprites in the group
                bullet.draw_bullet()  #to draw all bullets on screen, loop through draw_bullet method for all bullets in the group

            #make most recently drawn screen visible
            pygame.display.flip() #How it game elements move/dissapear

if __name__=='__main__':
    #making a game instance and running the game
    ai = AlienInvasion()
    ai.run_game()
