import sys
from time import sleep #pauses game for a bit once ship is hit

import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        #create instance to store game statistics
        self.stats = GameStats(self)
        self.ship = Ship(self) #makes instance of the ship after screen has been created

        #Bullet 
        self.bullets = pygame.sprite.Group() #used to store live bullets 

        #Alien
        self.aliens = pygame.sprite.Group()#store the aliens
        self._create_fleet()

        #make play button
        self.play_button = Button(self, "Play") #creates instance of Button with label of "Play"



    def run_game(self):
        #starting main loop for the game!
        while True:  #looking for keyboard/mouse clicks from user
            self._check_events()

            if self.stats.game_active:
                self.ship.update()  #this calls the update method in the ship file, it can correctly move right
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        #respond to key presses and mouse clicks
        for event in pygame.event.get():  #returns list of events that have taken place since last time the function was called
            if event.type ==pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  #set the moving_right object? to False once key isn't pressed anymore
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() #only clicks on the play button will be recognized to start the game
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        #start a new game when the player clicks play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos) #only will start if play button is clicked AND game is currently inactive
        if button_clicked and not self.stats.game_active: #if mouse click collides w/ play button, make game active
            #reset game stats
            self.stats.reset_stats() #reset game stats, gives player 3 more ships
            self.stats.game_active = True

            #get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()  

            #hide mouse cursor
            pygame.mouse.set_visible(False)      


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
        if len(self.bullets) < self.settings.bullets_allowed: #checks to see if # of bullets fired, doesn't exceed allowed amount in settings before firing more bullets
            new_bullet = Bullet(self) #instance of Bullet called new bullet
            self.bullets.add(new_bullet) #add that new instance the group bullets()

    def _update_bullets(self):
        #update position of bullets and get rid of old bullets
        
        #update bullet position
        self.bullets.update()

        #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():  #can't remove items in a list in a for loop, so use copy
            if bullet.rect.bottom <=0: #check to see if the bullet has dissapeared at top of screen
                self.bullets.remove(bullet) #if yes, remove bullet

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
         #Code for when bullets collide with aliens
        #   If hit, get rid of bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) #detects if bullet and alien collide. "True" = remove each object upon collision
                                                                                     #where individual aliens are destroyed
        if not self.aliens: #checks is alien group is empty, if yes, returns a false
            #destroy existing bullets and create new fleet
            self.bullets.empty() #if no aliens, empty the group of bullets (remove any bullets that haven't collided)
            self._create_fleet() #calls method that fills the screen with aliens again

    def _create_fleet(self):
        #create the fleet of aliens
        #make an alien
        alien = Alien(self) #creating an alien instance. Need this before calcs b/c need to know width and height
        alien_width, alien_height = alien.rect.width, alien.rect.height #stores alien width and height
        #find # of aliens that can fit in each row across the screen
        available_space_x = self.settings.screen_width - (2*alien_width) #this leaves space for the margins (1 alien width on each side)
        #find # of aliens in a row with spacing between them. spacing = width of 1 alien
        number_aliens_x = available_space_x // (2*alien_width)

        #determine # of rows of aliens that fit onto the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.scree_height - (3*alien_height)-ship_height) #vertical space available = sub alien height from top, ship height from bottom, and 2 alien heights from bottom
        number_rows = available_space_y // (2*alien_height) #row height = 1 alien. space/height of 2 aliens

        #create fleet of aliens
        for row_number in range(number_rows): #nested for loops needed to create multiple rows
            for alien_number in range(number_aliens_x): #counts from 0 to # of rows we want
                self._create_alien(alien_number, row_number) #creates an alien in row 1. Row_number argument allows each row to be placed farther down the screen

    def _create_alien(self, alien_number, row_number):
         #create alien + place in row
        alien = Alien(self) #creates alien instance
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2*alien_width*alien_number #setting x coordinates. #each alien = pushed to the right 1 alien width from left margin
                                                                    #x2 b/c each alien takes up 2 spaces (to allow for 1 width of space b/t them
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2*alien.rect.height*row_number #each row starts 2 alien heights apart
        self.aliens.add(alien) #adding that instance to the fleet holding all of the other aliens

    def _check_fleet_edges(self):
        #respond appropiately if any aliens have reached the left or right edge
        for alien in self.aliens.sprites(): #for every alien stored in the alien sprites group,
            if alien.check_edges(): #run the check_edges method in alien file--> check to see if the aliens hit either side of screen
                self._change_fleet_direction() #if check_edges returns true, call the change_fleet_direction method and...
                break #break the for loop 

    def _change_fleet_direction(self):
        #drop the entire fleet and change it's directions
        for alien in self.aliens.sprites(): #loop through all the aliens in the sprites group
            alien.rect.y += self.settings.fleet_drop_speed #change the y position by adding the drop speed amount 
        self.settings.fleet_direction *= - 1 #changes the fleet's direction by multiplying it's current value by -1 

    def _check_aliens_bottom(self):
        #check if any aliens have reached bottom of the screen
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >=screen_rect.bottom:
                #treat this the same as if the ship got hit
                self._ship_hit()
                break

    def _ship_hit(self):
        #respond to ships being hit by aliens
        if self.stats.ships_left > 0:
            #decrment ships left
            self.stats.ships_left -= 1 #reduces ship count by 1

            #get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5) #pause before redrawing game so player knows they've been hit

        else: 
            self.stats.game_active = False #if player has no more ships, set game_active to False
            pygame.mouse.set_visible(True) #cursor visible as soon as game becomes inactive

    def _update_aliens(self):
        #check if fleet is at an edge, then update position of all aliens in the fleet
        self._check_fleet_edges()#call the check fleet edges to check if the fleet is at an edge or not before updating the position of the aliens
        self.aliens.update() #corresponds to method in alien file that changes their position

        #look for alien and ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens): #looks for any member of a group coming in contact with a sprite (ship), stops looking once it's found an alien that collided with the ship
            self._ship_hit()
            

        #look for aliens hitting bottom of the screen
        self._check_aliens_bottom()


    def _update_screen(self):
            #redraw the screen during each pas through loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme() #this draws ship on screen and puts it on top of the bg color

            for bullet in self.bullets.sprites(): #sprites method returns list of al aprites in the group
                bullet.draw_bullet()  #to draw all bullets on screen, loop through draw_bullet method for all bullets in the group

            #alien
            self.aliens.draw(self.screen) #draw alien on screen

            #draw play button on screen
            if not self.stats.game_active:
                self.play_button.draw_button() #create AFTER all other elements have been drawn but before flipping to new screen

            #make most recently drawn screen visible
            pygame.display.flip() #How it game elements move/dissapear

if __name__=='__main__':
    #making a game instance and running the game
    ai = AlienInvasion()
    ai.run_game()
