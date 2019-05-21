from Tile import Tile, getTileTypeFromStrig
from Observation import *
from random import randrange
import os

class Board:
    def __init__(self,loadMap = ""):
        self.rows = 0
        self.cols = 0

        self.board = []

        self.numberOfGolems = 1
        self.numberOfPits = 1
        self.numberOFPits = 1

        self.mapName = ""
        self.notes = ""
        self.encodingVersion = 1

        self.isInitalized = False

        self.currentRow = -1
        self.currentCol = -1
        self.currentIndex = -1

        self.initalIndex = -1

        if loadMap != "":
            self.loadMapFromFile(loadMap)
            print(self)

    def loadBoard(self,board_as_list_of_strings,rows,cols):
        self.rows = rows
        self.cols = cols

        for index in range(self.rows * self.cols):
            self.board.append(Tile(index//self.rows,index%self.rows,tile_type = getTileTypeFromStrig(board_as_list_of_strings[index])))
        self.isInitalized = True
        self.initalizePosition()

    def isValidRowCol(self,row_num,col_num):
        if self.isInitalized:
            return (row_num in range(0,self.rows)) and (col_num in range(0,self.cols))
        else:
            False

    def rowColToIndex(self,rows,cols):
        return self.cols*rows + cols

    def getAdjacentTiles(self,tile):
        adjacentTiles = []
        #print(tile)
        for (row,col) in tile.getPossibleAdjacentTiles():
            #print(row,col)
            if self.isValidRowCol(row,col):
                adjacentTiles.append((row,col))
        return adjacentTiles
            


    def generate(self,rows,cols):
        self.rows = rows
        self.cols = cols
                              
        for index in range(self.rows * self.cols):
            self.board.append(Tile(index//self.rows,index%self.rows))

        self.isInitalized = True

        #For now:
        #   place exit/entrance in bottom left
        #   walk 5 tiles before placing treasure
        bottomLeftIndex = (self.rows - 1) * self.cols
        self.board[bottomLeftIndex].updateTileType("EXIT")

        currentPos = ((self.rows - 1), 0)
        stepsLeft = 15
        visited = set()
        while(stepsLeft > 0):
            currentTile = self.board[self.rowColToIndex(currentPos[0],currentPos[1])]
            adjacentTiles = self.getAdjacentTiles(currentTile)
            while True:
                nextTile = adjacentTiles[randrange(len(adjacentTiles))]
                if (nextTile[0]*self.cols + nextTile[1] != bottomLeftIndex):
                    break
            visited.add(currentPos)
            currentPos = nextTile
            

            stepsLeft-=1

            
        #check not exit square:
        print(visited)
        print(currentPos)
        treasureIndex = (currentPos[0]*self.cols) + currentPos[1]
        self.board[treasureIndex].updateTileType("TREASURE")

    def loadMapFromFile(self,file_path):
        hasSeenHeader = False
        encodingVersion = self.encodingVersion
        the_map = []
        last_row_length = -1
        
        if os.path.isfile(file_path):
            with open(file_path) as mapFile:
                for line in mapFile.readlines():
                    if line[0] == "#":
                        self.notes += line[1:]
                    elif not hasSeenHeader:
                        toProcess = line.strip().split(":")
                        if toProcess[0] == "GolemGlobe_map":
                            toProcess = toProcess[1].split(" ")
                            if len(toProcess) == 2:
                                self.mapName = toProcess[0]
                                encodingStr = toProcess[1].split("=")
                                if len(encodingStr) == 2 and encodingStr[0].strip() == "encoding":
                                    self.encodingVersion = encodingStr[1]
                                else:
                                    print("error: invalid encoding substring")
                                    return
                            else:
                                print("error: invalid name/encoding substring")
                                return
                            hasSeenHeader = True
                        else:
                            print("error: invalid header")
                            return
                            
                    else:
                        currentRow = []
                        for i in line.strip():
                            currentRow.append(i)
                        if last_row_length == -1 or len(currentRow) == last_row_length:
                            the_map.extend(currentRow)
                            last_row_length = len(currentRow)
                        else:
                            print("error: rows are different lengths")
                            return
        else:
            print("error: {} is an invalid filepath.".format(file_path))
            return

        self.loadBoard(the_map,len(the_map)//last_row_length,last_row_length)
        

    def initalizePosition(self):
        if self.isInitalized:
            for index in range(len(self.board)):
                if self.board[index].isExit():
                    self.currentRow = index//self.rows
                    self.currentCol = index%self.rows
                    self.currentIndex = index
                    self.initalIndex = index
                    return
            print("error: No exit found.")
            return
        else:
            print("error: can't initalize starting postition, map itself is not initalized.")


    def reset(self):
        self.currentIndex = self.initalIndex 
    def tileAtIndex(self,index=-1):
        if index == -1:
            return self.board[self.currentIndex]
        else:
            return self.board[index]

    def getIndexOfValidMoves(self,index=-1):
        currentTile = self.tileAtIndex(index)
        possibleMoves = currentTile.getPossibleAdjacentTiles()

        moves = []

        for eachMove in possibleMoves:
            (row,col) = eachMove
            if row in range(self.rows) and col in range(self.cols):
                moves.append(self.rows*row+col)

        return moves

    def getObservationForIndex(self,index=-1):
        checkIndex = self.currentIndex if index == -1 else index

        adjTiles = self.getIndexOfValidMoves(index)
        obs_type = []
        for eachTile in adjTiles:
            obs_type.append(self.board[eachTile].getAdjacentObservation())
        obs_type.append(self.tileAtIndex().getObservationForStand())

        obs_type = list(set(obs_type))

        return Observation(index//self.rows,index%self.rows,checkIndex,obs_type)
        
                

    def __repr__(self):
        toReturn = ""
        toReturn += "GolemGlobe: Map = {}, Size = {}x{}\n\n".format(self.mapName,self.rows,self.cols)
        for i in range(self.rows):
            currentRow = ""
            for j in range(self.cols):
                currentRow += self.board[self.rowColToIndex(i,j)].__repr__() + " "
            currentRow += "\n"
            toReturn += currentRow
        return toReturn

    def print(self):
        print(self)

b = Board("C:\\Users\\wills\\Desktop\\CS_175\\maps\\test.txt")
print(b.getIndexOfValidMoves())
#b.generate(10,10)
    
