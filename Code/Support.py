import pygame

def import_folder(path):
    """Returns a list of serfaces from a folder"""
    #TODO: make it import all files rn it just takes in a single file
    return pygame.image.load(path).convert_alpha()

def import_CSV_file(path):
    """Imports a csv file as a 2d array where the rows are the rows of the csv file"""
    #TODO: all of it 