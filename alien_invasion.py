import sys
import pygame

class AlienInvasion:
    #overall class to manage game assets and behavior

    ##initialize game, and create game assests and behavior.
    def __init__(self):
        pygame.init() #why don't we need a "self." argument??
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game():
        #starting main loop for the game!
        while True:
            #looking for keyboard/mouse clicks from user
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()
            
            #make most recently drawn screen visible
            pygame.display.flip()

if __name__=='__main__':
    #making a game instance and running the game
    ai = AlienInvasion()
    ai.run_game()