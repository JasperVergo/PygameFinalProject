
import pygame 
from Settings import *
import Level
  
def main():

    pygame.init() 
    
    #CREATING THE CANVAS 
    canvas = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HIGHT)) 
    clock = pygame.time.Clock()
    pygame.display.set_caption("Mini RPG") 
    exit = False

    #Creating the map
    level = Level.Level()
    
    #game loop 
    while not exit: 
        for event in pygame.event.get(): 
            #cleans up after closing the program 
            if event.type == pygame.QUIT: 
                exit = True
        #updates the display
        pygame.display.update() 
        clock.tick(FPS)


main()