import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    #overall class to manage game assets and behavior

    ##initialize game, and create game assests and behavior.
    def __init__(self):
        pygame.init() #why don't we need a "self." argument??
        #self.screen = pygame.display.set_mode((1200, 800))  #represents entire game window
        self.settings = Settings() #creating an instance of settings

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.scree_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) #makes instance of the ship after screen has been created

        #change background color
        #self.bg_color = (230, 230, 230)

    def run_game(self):
        #starting main loop for the game!
        while True:  #looking for keyboard/mouse clicks from user
            self._check_events()
            self._update_screen()

    def _check_events(self):
        #respond to key presses and mouse clicks
        for event in pygame.event.get():  #returns list of events that have taken place since last time the function was called
            if event.type ==pygame.QUIT:
                sys.exit()

    def _update_screen(self):
            #redraw the screen during each pas through loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme() #this draws ship on screen and puts it on top of the bg color

            #make most recently drawn screen visible
            pygame.display.flip() #How it game elements move/dissapear

if __name__=='__main__':
    #making a game instance and running the game
    ai = AlienInvasion()
    ai.run_game()
