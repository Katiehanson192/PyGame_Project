class GameStats:
    #track statistics for Alien Invasion

    def __init__(self, ai_game):
        #initialize statistics
        self.settings = ai_game.settings
        self.reset_stats() #for when players start a new game
        #start AI in inactive state
        self.game_active = False


    def reset_stats(self):
        #Initialize statistics that can change during the game
        self.ships_left = self.settings.ship_limit #makes games stats set correctly when game is launched
        self.score = 0 #initialize here so it resets each time the game starts over

