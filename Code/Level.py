from Settings import *
import pygame 
import Tile
from Support import *
import sys
from Player import Player
import Button
import ui


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

        #for all ui elements
        self.ui_elements = pygame.sprite.Group()

        #for all grass and wiggly things
        self.folliage = pygame.sprite.Group()
        ###########################################

        #get display surfice. a display surfice is what pygame draws things to
        self.display_serfice = pygame.display.get_surface()


        self.half_width = self.display_serfice.get_size()[0] // 2
        self.half_hight = self.display_serfice.get_size()[1] // 2
        self.draw_offset = pygame.math.Vector2()
        self.current_map = []
        self.is_Menu = False

        self.player = None


    


    def create_Map(self,map) -> None:
        self.delete_Map()
        """loads several maps from csv files and makes tile objects with them"""
        self.current_map = map
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
            "34":import_folder("graphics\\tileset\wall\\wall_2_flipped"),
            "68":import_folder("graphics\\deco\\flower"),
            "69":import_folder("graphics\\deco\\flower_2"),
            "70":import_folder("graphics\\deco\\flower_3"),
            "71":import_folder("graphics\\deco\\grass"),
            "72":import_folder("graphics\\deco\\grass_2"),
            "73":import_folder("graphics\\deco\\grass_3"),
            "74":import_folder("graphics\\deco\\grass_4"),
            "75":import_folder("graphics\\deco\\grass_5"),
            "76":import_folder("graphics\\deco\\grass_6"),
            "77":import_folder("graphics\\deco\\rock"),
            "78":import_folder("graphics\\deco\\rock_2"),
            "79":import_folder("graphics\\deco\\roof_grass"),
            "80":import_folder("graphics\\deco\\roof_grass_2"),
            "81":import_folder("graphics\deco\\roof_grass_3"),
            "82":import_folder("graphics\\deco\\shroom"),
            "83":import_folder("graphics\\deco\\shroom_2"),
            "84":import_folder("graphics\\tileset\\floating_platform\\Full_platform"),
            "85":import_folder("graphics\\tileset\\floating_platform\\Full_platform_2"),
            "86":import_folder("graphics\\tileset\\floating_platform\\Full_platform_3"),
            "87":import_folder("graphics\\tileset\\floating_platform\\platformend"),
            "88":import_folder("graphics\\tileset\\floating_platform\\platformend_2"),
            "90":import_folder("graphics\\tileset\\upside_down_2"),
            "91":import_folder("graphics\\tileset\\upside_down_3"),
            "92":import_folder("graphics\\tileset\\upside_down_trans"),
            "93":import_folder("graphics\\tileset\\upside_down_trans_2"),
            "94":import_folder("graphics\\spikes\\spikes_2_upsidedown"),
            "95":import_folder("graphics\\spikes\\spikes_upsidedown"),
            "96":import_folder("graphics\\tileset\\back"),
            "97":import_folder("graphics\\door\\door")
        }
        #alters the hitbox size for specific tiles
        inflations = {
            "rock":(0,0),
            "1":(28,-15),
            "2":(28,-15),
            "3":(0,0),
            "4":(0,0),
            "0":(28,-15),
            "5":(0,0),
            "6":(0,0),
            "7":(0,0),
            "8":(0,0),
            "9":(0,0),
            "10":(0,0),
            "11":(0,0),
            "12":(0,0),
            "13":(0,0),
            "14":(0,0),
            "15":(0,0),
            "16":(0,0),
            "17":(0,0),
            "18":(0,0),
            "19":(0,0),
            "20":(0,0),
            "21":(0,0),
            "22":(0,0),
            "23":(0,0),
            "24":(0,0),
            "25":(0,0),
            "26":(0,0),
            "27":(0,0),
            "28":(-10,-20),
            "29":(-10,-20),
            "30":(0,0),
            "31":(0,0),
            "32":(0,0),
            "33":(0,0),
            "34":(0,0),
            "34":(0,0),
            "35":(0,0),
            "68":(0,0),
            "69":(0,0),
            "70":(0,0),
            "71":(0,0),
            "72":(0,0),
            "73":(0,0),
            "74":(0,0),
            "75":(0,0),
            "76":(0,0),
            "77":(0,0),
            "78":(0,0),
            "79":(0,0),
            "80":(0,0),
            "81":(0,0),
            "82":(0,0),
            "83":(0,0),
            "84":(0,0),
            "85":(0,0),
            "86":(0,0),
            "87":(0,0),
            "88":(0,0),
            "90":(0,0),
            "91":(0,0),
            "92":(0,0),
            "93":(0,0),
            "94":(-10,-20),
            "95":(-10,-20),
            "96":(0,0),
            "97":(0,30)
        }

        if map == "Menu":   
            Tile.Tile(0,0,(DEFAULT_WIDTH,DEFAULT_HIGHT),[self.visible_Sprites],-1,(0,0),import_bg("graphics\screens\Start_screen"))
            Button.Button(DEFAULT_WIDTH // 2, DEFAULT_HIGHT //1.8, "graphics\\buttons\\START", 1.9,self.display_serfice,[self.ui_elements,self.visible_Sprites],self.create_Map,MAPS.get("Map2"))
            Button.Button(DEFAULT_WIDTH // 2, DEFAULT_HIGHT // 1.5, "graphics\\buttons\\Quit", 1.9,self.display_serfice,[self.ui_elements,self.visible_Sprites],self.close_game,None)
        elif map == "Restart_Menu":
             Tile.Tile(0,0,(DEFAULT_WIDTH,DEFAULT_HIGHT),[self.visible_Sprites],-1,(0,0),import_folder("graphics\screens\Pause_screen",True))
             Button.Button(DEFAULT_WIDTH // 2, DEFAULT_HIGHT // 1.9, "graphics\\buttons\\START", 3,self.display_serfice,[self.ui_elements,self.visible_Sprites],self.create_Map,MAPS.get("Map2"))
             Button.Button(DEFAULT_WIDTH // 2, DEFAULT_HIGHT // 1.5, "graphics\\buttons\\Quit", 3,self.display_serfice,[self.ui_elements,self.visible_Sprites],self.close_game,None)
        else:
            #goes through the rows and collums of a 2d list along with the index of each and checks what tile should be spawned along with 
            #calulating where it should be spawned based on the TILE_SIZE varible in Settings.py

            for layer in map:
                for row_Index,row in enumerate(import_CSV_file(layer)):
                    for col_Index, col in enumerate(row):


                        if col == "35": 
                            #loads the player, Note: if no player is pressent the program will currently
                            #  crash due to the update funtion calling it 
                            ui_padding = 10
                            self.key_w = ui.Ui_element((ui_padding * 2 + TILE_SIZE, ui_padding),(TILE_SIZE,TILE_SIZE),import_folder("Graphics\\UI\\W"),[self.ui_elements])
                            self.key_s = ui.Ui_element((ui_padding * 2 + TILE_SIZE,ui_padding * 2 + TILE_SIZE),(TILE_SIZE,TILE_SIZE),import_folder("Graphics\\UI\\S"),[self.ui_elements])
                            self.key_a = ui.Ui_element((ui_padding,ui_padding * 2 + TILE_SIZE),(TILE_SIZE,TILE_SIZE),import_folder("Graphics\\UI\\A"),[self.ui_elements])
                            self.key_d = ui.Ui_element((TILE_SIZE * 2 + ui_padding * 3,ui_padding * 2 + TILE_SIZE),(TILE_SIZE,TILE_SIZE),import_folder("Graphics\\UI\\D"),[self.ui_elements])
                            self.key_f = ui.Ui_element((TILE_SIZE * 3 + ui_padding * 5,ui_padding * 2 + TILE_SIZE),(TILE_SIZE,TILE_SIZE),import_folder("Graphics\\UI\\F"),[self.ui_elements])
                            self.dash_ui = ui.Dash_icon((DEFAULT_WIDTH - (TILE_SIZE + 20), DEFAULT_HIGHT - (TILE_SIZE + 20)),(TILE_SIZE,TILE_SIZE),[import_folder("Graphics\sphere\sphere_dash"),import_folder("Graphics\sphere\sphere")],import_folder("Graphics\sphere\sphere_dash"),[self.ui_elements])
                            self.player = Player(self.visible_Sprites,((col_Index * TILE_SIZE, row_Index * TILE_SIZE)),self.collition_Sprites,self.event_Sprites,col,self,self.folliage,self.dash_ui)

                        elif col in EVENT_IDS: # for sprites that trigger events 
                            surf = graphics.get(col)
                            Tile.Tile((col_Index * TILE_SIZE),(row_Index * TILE_SIZE),(TILE_SIZE,TILE_SIZE), [self.visible_Sprites,self.event_Sprites],col,inflations.get(col),surf)

                        elif col in ["3","4","8","19","23","27","28","29","96"]: # sprites without collision
                            surf = graphics.get(col)
                            Tile.Tile((col_Index * TILE_SIZE),(row_Index * TILE_SIZE),(TILE_SIZE,TILE_SIZE), [self.visible_Sprites],col,inflations.get(col),surf)

                        elif col in ["68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83"]: #folliage
                            surf = graphics.get(col)
                            Tile.folliage((col_Index * TILE_SIZE),(row_Index * TILE_SIZE),(TILE_SIZE,TILE_SIZE), [self.visible_Sprites,self.folliage],col,inflations.get(col),surf,self.player)

                        elif col in graphics:
                            surf = graphics.get(col)
                            Tile.Tile((col_Index * TILE_SIZE),(row_Index * TILE_SIZE),(TILE_SIZE,TILE_SIZE), [self.visible_Sprites,self.collition_Sprites],col,inflations.get(col),surf)
                            
                        elif col != "-1":
                            raise Exception(col)
                        
            self.player.event_sprites = self.event_Sprites


          
            pygame.mixer.music.load("Audio\\mixkit-forest-birds-ambience-1210.wav") #audio from https://mixkit.co/free-sound-effects/ambience/
            pygame.mixer.music.set_volume(.2)
            pygame.mixer.music.play(-1,0,1000)
    
    def update(self):
        """This is where all things that should be updated every frame """
        self.display_serfice.fill("black") #fills the screen with black to reset the sreen every frame 
        if self.current_map not in ["Restart_Menu","Menu"]:
            self.custom_draw()
            self.player.update()
            self.ui_elements.draw(self.display_serfice)
            #TODO: add culling so the game won't load the whole map but instead will load only the part the player can see   
        else:
            self.visible_Sprites.draw(self.display_serfice)
            self.ui_elements.update()
            

    def custom_draw(self):
        """custom draw to offset the camera based on the players position """
        
        self.draw_offset.x = self.player.rect.centerx - self.half_width
        self.draw_offset.y = self.player.rect.centery - self.half_hight
        #blits visible sprites and applies offset based on the player position
        for sprite in self.visible_Sprites:
            offset_pos = sprite.rect.topleft - self.draw_offset
            self.display_serfice.blit(sprite.image,offset_pos)

            
    
    def delete_Map(self):
        """removes all the tiles from a map and clears the groups"""
        self.visible_Sprites.empty()
        self.collition_Sprites.empty()
        self.event_Sprites.empty()
        self.ui_elements.empty()
        self.player = None

    def restart_map(self):
        self.delete_Map()
        self.create_Map(self.current_map)

    def close_game(self,close):
        """Closes the game"""
        pygame.event.post(pygame.QUIT)



