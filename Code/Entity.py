import pygame
from Settings import TILE_SIZE


class Enity(pygame.sprite.Sprite):

    def __init__(self,groups,collition_sprites,max_Health):
        super().__init__(groups)
        #TODO: The healh values should be taken from a database 
        #max health and current health are needed to insure that even if the player heals they won't go over the maximum health
        #it is also used for the health bars ratios
        self.current_Health = max_Health
        self.max_Health = max_Health


        self.current_frame = 0 #count of the frames that this has been active 
        self.frame_Index = 0 #used from animations

        #a Vector2 is a set of two numbers ex. (0,4) representing x and y. 
        # you can accsess the indevidual values with the .x and .y 
        #pygame has a number of handy methods that can be used on a Vector2
        #this varible is responsible for acually moving the entity and should be set to move the entity rather than directly moving them. 
        #once set call the move() method with the speed of the entity 
        self.direction = pygame.math.Vector2()

        self.collition_Sprites = collition_sprites
        self.collition_tolorance = 5

        self.gravity = .4 #gravity speed
        self.max_gravity_speed = 4
        self.velocity = pygame.Vector2(0,0)
        


    def move(self, speed):
        "Universal move funtion for all enities"

        #checks the length of the vector. if the vector is 0 the entity is still. 
        # normilizing a vector with a magnatude of 0 throws a error
        #if self.direction.magnitude() != 0: 
        #    self.direction.normalize() #makes the magnatude of the vector 1 to prevent increased speed on dyagnols 
        
        #moves the entity based on the direction 
        self.velocity.x = self.direction.x * speed

        if self.is_falling():
            self.velocity.y += self.gravity
            if self.velocity.y > self.max_gravity_speed:
                self.velocity.y = self.max_gravity_speed
            else:
                self.direction.y = -1
        elif self.velocity.y > 0 :
            self.velocity.y = 0
            self.direction.y = 0


        #print(self.velocity,self.is_falling())


        self.hitbox.y += self.velocity.y
        self.collition("verdical")

        self.hitbox.x += self.velocity.x
        self.collition("horizantal")




        #updates the rest of the enity to follow the hitbox 

        self.rect.center = self.hitbox.center
        

    def collition(self,direction):
        """Handles collition for the enity""" 
        #handles horizantal collition
        #TODO: upword collition is so broken
        if direction == "horizantal":
            for sprite in self.collition_Sprites:
                topleft = self.check_topleft_collition(sprite)
                topright = self.check_topright_collition(sprite)
                bottomright = self.check_bottomright_collition(sprite)
                bottomleft = self.check_bottomleft_collition(sprite)

                if topleft or bottomleft:
                    self.hitbox.left = sprite.hitbox.right

                elif topright or bottomright:
                    self.hitbox.right = sprite.hitbox.left      

        if direction == "verdical":
            for sprite in self.collition_Sprites:
                topleft = self.check_topleft_collition(sprite)
                topright = self.check_topright_collition(sprite)
                bottomright = self.check_bottomright_collition(sprite)
                bottomleft = self.check_bottomleft_collition(sprite)
            
                if topleft or topright:
                    self.hitbox.top = sprite.hitbox.bottom

                elif bottomleft or bottomright:
                    self.hitbox.bottom = sprite.hitbox.top 

    def check_Left_collition(self,sprite):
        return sprite.hitbox.collidepoint(self.hitbox.centerx,self.hitbox.left-self.collition_tolorance)
    
    def check_right_collition(self, sprite):
        return sprite.hitbox.collidepoint(self.hitbox.centerx,self.hitbox.left-self.collition_tolorance)
    
    def check_bottom_collition(self,sprite):
        return sprite.hitbox.collidepoint(self.hitbox.centerx,self.hitbox.bottom+self.collition_tolorance)
    
    def check_top_collition(self,sprite):
        return sprite.hitbox.collidepoint(self.hitbox.centerx,self.hitbox.top-self.collition_tolorance)

    def check_topleft_collition(self,sprite):
        return sprite.hitbox.collidepoint(self.hitbox.topleft)
    
    def check_topright_collition(self,sprite):
        return sprite.hitbox.collidepoint(self.hitbox.topright)
    
    def check_bottomleft_collition(self,sprite):
        return sprite.hitbox.collidepoint(self.hitbox.bottomleft)
    
    def check_bottomright_collition(self,sprite):
        return sprite.hitbox.collidepoint(self.hitbox.bottomright)
    

    def animate(self):
        """updates the frame of the animation based on the status. the animation frames are retrived from the self.graphics variable"""
        self.get_Current_State() #updates the current state 
        #if the next frame exsists 
        if self.frame_Index + 1 < len(self.graphics.get(self.status)):
            self.frame_Index += 1
        
        elif self.status not in self.holdAnimations:
            self.frame_Index = 0 #resets the frame 
        
        #gets the players current frame from self.graphics and flips it if nessissary based on the flipped varible 
        self.image = pygame.transform.flip(self.graphics.get(self.status)[self.frame_Index],self.flipped,False)

    def is_falling(self):
        """returns true if the player is falling"""
        for sprite in self.collition_Sprites:
            if sprite.hitbox.collidepoint(self.hitbox.centerx,self.hitbox.bottom+self.collition_tolorance + 1):
                 return False
        return True            
