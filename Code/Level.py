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
        #TODO: fix this so the hitboxes are right
        graphics = {           
            "rock":import_folder("Graphics\Test"),
            "1":import_folder("graphics\\tileset\\floating_platform\\platform_2"),
            "2":import_folder("graphics\\tileset\\floating_platform\\platform_3"),
            "3":import_folder("graphics\\tileset\\floating_platform\\platform_end_left"),
            "4":import_folder("graphics\\tileset\\floating_platform\\platform_end_right"),
            "0":import_folder("graphics\\tileset\\floating_platform\\platform"),
            "5":import_folder("graphics\\tileset\\floor\\floor_1"),
            "6":import_folder("graphics\\tileset\\floor\\floor_2"),
            "7":import_folder("graphics\\tileset\\floor\\floor_3"),
            "8":import_folder("graphics\\tileset\\floor\\floor_void"),
            "9":import_folder("graphics\\tileset\\floor_up\\floor_up_corner_left"),
            "10":import_folder("graphics\\tileset\\floor_up\\floor_up_corner_right"),
            "11":import_folder("graphics\\tileset\\floor_up\\floor_up_left"),
            "12":import_folder("graphics\\tileset\\floor_up\\floor_up_right"),
            "13":import_folder("graphics\\tileset\\floor_up\\floor_up_trans_left"),
            "14":import_folder("graphics\\tileset\\floor_up\\floor_up_trans_right"),
            "15":import_folder("graphics\\tileset\\floor_up\\floor_up2_trans"),
            "16":import_folder("graphics\\tileset\\roof\\roof_1"),
            "17":import_folder("graphics\\tileset\\roof\\roof_2"),
            "18":import_folder("graphics\\tileset\\roof\\roof_3"),
            "19":import_folder("graphics\\tileset\\roof\\roof_void"),
            "20":import_folder("graphics\\tileset\\transitions\\wall_floor_corner"),
            "21":import_folder("graphics\\tileset\\transitions\\wall_floor_void"),
            "22":import_folder("graphics\\tileset\\transitions\\wall_roof_corner"),
            "23":import_folder("graphics\\tileset\\transitions\\wall_roof_void"),
            "24":import_folder("graphics\\tileset\\wall\\wall_1"),
            "25":import_folder("graphics\\tileset\\wall\\wall_2"),
            "26":import_folder("graphics\\tileset\\wall\\wall_3"),
            "27":import_folder("graphics\\tileset\\wall\\wall_void"),
            "28":import_folder("graphics\\spikes\\spikes"),
            "29":import_folder("graphics\spikes\spikes_2"),
            "30":import_folder("graphics\\tileset\\transitions\\wall_floor_corner_flipped"),
            "31":import_folder("graphics\\tileset\\transitions\\wall_roof_corner_flipped"),
            "32":import_folder("graphics\\tileset\wall\\wall_3_flipped"),
            "33":import_folder("graphics\\tileset\wall\\wall_1_flipped"),
            "34":import_folder("graphics\\tileset\wall\\wall_2_flipped")
        }

        #goes through the rows and collums of a 2d list along with the index of each and checks what tile should be spawned along with 
        #calulating where it should be spawned based on the TILE_SIZE varible in Settings.py

        for layer in map:
            for row_Index,row in enumerate(import_CSV_file(layer)):
                for col_Index, col in enumerate(row):


                    if col == "35": 
                        #loads the player, Note: if no player is pressent the program will currently
                        #  crash due to the update funtion calling it 
                        self.player = Player(self.visible_Sprites,((col_Index * TILE_SIZE, row_Index * TILE_SIZE)),self.collition_Sprites,col)
                    elif col in ["3","4","8","19","23","27","28","29"]: # sprites without collision
                        surf = graphics.get(col)
                        Tile.Tile((col_Index * TILE_SIZE),(row_Index * TILE_SIZE),TILE_SIZE, [self.visible_Sprites],col,surf)
                    elif col in graphics:
                        surf = graphics.get(col)
                        Tile.Tile((col_Index * TILE_SIZE),(row_Index * TILE_SIZE),TILE_SIZE, [self.visible_Sprites,self.collition_Sprites],col,surf)
                    elif col != "-1":
                        raise Exception(col)

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





