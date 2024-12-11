import pygame
from Settings import TILE_SIZE

class Ui_element(pygame.sprite.Sprite):
    def __init__(self,pos,scale,image, *groups):
        super().__init__(*groups)
        self.pos = pos
        self.scale = scale
        self.image = image
        print(self.image)
        self.image = pygame.transform.scale(self.image,scale)
        self.rect = self.image.get_rect(topleft=pos)

class Dash_icon(Ui_element):
    def __init__(self, pos, scale,images, image=pygame.surface.Surface((TILE_SIZE, TILE_SIZE)), *groups):
        super().__init__(pos, scale, image, *groups)
        self.images = images

    def update_status(self,newStatus):
        self.image = self.images[newStatus]