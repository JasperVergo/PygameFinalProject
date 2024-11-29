#Screen settings 
FPS = 60
DEFAULT_WIDTH = 1080
DEFAULT_HIGHT = 720

#Tile info 
TILE_SIZE = 64

#player stats 
ANIMATION_SPEED = 1000 #Animation speed where 1000 is once per second 
player_Base_Stats = {
    "maxHealth":100,
    "speed":10,
    "jumpVelocity":-20,
    "dashVelocity": 40,
    "dashCooldown":.5
}


MAPS = {
    "testmap":["Maps\Objects_test_Background.csv","Maps\Objects_test_Objects.csv"]
}

#temperary map for testing   
MAP = [
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,1,1,1,1,1,1,1,1,0,1,1,1,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
       [0,1,0,1,1,0,0,1,0,1,1,0,1,1,0],
       [0,1,0,0,0,0,"P",0,0,0,0,0,0,0,0],
       [0,1,0,0,1,0,0,1,1,0,0,0,1,1,0],
       [0,1,1,1,1,0,0,1,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,1,1,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,1,1,0,0,0,1,1,0,1,0,1,0,0],
       [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,1,0,1,0,1,0,0],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
       ]