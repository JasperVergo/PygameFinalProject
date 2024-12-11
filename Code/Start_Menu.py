import pygame
import sys
from Support import *
import os

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
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape the Slimgeon")

#load background image
background = pygame.image.load('graphics/screens/Start_screen.png').convert_alpha()
width = background.get_width()
height = background.get_height()
background = aspect_scale(background, (width * 4.5, height * 4.5))  # Scale the background to the screen size
# background = aspect_scale(background, (300, 160))  # Scale the background to the screen size


#load button images
start_img = pygame.image.load('graphics/buttons/START.png').convert_alpha()
quit_img = pygame.image.load('graphics/buttons/Quit.png').convert_alpha()

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
start_button = Button(450, 350, start_img, 1.6)
quit_button = Button(450, 440, quit_img, 1.6)

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


