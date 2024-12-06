import pygame

class Ui_element(pygame.sprite.Sprite):
    def __init__(self,pos,scale,backgroundColor, *groups):
        super().__init__(*groups)
        self.pos = pos
        self.scale = scale
        self.background = backgroundColor
        self.text = self.text
    