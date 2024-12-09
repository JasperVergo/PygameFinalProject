import pygame
import sys
from Support import *

pygame.init()

def aspect_scale(img, box):
    bx, by = box
    """ Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    ix,iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx/float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by/float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx/float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by

    return pygame.transform.scale(img, (sx,sy))

#game window settings
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape the Slimgeon")

#load background image
background = import_folder('graphics/screens/Pause_screen')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale the background to the screen size

restart_img = import_folder('graphics/buttons/Restart')
quit_img = import_folder('graphics/buttons/Quit')

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        # self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = aspect_scale(image, (width * scale, height * scale))
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
restart_button = Button(412, 300, restart_img, 1.7)
quit_button = Button(412, 400, quit_img, 1.7)

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
    restart_button.draw()
    quit_button.draw()

    #check for button clicks
    if restart_button.is_clicked():
        print("Start Button Clicked")

    if quit_button.is_clicked():
        print("Exit Button Clicked")
        run = False

    #handle Hover Effect
    if restart_button.is_hovered():
        pygame.draw.rect(screen, (255, 255, 255), restart_button.rect, 3)  # Add a border on hover (white outline)
    if quit_button.is_hovered():
        pygame.draw.rect(screen, (255, 255, 255), quit_button.rect, 3)  # Add a border on hover (white outline)

    #update the Screen
    pygame.display.update()

#quit the Game
pygame.quit()
sys.exit()

