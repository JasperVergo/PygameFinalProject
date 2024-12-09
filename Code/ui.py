import pygame
from Settings import TILE_SIZE

class Ui_element(pygame.sprite.Sprite):
    def __init__(self,pos,scale,backgroundColor,image=pygame.surface.Surface((TILE_SIZE,TILE_SIZE)), *groups):
        super().__init__(*groups)
        self.pos = pos
        self.scale = scale
        self.background = backgroundColor
        self.text = self.text
        self.image = image
        self.rect = self.image.get_rect()
    