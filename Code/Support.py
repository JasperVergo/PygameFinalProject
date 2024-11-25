import pygame
from os import walk
from Settings import TILE_SIZE
import csv
from os import path as osPath


def import_folder(path):
    """Returns a list of pygame image objects from a folder if no files are found returns a empty list"""
    surface = [] #stores a list of all the imported image sources 
    #makes a list of all the file names 
    filenames = next(walk(osPath.join(*path.split("\\"))), (None, None, []))[2] #code snipit from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    if len(filenames) > 0:
        for filename in filenames:
            filePath = osPath.join(*path.split("\\"), filename)
            image = pygame.image.load(filePath).convert_alpha()
            image = pygame.transform.scale(image, (TILE_SIZE,TILE_SIZE))
            surface.append(image) #loads and appends the image found by walk
        #returns a list of pygame image object, this is used as a surfice when displaying things
    else:
        return osPath.join(*(path + ".png").split("\\")) 
    return surface

def import_CSV_file(path):
    """Imports a csv file as a 2d array where the rows are the rows of the csv file"""
    #TODO: all of it 
    with open(path,"r") as mapLayer:
        pass

