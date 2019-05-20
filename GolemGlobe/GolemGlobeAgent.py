import random
from collections import defaultdict

class GolemGlobeAgent:
    def __init__(self,map_size_rows,map_size_cols,inital_index):
        self.observations = [None]*map_size_cols*map_size_rows

        self.currentIndex = inital_index
        self.initalIndex = inital_index

        self.previousIndex = []
        self.currentActions = []
        self.currentSteps = 0
        self.currentTotalReward = 0

        self.prveviousRewardsFromTiles = [[]]*map_size_cols*map_size_rows
        #print(self.prveviousRewardsFromTiles)

    def needToReset(self):
        return self.observations[self.currentIndex].needToReset()

    def finished(self):
        return self.observations[self.currentIndex].finished()
    
    def moveToIndex(self,newIndex):
        self.previousIndex.append(self.currentIndex)
        self.currentIndex = newIndex

        self.currentSteps += -1
        self.currentTotalReward = self.currentSteps * -1

    def averageFromIndex(self,index):
        the_list = self.prveviousRewardsFromTiles[index]
        if len(the_list) == 0:
            return 0
        else:
            return sum(the_list)/len(the_list)

    def bestMoves(self):
        moves = defaultdict(list)

        for index in self.currentActions:
            val = self.averageFromIndex(index)
            moves[val].append(index)

        return moves[max(moves.keys())]
    
    def selectAction(self):
        randomness = 0.5

        if random.random() > randomness:
            #best move
            return random.choice(self.bestMoves())
        else:
            return random.choice(self.currentActions)

        
        

    def reset(self):
        for eachIndex in self.previousIndex:
            self.prveviousRewardsFromTiles.append(self.currentTotalReward)

        
        self.currentIndex = self.initalIndex
        self.previousIndex = []
        self.currentActions = []
        self.currentSteps = 0

