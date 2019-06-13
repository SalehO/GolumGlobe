import random
from AgentMemory import *
from ActionHistory import *
from Stats import *

class GolemAgent:
    def __init__(self,map_size_rows,map_size_cols,inital_index,previousMemory):
        #self.currentMapObservations = [Observation()]*map_size_cols*map_size_rows #NO Walls
        self.currentMapObservations = [None]*(map_size_cols+2)*(map_size_rows+2)
        self.currentIndex = inital_index
        self.initalIndex = inital_index

        self.previousMemory = previousMemory
        
        self.currentMemory = Memory()
        self.currentUnknownIndexes = []

        self.previousIndex = []
        self.currentSteps = 0
        
        self.currentActioNumber = 0
        self.previousActions = []
        self.rewardForAction = []

        self.stats = Stats()

        self.hasFallenIndexes = []
        self.killedGolemAtIndex = []


        self.cummulativeReward = 0

        self.lastAction = None
        self.rewardForLastAction = 0
        self.lastCurrentIndex = -1
        self.lastObservationalCollection = ObservationCollection()

        self.currentObservationCollection = ObservationCollection()

        self.currentActionHistory = ActionHistory()

        self.gamma = 0.2
        self.siFactor = 0.2
        self.randomness = 0.35
        self.risk = 0.75
        self.exploration = 1.0

        self._fill_map(map_size_cols,map_size_rows)

        self.num_rows = map_size_rows
        self.num_cols = map_size_cols

        self.totalTiles = self.num_rows*self.num_cols

        self.orientation = [-map_size_cols,1,map_size_cols,-1] #(delta row, delta col) for move_forward

    def reachedMaxStepCount(self):
        return self.currentSteps  > 150 #will reset it
        
    def saveMemory(self,path):
        self.currentMemory.saveMemory(path)

    def loadMemory(self,path):
        self.previousMemory.loadMemory(path)
        
    def _fill_map(self,map_size_cols,map_size_rows):
        for i in range(map_size_cols+2):
            self.currentMapObservations[i] = Observation("Wall")
        offset = map_size_cols + 2
        for i in range(map_size_rows):
            self.currentMapObservations[offset] = Observation("Wall")
            offset += 1
            for j in range(map_size_cols):
                self.currentMapObservations[offset] = Observation("Unknown")
                offset += 1
            self.currentMapObservations[offset] = Observation("Wall")
            offset += 1
        for i in range(map_size_cols+2):
            self.currentMapObservations[offset+i] = Observation("Wall")

        for i in range(map_size_cols*map_size_rows): self.currentUnknownIndexes.append(i)

    def isAgentDead(self):
        return self.currentMapObservations[self.indexToCurrentMapIndex(self.currentIndex)].isAgentDead() or self.reachedMaxStepCount()
                                           
    def isAgentOnGold(self):
        return self.currentMapObservations[self.indexToCurrentMapIndex(self.currentIndex)].isGoldOnTile()

    def isUnknown(self,index):
        return self.currentMapObservations[self.indexToCurrentMapIndex(index)].isUnknown()

    def finished(self):
        return self.isAgentOnGold()

    def needToReset(self):
        return self.isAgentDead()

    def indexToCurrentMapIndex(self,index):
        row = index//self.num_cols
        col = index%self.num_cols
        return (self.num_cols) + 2*(row+1) + (row*self.num_cols) + col + 1

    def currentMapIndexToIndex(self,currentMapIndex):
        row = currentMapIndex//(self.num_cols+2)
        col = currentMapIndex%(self.num_cols+2)
        #print(row,col)
        return (row-1)*self.num_cols + (col - 1)

    def expectedRewardForAction(self):
        expected_actions_from_previous_memory = {}
        expected_actions_from_current_memory = {}

        expected = {}
        if self.previousMemory.hasEncounteredScenario(self.currentObservationCollection):
            expected_actions_from_previous_memory = self.previousMemory.expected_reward_for_action(self.currentObservationCollection,True,self.gamma)
        if self.currentMemory.hasEncounteredScenario(self.currentObservationCollection):
            expected_actions_from_current_memory = self.currentMemory.expected_reward_for_action(self.currentObservationCollection,True,self.gamma)

        if len(expected_actions_from_previous_memory) > 0: #has encountered from previous memory
            if len(expected_actions_from_current_memory) > 0: #has encountered from current map
                for i in list(set(expected_actions_from_current_memory.keys()).union(set(expected_actions_from_previous_memory.keys()))):
                    rewardFromCurrent = 0
                    rewardFromPast = 0

                    val = 0

                    if i in expected_actions_from_current_memory.keys(): rewardFromCurrent = expected_actions_from_current_memory[i] * 0.5
                    if i in expected_actions_from_previous_memory.keys(): rewardFromPast = expected_actions_from_previous_memory[i] * 0.5
                    #if i in expected_actions_from_current_memory.keys(): rewardFromCurrent = expected_actions_from_current_memory[i]
                    #if i in expected_actions_from_previous_memory.keys(): rewardFromPast = expected_actions_from_previous_memory[i]

                    if rewardFromCurrent == 0 or rewardFromPast == 0:
                        val = rewardFromCurrent + rewardFromPast
                    else:
                        val = (1.0 - self.siFactor)*rewardFromCurrent + (self.siFactor)*rewardFromPast

                    expected.update({i:val})
                    
            else:
                expected = expected_actions_from_previous_memory
        else: #has not enountered from previous memory
            if len(expected_actions_from_current_memory) > 0: #has encountered from current map
                expected = expected_actions_from_current_memory
                
        return expected

    def indexToRowCol(self, index):
        return (index//self.num_rows,index%self.num_rows)


    def distanceBetweenIndexes(self,index0,index1):
        (row0,col0) = self.indexToRowCol(index0)
        (row1,col1) = self.indexToRowCol(index1)
        return abs(row0-row1) + abs(col0-col1)

    def getDistanceBetweenIndexAndAllUnknown(self,index):
        totalDistance = 0
        for i in self.currentUnknownIndexes:
            totalDistance += self.distanceBetweenIndexes(index,i)
        return totalDistance

    def getDistanceWeightIndex(self,index):
        totalDistance = self.getDistanceBetweenIndexAndAllUnknown(index)
        return ((self.totalTiles/(len(self.currentUnknownIndexes) + 1))*((self.num_rows*self.num_cols)/(totalDistance + 1)))

    def constructObservationCollection(self,index):
        mapIndex = self.indexToCurrentMapIndex(index)
        #numpad configuration, index at position 5:
        obs = [self.currentMapObservations[mapIndex -(self.num_cols+2) + 1], #7 on numpad
               self.currentMapObservations[mapIndex + 1], #8 on numpad
               self.currentMapObservations[mapIndex +(self.num_cols+2) + 1], #9 on numpad
               self.currentMapObservations[mapIndex - (self.num_cols+2)],#4 on numpad
               self.currentMapObservations[mapIndex],#5 on numpad
               self.currentMapObservations[mapIndex + (self.num_cols+2)],#6 on numpad
               self.currentMapObservations[mapIndex - (self.num_cols+2) - 1],#1 on numpad
               self.currentMapObservations[mapIndex - 1],#2 on numpad
               self.currentMapObservations[mapIndex +(self.num_cols+2) - 1]#3 on numpad
               ]
        to_str = []
        str_rep_of_obs = " ".join(list(map(lambda x: str(x),obs)))
        print(str_rep_of_obs)
        return ObservationCollection(str_rep_of_obs)

    def updateObservationAtIndex(self,index,obs):
        toReturn = False
        #print(self.currentUnknownIndexes)
        if index in self.currentUnknownIndexes:
            self.currentUnknownIndexes.pop(self.currentUnknownIndexes.index(index))
            toReturn = True
        self.currentMapObservations[self.indexToCurrentMapIndex(index)] = obs
        return toReturn

    def _get_valid_actions(self):
        allMoves = actions_map.keys()
        obs_collection = self.constructObservationCollection(self.currentIndex)
        return obs_collection.get_valid_actions(allMoves)

    def obsAtIndex(self,index):
        return self.currentMapObservations[self.indexToCurrentMapIndex(self.currentIndex)]
        
    def selectAction(self):
        validMoves = self._get_valid_actions()

        expected_rewards = self.expectedRewardForAction()
        print("Current obs: {}".format(self.obsAtIndex(self.currentIndex)))

        expected_rewards_for_valid_moves = {}
        for eachMove in validMoves:
            guessForReward = 0

            if eachMove in expected_rewards.keys():
                guessForReward += expected_rewards[eachMove]

            action = Action(actions_map[eachMove])
            (newIndex,newAttack) = action.take_action(self.orientation,self.currentIndex,self.num_rows,self.num_cols) #simply finding index
            if self.isUnknown(newIndex) or (newAttack != -1 and self.isUnknown(newIndex)):
                guessForReward += 2

            #handle golem
            if self.obsAtIndex(self.currentIndex).isSmell():
                if self.isUnknown(newAttack):
                    if action.is_move():
                        guessForReward -= 150
                    else:
                        guessForReward += 150
            else:
                if not action.is_move(): #penalty for hitting wildly
                    guessForReward -= 500

            #handle pit:
            if self.obsAtIndex(self.currentIndex).isBreeze():
                if action.is_move():
                    if newIndex in self.hasFallenIndexes:
                        guessForReward = -10000 #don't fall in same pit
                    elif self.isUnknown(newIndex):
                        #guessForReward = -100
                        guessForReward += 0
                    #else:
                    #   guessForReward -= self.getDistanceWeightIndex(newIndex) #may only attack now?

            if action.is_move():
                if self.isUnknown(newIndex):
                    if not self.obsAtIndex(self.currentIndex).isBreeze() and not self.obsAtIndex(self.currentIndex).isSmell():
                        guessForReward += (self.num_rows*self.num_cols)/(len(self.currentUnknownIndexes) + 1 * 1.0) * self.exploration
                #else:
                guessForReward += self.getDistanceWeightIndex(newIndex)
            else:
                if self.obsAtIndex(newAttack).isMauled():
                    guessForReward += 1000
                
            expected_rewards_for_valid_moves.update({eachMove: guessForReward})
        #print(expected_rewards_for_valid_moves)
        #b = input()

        bestActions = []
        bestActionVal = 0
        goodActions = []
        badActions = []
        terribleActions = []

        for (k,v) in sorted(expected_rewards_for_valid_moves.items(),key = lambda x: x[1], reverse = True):
            if len(bestActions) == 0:
                bestActionVal = v
                bestActions.append(k)
            elif v == bestActionVal:
                bestActions.append(k)
            elif v > 0:
                goodActions.append(k)
            elif v >= -500:
                badActions.append(k)
            else:
                terribleActions.append(k)


        if random.random() > self.randomness:
            act_str = random.choice(bestActions)
        else:
            positiveChoices = bestActions + goodActions
            if random.random() > self.randomness:
                act_str = random.choice(positiveChoices)
            else:
                notTerrible = positiveChoices + badActions
                if random.random() > self.risk:
                    act_str = random.choice(notTerrible)
                else:
                    allChoices = notTerrible + terribleActions
                    act_str = random.choice(allChoices)

        return Action(actions_map[act_str])
        """
        #find best guess:
        maxGuessReward = 0
        maxActions = []
        otherActions = []
        #for (k,v) in sorted(expected_rewards_for_valid_moves.items(),key = lambda x: x[1], reverse = True):
        for (k,v) in expected_rewards_for_valid_moves.items():
            if v > maxGuessReward or maxActions == []:
                otherActions.extend(maxActions)
                maxActions = [k]
                maxGuessReward = v
            elif v == maxGuessReward:
                maxActions.append(k)
            else:
                otherActions.append(k)

        #pick:
        #print(maxActions,otherActions)
        if random.random() > self.randomness or (len(otherActions) == 0 and len(maxActions) != 0):
            act_str = random.choice(maxActions)
        else:
            act_str = random.choice(otherActions)

        #print(actions_map[act_str])
        return Action(actions_map[act_str])
        """    

    def update(self,newObs,obs_index,resetWhenNeeded=True):
        #calculate reward:
        exploredNewTile = self.updateObservationAtIndex(obs_index,newObs)

        if newObs.isFall():
            self.hasFallenIndexes.append(obs_index)
        #print(newObs)

        lastRewardVal = 0
        needToReset = False
        if self.isAgentDead():
            lastRewardVal = -10000
            needToReset = True
        else:
            if self.isAgentOnGold():
                lastRewardVal = 1000
                needToReset = True
            else:
                if exploredNewTile:
                    lastRewardVal += 3
                    if self.lastAction.is_attack(): #attacked tile hadn't observed yet
                        if "Killed" in self.currentMapObservations[self.indexToCurrentMapIndex(obs_index)].observation_type:
                            lastRewardVal += 250
                        else:
                            lastRewardVal -= 20
                    else:
                        lastRewardVal -= 2 #for taking a step
                else:
                    if self.lastAction.is_attack():
                        lastRewardVal -= 100

                    else:
                        lastRewardVal -= 2

        self.rewardForLastAction = lastRewardVal
        self.rewardForAction.append(lastRewardVal)

        self.currentActionHistory.add(self.currentObservationCollection,self.lastAction,lastRewardVal)

        #update stored info:
        #self.currentMemory.add(self.lastObservationCollection,self.lastAction,self.rewardForLastAction)
        #self.currentActions.append(self.lastAction)
        self.previousIndex.append(self.lastCurrentIndex)
        #self.cummulativeReward = self.rewardForLastAction
        self.currentObservationCollection = self.constructObservationCollection(self.currentIndex)
        
        
            

    def performAction(self):
        action = self.selectAction()
        (newIndex,attackIndex) = action.take_action(self.orientation,self.currentIndex,self.num_rows,self.num_cols)

        #update cached values:
        self.lastCurrentIndex = self.currentIndex
        self.lastAction = action
        #print("last act",self.lastAction)
        self.lastObservationCollection = self.currentObservationCollection

        #make move:
        self.currentIndex = newIndex
        self.currentSteps += 1
        self.currentActioNumber += 1


        return (newIndex,attackIndex)

    def calculateFinalRewards(self):
        weightedRewards = []
        for i in range(self.currentActioNumber):
            index = len(self.currentActioNumber) - i

    def _reset_action_history(self):
        toParse = self.currentActionHistory.reset(self.gamma)
        for (c,a,r,fr) in toParse:
            self.currentMemory.add(c,a,r,fr) 

    def reset(self,obsTilesToReset=[]):

        if len(self.currentActionHistory.rewards) > 1:
            self.stats.add(self.rewardForLastAction,self.currentActionHistory._get_final_reards(self.gamma),self.currentSteps,self.isAgentOnGold())
            print(self.stats)

        print(self.currentActionHistory)

        self._reset_action_history()
        
        self.currentIndex = self.initalIndex
        self.previousIndex = []
        self.currentActions = []
        self.currentSteps = 0

        for i in obsTilesToReset:
            self.currentMapObservations[i].update()

        #self.calculateFinalRewards()

        self.currentActioNumber = 0
        self.previousActions = []
        self.rewardForAction = []
        
