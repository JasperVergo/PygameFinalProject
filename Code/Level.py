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


        self.half_width = self.display_serfice.get_size()[0] // 2
        self.half_hight = self.display_serfice.get_size()[1] // 2
        self.draw_offset = pygame.math.Vector2()



    def create_Map(self,map : list) -> None:
        """loads several maps from csv files and makes tile objects with them"""

        #graphics holds the pygame surfaces for each sprite Tile
        graphics = {           
            "rock":import_folder("Graphics\Test"),
            "platform_2":import_folder("graphics\tileset\floating_platform"),
            "platform_3":import_folder("graphics\tileset\floating_platform"),
            "platform_end_left":import_folder("graphics\tileset\floating_platform"),
            "platform_end_right":import_folder("graphics\tileset\floating_platform"),
            "platform":import_folder("graphics\tileset\floating_platform"),
            "floor_1":import_folder("graphics\tileset\floor"),
            "floor_2":import_folder("graphics\tileset\floor"),
            "floor_3":import_folder("graphics\tileset\floor"),
            "floor_void":import_folder("graphics\tileset\floor"),
            "floor_up_corner_left":import_folder("graphics\tileset\floor_up"),
            "floor_up_corner_right":import_folder("graphics\tileset\floor_up"),
            "floor_up_left":import_folder("graphics\tileset\floor_up"),
            "floor_up_right":import_folder("graphics\tileset\floor_up"),
            "floor_up_trans_left":import_folder("graphics\tileset\floor_up"),
            "floor_up_trans_right":import_folder("graphics\tileset\floor_up"),
            "floor_up2_trans":import_folder("graphics\tileset\floor_up"),
            "roof_1":import_folder("graphics\tileset\roof"),
            "roof_2":import_folder("graphics\tileset\roof"),
            "roof_3":import_folder("graphics\tileset\roof"),
            "roof_void":import_folder("graphics\tileset\roof"),
            "wall_floor_corner":import_folder("graphics\tileset\transitions"),
            "wall_floor_void":import_folder("graphics\tileset\transitions"),
            "wall_roof_corner":import_folder("graphics\tileset\transitions"),
            "wall_roof_void":import_folder("graphics\tileset\transitions"),
            "wall_1":import_folder("graphics\tileset\wall"),
            "wall_2":import_folder("graphics\tileset\wall"),
            "wall_3":import_folder("graphics\tileset\wall"),
            "wall_void":import_folder("graphics\tileset\wall"),
        }

        #goes through the rows and collums of a 2d list along with the index of each and checks what tile should be spawned along with 
        #calulating where it should be spawned based on the TILE_SIZE varible in Settings.py
        #TODO: add a switch statement to allow different maps to be loaded differently 

        for layer in maps:
            for row_Index,row in enumerate(import_CSV_file(layer)):
                for col_Index, col in enumerate(row):
                    if col == 1:
                        surf = graphics.get("rock")[0]
                        #this is for testing purposes only
                        Tile.Tile((col_Index * TILE_SIZE),(row_Index * TILE_SIZE),TILE_SIZE, [self.visible_Sprites,self.collition_Sprites],surf)  
                    elif col == "P": 
                        #loads the player, Note: if no player is pressent the program will currently
                        #  crash due to the update funtion calling it 
                        self.player = Player(self.visible_Sprites,((col_Index * TILE_SIZE, row_Index * TILE_SIZE)),self.collition_Sprites)
        if self.player == None:
            self.player = Player(self.visible_Sprites,((DEFAULT_WIDTH // 2, DEFAULT_HIGHT // 2)),self.collition_Sprites)            


    def update(self):
        """This is where all things that should be updated every frame """
        self.display_serfice.fill("black") #fills the screen with black to reset the sreen every frame 
        self.player.update()
        #TODO: add culling so the game won't load the whole map but instead will load only the part the player can see 
        self.custom_draw()

    def custom_draw(self):
        """custom draw to offset the camera based on the players position """
        
        self.draw_offset.x = self.player.rect.centerx - self.half_width
        self.draw_offset.y = self.player.rect.centery - self.half_hight

        for sprite in self.visible_Sprites:
            offset_pos = sprite.rect.topleft - self.draw_offset
            self.display_serfice.blit(sprite.image,offset_pos)

            
    
    def delete_Map(self):
        """removes all the tiles from a map and clears the groups"""
        self.visible_Sprites.empty()
        self.collition_Sprites.empty()
        self.event_Sprites.empty()
        del self.player





