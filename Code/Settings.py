#Screen settings 
FPS = 60
DEFAULT_WIDTH = 1500
DEFAULT_HIGHT = 800

#Tile info 
TILE_SIZE = 64

#player stats 
ANIMATION_SPEED = 1000 #Animation speed where 1000 is once per second 
player_Base_Stats = {
    "maxHealth":100,
    "speed":10,
    "jumpVelocity":-20,
    "dashVelocity": 20,
    "dashCooldown":.5
}


MAPS = {
    "testmap":["Maps\Objects_test_Background.csv","Maps\Objects_test_Objects.csv"],
    "Map3":["Maps\Map3._Player.csv","Maps\Map3._Objects.csv","Maps\Map3._Tiles.csv"],
    "Map2":["Maps\Map2_back.csv","Maps\Map2_Player.csv","Maps\Map2_deco.csv","Maps\Map2_deco2.csv","Maps\Map2_deco3.csv","Maps\Map2_Tile_Layer_2.csv"]
}

EVENT_IDS ={
    "28": "restart",
    "29": "restart",
    "95": "restart",
    "94": "restart",
    "97": "win"
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