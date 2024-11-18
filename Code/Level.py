from Settings import *
import pygame 
import Tile
from Support import *
import sys
from Player import Player


class Level():

    def __init__(self):

        ########------Groups------#########
        
        #groups are collections of Sprites that can have actions done to them all at once like drawing them.
        #sprites can be assined to multiple groups
        
        #contains all visible sprites that are drawn to the screen 
        self.visible_Sprites = pygame.sprite.Group()

        #contains sprites that block entites from moving through them 
        self.collition_Sprites = pygame.sprite.Group()

        #contains sprites used for events in the event manager,
        #  in other words it contains trigger boxes for anything that need special or unique logic 
        self.event_Sprites = pygame.sprite.Group()
        ###########################################

        #get display surfice. a display surfice is what pygame draws things to
        self.display_serfice = pygame.display.get_surface()

    


    def create_Map(self,map : list) -> None:
        """loads several maps from csv files and makes tile objects with them"""

        #graphics holds the pygame surfaces for each sprite Tile
        graphics = {
            "rock":import_folder("Graphics\Test")
        }

        #goes through the rows and collums of a 2d list along with the index of each and checks what tile should be spawned along with 
        #calulating where it should be spawned based on the TILE_SIZE varible in Settings.py
        for row_Index,row in enumerate(map):
            for col_Index, col in enumerate(row):
                #TODO: add a switch statement to allow different maps to be loaded differently 
                if col == 1:
                    surf = graphics.get("rock")[0]
                    #this is for testing purposes only
                    Tile.Tile((col_Index * TILE_SIZE),(row_Index * TILE_SIZE),TILE_SIZE, [self.visible_Sprites],surf)  
                elif col == "P": 
                    #loads the player, Note: if no player is pressent the program will currently
                    #  crash due to the update funtion calling it 
                    self.player = Player(self.visible_Sprites,((col_Index * TILE_SIZE, row_Index * TILE_SIZE)))
                    


    def update(self):
        """This is where all things that should be updated every frame """
        self.display_serfice.fill("black")
        self.player.update()
        #TODO: add culling so the game won't load the whole map but instead will load only the part the player can see 
        self.visible_Sprites.draw(self.display_serfice) #draws the visible sprite group to the screen so we can see it. 

    
    def delete_Map(self):
        """removes all the tiles from a map and clears the groups"""
        pass



