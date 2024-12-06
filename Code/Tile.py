import pygame
from Settings import *

class Tile(pygame.sprite.Sprite):
    """the base for all tiles that are placed"""
    def __init__(self,x,y,size,groups,id,inflation,image = pygame.Surface((TILE_SIZE,TILE_SIZE))):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.size = size 
        self.groups = groups 
        self.image = image
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.hitbox = self.rect.inflate(inflation)
        self.id = id

