import pygame
from Entity import Enity
from Settings import *
from Support import *
import math

class Player(Enity):
    def __init__(self,groups,pos,collition_sprites):
        super().__init__(groups,collition_sprites)
        #TODO: this should be taken from some kind of stats dictionary in settings rather than being hard coded here 
        self.speed = 10 #the move speed of the player
        #visuals 
        self.graphics = {
            "side_walk": import_folder("graphics\Player\side_walk"),
            "side_idle": import_folder("graphics\Player\side_idle"),
            "hurt": import_folder("graphics\Player\hurt_anim"),
            "jump": import_folder("graphics\Player\jump_anim"),
            "side_dash" : import_folder("graphics\Player\side_dash_anim"),
            "up_dash" : import_folder("graphics\Player\\up_dash_anim")
        }
        self.status = "side_walk"
        self.elapsed = pygame.time.get_ticks()
        self.image = self.graphics.get(self.status)[0]
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-40,-20) #makes the player hitbox, TODO: inflate the hitbox by a negitive number to make it harder to get stuck
        self.flipped = False
        self.is_jumping = False
        self.is_dashing = False
        self.jumpVelocity = -6

    def get_Current_State(self):
        '''
        finds the current state to determine the animation that should be played. 
        the state is a string split by underscores where the first word is the direction, (up, down,side,downside,upside)
        the second section is the action ex. (walk, dash, idle)
        the string should also line up with the file locations so that for exsample up_walk is in the directory player/up/walk
        the left and right sides are done by flipping the player sprite
        '''
        #this is a temperary solution it will porbably need to be rewritten when more states exsist
        if self.direction.x != 0:
            self.status = "side_walk"
        else:
            self.status = "side_idle"

    def jump(self):
        if not self.is_falling():
            self.velocity.y = self.jumpVelocity
            self.direction.y = 1
            print("jump")

    def input(self):
        """manages player keypresses"""
        
        #gets all the keys that are currently being pressed, 
        #this is how we are checking key presses rather than with the event bus
        keydown = pygame.key.get_pressed()

        #sets direction of horzantal movment 
        if keydown[pygame.K_a]:
            self.direction.x = -1
            self.flipped = True
        elif keydown[pygame.K_d]:
            self.direction.x = 1
            self.flipped = False
        else:
            self.direction.x = 0

        if keydown[pygame.K_SPACE]:
            self.jump()
        
        #TODO: Gravity and jumping 


    def update(self):
        """contains all the code that should be run for the player every frame"""
        self.input()

        #triggers next frame every 8 frames, to increase animation speed decrease this number 
        if self.current_frame % 8 == 0:
            self.animate()

        self.move(self.speed) #this method is in the entity class

        self.current_frame += 1

    