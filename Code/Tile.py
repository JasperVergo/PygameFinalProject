class Tile:
    """the base for all tiles that are placed"""
    def __init__(self,x,y,size,groups,image):
        self.x = x
        self.y = y
        self.size = size
        self.groups = groups 
        self.image = image

