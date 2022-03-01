import pygame.font
class Button:

    def __init__(self, ai_game, msg): 
        #initialized button attributes
        self.screen = ai_game.screen  
        self.screen_rect = self.screen.get_rect()

        #set dimensinos and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48) #default font, size 48

        #Build button's rect object and center it
        self.rect = pygame.Rect(0,0, self.width, self.height) #center button on screen 
        self.rect.center = self.screen_rect.center

        #Button message needs to be prepped only once
        self._prep_msg(msg) #needs to render the string you want to display as an image

    def _prep_msg(self, msg):
        #turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg,True, self.text_color,self.button_color) #turns text stored in msg into an image and stores in self.msg_image
        self.msg_image_rect = self.msg_image.get_rect() #centering the text
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect) #fill in button
        self.screen.blit(self.msg_image,self.msg_image_rect) #text image