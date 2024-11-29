import pygame
import sys

pygame.init()

#game window settings
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape the Slimgeon")

#load background image
background = pygame.image.load('Start_screen.png')  

#load button images
start_img = pygame.image.load('START.png').convert_alpha()  
quit_img = pygame.image.load('Quit.png').convert_alpha()  

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_hovered(self):
        #check if the mouse is hovering over the button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            return True
        return False

    def is_clicked(self):
        #check if the mouse is clicked on the button
        if self.is_hovered() and pygame.mouse.get_pressed()[0]:  # Left click (0 is the left mouse button)
            return True
        return False

#create buttons
start_button = Button(100, 456, start_img, 0.5)
quit_button = Button(235, 300, quit_img, 0.5)

#game loop
run = True
while run:
    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #draw background
    screen.blit(background, (0, 0))

    #draw buttons
    start_button.draw()
    quit_button.draw()

    #check for button clicks
    if start_button.is_clicked():
        print("Start Button Clicked")

    if quit_button.is_clicked():
        print("Exit Button Clicked")
        run = False

    #handle Hover Effect
    if start_button.is_hovered():
        pygame.draw.rect(screen, (255, 255, 255), start_button.rect, 3)  # Add a border on hover (white outline)
    if quit_button.is_hovered():
        pygame.draw.rect(screen, (255, 255, 255), quit_button.rect, 3)  # Add a border on hover (white outline)

    #update the Screen
    pygame.display.update()

#quit the Game
pygame.quit()
sys.exit()
