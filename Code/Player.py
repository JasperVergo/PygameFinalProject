import pygame
from Entity import Enity
from Settings import *
from Support import *

class Player(Enity):
    def __init__(self,groups,pos):
        super().__init__(groups)
        #TODO: this should be taken from some kind of stats dictionary in settings rather than being hard coded here 
        self.speed = 10 #the move speed of the player

        #visuals 
        self.graphics = {
            "side_walk": import_folder("graphics\walk_anim")
        }
        self.status = "side_walk"
        self.elapsed = pygame.time.get_ticks()
        self.image = self.graphics.get(self.status)[0]
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect #makes the player hitbox, TODO: inflate the hitbox by a negitive number to make it harder to get stuck



    def get_Current_State(self):
        '''
        finds the current state to determine the animation that should be played. 
        the state is a string split by underscores where the first word is the direction, (up, down,side,downside,upside)
        the second section is the action ex. (walk, dash, idle)
        the string should also line up with the file locations so that for exsample up_walk is in the directory player/up/walk
        the left and right sides are done by flipping the player sprite
        '''
        pass


    def input(self):

        #gets all the keys that are currently being pressed, 
        #this is how we are checking key presses rather than with the event bus
        keydown = pygame.key.get_pressed()

        #sets direction of horzantal movment 
        if keydown[pygame.K_a]:
            self.direction.x = -1
        elif keydown[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
        #TODO: Gravity and jumping 


    def animate(self):
        self.get_Current_State()
        if self.frame_Index + 1 < len(self.graphics.get(self.status)):
            self.frame_Index += 1
            self.image = self.graphics.get(self.status)[self.frame_Index]
        else:
            self.frame_Index = 0
                
        
        
        
        


    def update(self):
        """contains all the code that should be run for the player every frame"""
        self.input()
        self.elapsed = pygame.time.get_ticks() - self.elapsed
        if self.elapsed > 1600:
            print(self.elapsed, pygame.time.get_ticks())
            self.animate()

        self.move(self.speed)

    