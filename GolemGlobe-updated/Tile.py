
tiles = {"CLEAR":"B","GOLEM":"G","PIT":"P","EXIT":"E","TREASURE":"T"}
obsForAdjacentToTile = {"CLEAR":"","GOLEM":"Smell","PIT":"Breeze","EXIT":"","TREASURE":""}
obsForTile = {"CLEAR":"","GOLEM":"Mauled","PIT":"Fell","EXIT":"","TREASURE":"Glitter"}

def isValidType(tile_type):
    return tile_type in tiles.keys()


def getTypeString(tile_type):
    if isValidType(tile_type):
        return tiles[tile_type]
    else:
        return tiles["CLEAR"]

def getTileTypeFromStrig(string):
    for (k,v) in tiles.items():
        if v == string:
            return k
    return "CLEAR"



class Tile:
    def __init__(self,row_num,col_num,tile_type="CLEAR"):
        self.type = tile_type
        self.row = row_num
        self.col = col_num

        self.containsGolem = False
        self.containsPit = False
        self.conatinsTreasure = False

        #self.isEntrance = False
        #self.isExit = False

        self.isAdjacentToGolem = False
        self.isAdjacentToPit = False
        self.isAdjacentToTreasure = False

    def isExit(self):
        return self.type == "EXIT"

    def position(self):
        return (self.row,self.col)

    def attack(self):
        if self.type == "GOLEM":
            self.updateTileType("CLEAR")
            return True
        else:
            return False

    def updateTileType(self,tile_type):
        self.type = tile_type

    def getAllPossibleNeighbors(self):
        return [(self.row-1,self.col-1),
                (self.row-1,self.col),
                (self.row-1,self.col+1),
                (self.row,self.col-1),
                (self.row,self.col+1),
                (self.row+1,self.col-1),
                (self.row+1,self.col),
                (self.row+1,self.col+1)]

    def getPossibleAdjacentTiles(self):
        return [(self.row-1,self.col),
                (self.row,self.col-1),
                (self.row,self.col+1),
                (self.row+1,self.col)]

    def getAdjacentObservation(self):
        return obsForAdjacentToTile[self.type]

    def getObservationForStand(self):
        return obsForTile[self.type]
    

    def __repr__(self):
        return "{}".format(getTypeString(self.type))

    
