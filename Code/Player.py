import pygame
from Entity import Enity
from Settings import *
from Support import *
import math
import random

class Player(Enity):
    def __init__(self,groups,pos,collition_sprites,event_sprites,id,level,folliage_sprites,dashUI):
        super().__init__(groups,collition_sprites,player_Base_Stats["maxHealth"],folliage_sprites)
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
            "upSide_dash": import_folder("Graphics\diagonal_up_dash"),
            "downSide_dash": import_folder("Graphics\diagonal_down_dash"),
            "down_dash" : import_folder("Graphics\down_dash"),
            "fall" : import_folder("graphics\Player\\fall_anim")
        }
        #sounds from https://freesound.org/search/?q=footstep&f=grouping_pack%3A%229344_Footsteps%22
        self.footprints_sound = [
            pygame.mixer.Sound(import_audio_file("Audio\\Footstep_1.wav")),
            pygame.mixer.Sound(import_audio_file("Audio\\Footstep_2.wav")),
            pygame.mixer.Sound(import_audio_file("Audio\\Footstep_3.wav")),
            pygame.mixer.Sound(import_audio_file("Audio\\Footstep_4.wav")),
        ]
        for sound in self.footprints_sound:
            sound.set_volume(.1)
        self.holdAnimations = ["jump","side_dash","up_dash","fall"]
        self.event_sprites = event_sprites
        self.id = id
        self.level = level
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
        self.dash_UI = dashUI
        self.dash_sound = import_audio_file("Audio\mixkit-air-in-a-hit-2161.wav") # from https://mixkit.co/free-sound-effects/swish/
        self.dash_sound.set_volume(.3)

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
            if self.control_direction.x == 0 and self.control_direction.y == -1:
                self.status = "up_dash"
            elif self.control_direction.x != 0 and self.control_direction.y < 0:
                self.status = "upSide_dash"
            elif self.control_direction.x != 0 and self.control_direction.y > 0:
                self.status = "downSide_dash"
            elif self.control_direction.x == 0 and self.control_direction.y > 0:
                self.status = "down_dash"
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
            print(self.direction)
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

            else:
                if self.flipped:
                    self.velocity.x = self.dashVelocity * -1 
                else: 
                    self.velocity.x = self.dashVelocity 
            self.dash_sound.play()
            
                

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
            if keydown[pygame.K_a] or keydown[pygame.K_LEFT]:
                self.direction.x = -1
                self.control_direction.x = -1
                self.flipped = True
            elif keydown[pygame.K_d] or keydown[pygame.K_RIGHT]:
                self.direction.x = 1
                self.control_direction.x = 1
                self.flipped = False
            else:
                self.direction.x = 0
                self.control_direction.x = 0

            if keydown[pygame.K_w] or keydown[pygame.K_UP]:
                self.control_direction.y = -1
            elif keydown[pygame.K_s] or keydown[pygame.K_DOWN]:
                self.control_direction.y = 1
            else:
                self.control_direction.y = 0

            if keydown[pygame.K_SPACE]:
                self.jump()
            
            if keydown[pygame.K_f]:
                self.dash()


    def check_events(self):
        #dash timer
        if self.dash_timer + self.dash_cool_down < pygame.time.get_ticks():
            self.is_dashing = False
            self.is_gravity_active = True
            self.dashVelocity = player_Base_Stats["dashVelocity"]

        #event tiles
        for event in self.event_sprites:
            if self.hitbox.colliderect(event.hitbox):
                #triggers each event
                if EVENT_IDS.get(event.id) == "restart":
                    self.level.create_Map("Restart_Menu")
                elif EVENT_IDS.get(event.id) == "win":
                    self.level.create_Map("Menu")


    def update(self):
        """contains all the code that should be run for the player every frame"""
        if not self.is_dashing:
            self.input()

        #triggers next frame every 8 frames, to increase animation speed decrease this number 
        if self.current_frame % 8 == 0:
            self.animate()
        #walking sounds
        if self.current_frame % 10 == 0 and "walk" in self.status.split("_"):
                random.choice(self.footprints_sound).play()


        self.check_events()
        self.dash_UI.update_status(self.can_dash)
        self.collide_folliage()

        if self.is_dashing:
            self.move(self.dashVelocity)
            if self.dashVelocity > 0:
                self.dashVelocity -= self.drag
        else:
            self.move(self.speed) #this method is in the entity class

        self.current_frame += 1

    