import pygame
from Entity import Enity
from Settings import *
from Support import *
import math

class Player(Enity):
    def __init__(self,groups,pos,collition_sprites,id):
        super().__init__(groups,collition_sprites,player_Base_Stats["maxHealth"])
        #TODO: orginize this init 
        self.speed = player_Base_Stats["speed"] #the move speed of the player
        #visuals 
        self.graphics = {
            "side_walk": import_folder("graphics\Player\side_walk"),
            "side_idle": import_folder("graphics\Player\side_idle"),
            "hurt": import_folder("graphics\Player\hurt_anim"),
            "jump": import_folder("graphics\Player\jump_anim"),
            "side_dash" : import_folder("graphics\Player\side_dash_anim"),
            "up_dash" : import_folder("graphics\Player\\up_dash_anim"),
            "fall" : import_folder("graphics\Player\\fall_anim")
        }
        self.holdAnimations = ["jump","side_dash","up_dash","fall"]
        self.id = id
        self.status = "side_walk"
        self.elapsed = pygame.time.get_ticks()
        self.image = self.graphics.get(self.status)[0]
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30,-40) #makes the player hitbox
        self.flipped = False
        self.is_jumping = False
        self.can_dash = True
        self.is_dashing = False
        self.falling = False
        self.dash_cool_down = 250 #in ticks
        self.control_direction = pygame.math.Vector2(0,0)
        self.jumpVelocity = player_Base_Stats["jumpVelocity"]
        self.dashVelocity = player_Base_Stats["dashVelocity"]
        self.dash_timer = -1

    def get_Current_State(self):
        '''
        finds the current state to determine the animation that should be played. 
        the state is a string split by underscores where the first word is the direction, (up, down,side,downside,upside)
        the second section is the action ex. (walk, dash, idle)
        the string should also line up with the file locations so that for exsample up_walk is in the directory player/up/walk
        the left and right sides are done by flipping the player sprite
        '''
        #this is a temperary solution it will porbably need to be rewritten when more states exsist
        old_status = self.status

        if self.direction.x != 0:
            self.status = "side_walk"
        else:
            self.status = "side_idle"

        if self.is_jumping:
            self.status = "jump"
        if not self.is_falling():
            self.is_jumping = False
        
        elif self.velocity.y > 0:
            self.status = "fall"
        
        if self.is_dashing:
            if self.direction.x == 0:
                self.status = "up_dash"
            else:
                self.status = "side_dash"

        if self.status != old_status:
            self.frame_Index = 0
        

    def jump(self):
        if not self.is_falling() and not self.is_dashing:
            self.velocity.y = self.jumpVelocity
            self.direction.y = 1
            self.is_jumping = True

    def dash(self):
        if self.can_dash and not self.is_dashing:
            print("dash")
            self.can_dash = False
            self.is_dashing = True
            self.is_gravity_active = False
            if self.direction.magnitude() > 0:
                self.direction = self.control_direction
            else:
                self.direction.x = -1 if self.flipped else 1
            self.dash_timer = pygame.time.get_ticks()
            if self.control_direction.magnitude() > 0:
                self.velocity = self.control_direction.normalize() * self.dashVelocity
                print(self.velocity)
            else:
                if self.flipped:
                    self.velocity.x = self.dashVelocity * -1 
                else: 
                    self.velocity.x = self.dashVelocity 
                
                

    def on_Ground_hit(self):
        super().on_Ground_hit()
        self.can_dash = True

    def input(self):
        """manages player keypresses"""
        
        #gets all the keys that are currently being pressed, 
        #this is how we are checking key presses rather than with the event bus
        keydown = pygame.key.get_pressed()
        if not self.is_dashing:
            #sets direction of horzantal movment 
            if keydown[pygame.K_a]:
                self.direction.x = -1
                self.control_direction.x = -1
                self.flipped = True
            elif keydown[pygame.K_d]:
                self.direction.x = 1
                self.control_direction.x = 1
                self.flipped = False
            else:
                self.direction.x = 0
                self.control_direction.x = 0

            if keydown[pygame.K_w]:
                self.control_direction.y = -1
            elif keydown[pygame.K_s]:
                self.control_direction.y = 1
            else:
                self.control_direction.y = 0

            if keydown[pygame.K_SPACE]:
                self.jump()
            
            if keydown[pygame.K_f]:
                self.dash()


    def check_events(self):
        if self.dash_timer + self.dash_cool_down < pygame.time.get_ticks():
            self.is_dashing = False
            self.is_gravity_active = True
            self.dashVelocity = player_Base_Stats["dashVelocity"]
    


    def update(self):
        """contains all the code that should be run for the player every frame"""
        if not self.is_dashing:
            self.input()

        #triggers next frame every 8 frames, to increase animation speed decrease this number 
        if self.current_frame % 8 == 0:
            self.animate()

        self.check_events()


        if self.is_dashing:
            self.move(self.dashVelocity)
            if self.dashVelocity > 0:
                self.dashVelocity -= self.drag
        else:
            self.move(self.speed) #this method is in the entity class

        self.current_frame += 1

    