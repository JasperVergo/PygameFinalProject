import pygame
from Settings import *

class Tile(pygame.sprite.Sprite):
    """the base for all tiles that are placed"""
    def __init__(self,x,y,size,groups,id,inflation,image):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.size = size 
        self.groups = groups 
        self.image = image
        self.image = pygame.transform.scale(image, (int(self.size[0]),int(self.size[1])))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.hitbox = self.rect.inflate(inflation)
        self.id = id


class folliage(Tile):
    def __init__(self, x, y, size, groups, id, inflation, image,player):
        super().__init__(x, y, size, groups, id, inflation, image)
        self.is_jiggling = False
        self.jiggle_speed = 6 # bigger is slower
        self.jiggle_amount = 4
        self.current_frame = 0
        self.jiggle_start = self.current_frame
        self.player_ref = player
        self.is_jiggled = False
        self.base_image = self.image

        self.total_rotation = 0

    def jiggle(self):
        """rotates the folliage to get a little jiggle """
        if self.current_frame % self.jiggle_speed == 0 and self.player_ref.velocity.magnitude() > 0:
            if not self.is_jiggled:
                self.image = pygame.transform.rotate(self.image, self.jiggle_amount * -1)
                self.is_jiggled = True
            else:
                self.image = self.base_image
                self.is_jiggled = False



        self.current_frame += 1

