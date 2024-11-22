import pygame


class Enity(pygame.sprite.Sprite):

    def __init__(self,groups,collition_sprites):
        super().__init__(groups)
        #TODO: The healh values should be taken from a database 
        #max health and current health are needed to insure that even if the player heals they won't go over the maximum health
        #it is also used for the health bars ratios
        self.current_Health = 100
        self.max_Health = 100


        self.current_frame = 0 #count of the frames that this has been active 
        self.frame_Index = 0 #used from animations

        #a Vector2 is a set of two numbers ex. (0,4) representing x and y. 
        # you can accsess the indevidual values with the .x and .y 
        #pygame has a number of handy methods that can be used on a Vector2
        #this varible is responsible for acually moving the entity and should be set to move the entity rather than directly moving them. 
        #once set call the move() method with the speed of the entity 
        self.direction = pygame.math.Vector2()

        self.collition_Sprites = collition_sprites

    def move(self, speed):
        "Universal move funtion for all enities"

        #checks the length of the vector. if the vector is 0 the entity is still. 
        # normilizing a vector with a magnatude of 0 throws a error
        if self.direction.magnitude() != 0: 
            self.direction.normalize() #makes the magnatude of the vector 1 to prevent increased speed on dyagnols 
        
        #moves the entity based on the direction 
        self.hitbox.x += self.direction.x * speed
        self.collition("horizantal")
        self.hitbox.y += self.direction.y * speed 
        self.collition("verdical")
        #updates the rest of the enity to follow the hitbox 
        self.rect.center = self.hitbox.center
        
    def animate(self):
        """updates the frame of the animation based on the status. the animation frames are retrived from the self.graphics variable"""
        self.get_Current_State() #updates the current state 
        #if the next frame exsists 
        if self.frame_Index + 1 < len(self.graphics.get(self.status)):
            self.frame_Index += 1
        else:
            self.frame_Index = 0 #resets the frame 
        
        #gets the players current frame from self.graphics and flips it if nessissary based on the flipped varible 
        self.image = pygame.transform.flip(self.graphics.get(self.status)[self.frame_Index],self.flipped,False)

    def is_falling(self):
        """returns true if the player is falling"""
        pass

    def collition(self,direction):
        """Handles collition for the enity""" 
        #basic consepts taken from this tutorial: https://www.youtube.com/watch?v=QU1pPzEGrqw

        #handles horizantal collition
        if direction == "horizantal":
            #checks each collition sprite
            for sprite in self.collition_Sprites:
                #checks if there was a collition anywhere
                if sprite.hitbox.colliderect(self.hitbox):   
                    #this would mean that the entity is moving to the left
                    if self.direction.x < 0:
                        #if the entity dose collide move the left face of the entity hitbox
                        #  to the right side of the sprite it collided with 
                        self.hitbox.left = sprite.hitbox.right
                    #this would mean that the entity is moving to the right
                    if self.direction.x > 0:
                        #if the entity dose collide move the right face of the entity hitbox
                        #  to the left side of the sprite it collided with 
                        self.hitbox.right = self.hitbox.left
        #this handles collition for verdical movement
        #NOTE This is not tested
        if direction == "verdical":
            for sprite in self.collition_Sprites:
                #checks if there was a collition anywhere
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y < 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y > 0:
                        self.hitbox.top = sprite.hitbox.bottom