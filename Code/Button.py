import pygame
from os import path as osPath


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, filepath, scale,screen,groups,click_action,action_args):
        super().__init__(groups)
        image = pygame.image.load(osPath.join(*(filepath + ".png").split("\\"))).convert_alpha()
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
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

