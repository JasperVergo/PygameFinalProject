from Settings import *
import pygame 
import Tile


class Level():

    def __init__(self):
        pass

    def create_Map(map : list) -> None:
        """loads several maps from csv files and makes tile objects with them"""


        for row in MAP:
            for col in row:
                if col == "1":
                    Tile.Tile((col * TILE_SIZE) + TILE_SIZE // 2,(row * TILE_SIZE) + TILE_SIZE // 2,None)
                elif col == "0":
                    Tile.Tile((col * TILE_SIZE) + TILE_SIZE // 2,(row * TILE_SIZE) + TILE_SIZE // 2,None)
                


    def update():
        """creates the map tiles from several layers of csv files"""
        
        pass
