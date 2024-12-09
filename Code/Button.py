import pygame
from os import path as osPath


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, filepath, scale,screen,groups,click_action,action_args):
        super().__init__(groups)
        image = pygame.image.load(osPath.join(*(filepath + ".png").split("\\"))).convert_alpha()
        width = image.get_width()
        height = image.get_height()
        # self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = self.aspect_scale(image, (width * scale, height * scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen
        self.clicked_action = click_action
        self.action_args = action_args

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.is_hovered():
            pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 3)  # Add a border on hover (white outline)

    def is_hovered(self):
        #check if the mouse is hovering over the button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            return True
        return False

    def is_clicked(self):
        #check if the mouse is clicked on the button
        if self.is_hovered() and pygame.mouse.get_pressed()[0]:  # Left click (0 is the left mouse button)
            self.clicked_action(self.action_args)
            return True
        return False
    
    def update(self): 
        self.draw()
        self.is_hovered()
        self.is_clicked()

    def aspect_scale(self, image, box):
        bx, by = box
        """ Scales 'img' to fit into box bx/by.
        This method will retain the original image's aspect ratio """
        ix,iy = image.get_size()
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

        return pygame.transform.scale(image, (sx,sy))

