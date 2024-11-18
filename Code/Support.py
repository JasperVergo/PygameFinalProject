import pygame
from os import walk


def import_folder(path):
    """Returns a list of pygame image objects from a folder"""
    surface = [] #stores a list of all the imported image sources 
    #makes a list of all the file names 
    filenames = next(walk(path), (None, None, []))[2] #code snipit from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    for filename in filenames:
        filePath = path + "/" + filename #makes the file path
        surface.append(pygame.image.load(filePath).convert_alpha()) #loads and appends the image found by walk
    #returns a list of pygame image object, this is used as a surfice when displaying things
    return surface

def import_CSV_file(path):
    """Imports a csv file as a 2d array where the rows are the rows of the csv file"""
    #TODO: all of it 



pygame.init() 
