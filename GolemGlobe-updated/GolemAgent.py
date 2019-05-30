import random
from AgentMemory import *

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

        self.cummulativeReward = 0

        self.lastAction = None
        self.rewardForLastAction = 0
        self.lastCurrentIndex = -1
        self.lastObservationalCollection = ObservationCollection()

        self.currentObservationCollection = ObservationCollection()

        self.gamma = 0.7
        self.siFactor = 0.5
        self.randomness = 0.7

        self._fill_map(map_size_cols,map_size_rows)

        self.num_rows = map_size_rows
        self.num_cols = map_size_cols

        self.orientation = [-map_size_cols,1,map_size_cols,-1] #(delta row, delta col) for move_forward
        
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
        return self.currentMapObservations[self.indexToCurrentMapIndex(self.currentIndex)].isAgentDead()
                                           
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
                for i in list(set(expected_actions_from_current_memory.keys()).union(set(expected_actions_from_current_previous.keys()))):
                    rewardFromCurrent = 0
                    rewardFromPast = 0

                    val = 0

                    if i in expected_actions_from_current_memory.keys(): rewardFromCurrent = expected_actions_from_current_memory[i]
                    if i in expected_actions_from_current_previous.keys(): rewardFromPast = expected_actions_from_previous_memory[i]

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
        #print(obs)
        str_rep_of_obs = " ".join(list(map(lambda x: str(x),obs))).strip()
        return ObservationCollection(str_rep_of_obs)

    def updateObservationAtIndex(self,index,obs):
        toReturn = False
        if index in self.currentUnknownIndexes:
            self.currentUnknownIndexes.pop(self.currentUnknownIndexes.index(index))
            toReturn = True
        self.currentMapObservations[self.indexToCurrentMapIndex(index)] = obs
        return toReturn

    def _get_valid_actions(self):
        allMoves = actions_map.keys()
        obs_collection = self.constructObservationCollection(self.currentIndex)
        return obs_collection.get_valid_actions(allMoves)
        
    def selectAction(self):
        validMoves = self._get_valid_actions()

        expected_rewards = self.expectedRewardForAction()

        expected_rewards_for_valid_moves = {}
        for eachMove in validMoves:
            guessForReward = 0

            if eachMove in expected_rewards.keys():
                guessForReward += expected_rewards[eachMove]

            (newIndex,newAttack) = Action(actions_map[eachMove]).take_action(self.orientation,self.currentIndex,self.num_rows,self.num_cols) #simply finding index
            if self.isUnknown(newIndex) or (newAttack != -1 and self.isUnknown(newIndex)):
                guessForReward += 2
            else:
                guessForReward -= 2
            expected_rewards_for_valid_moves.update({eachMove: guessForReward})

        #print(expected_rewards_for_valid_moves)

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
            

    def update(self,newObs,obs_index,resetWhenNeeded=True):
        #calculate reward:
        exploredNewTile = self.updateObservationAtIndex(obs_index,newObs)

        lastRewardVal = 0
        needToReset = False
        if self.isAgentDead():
            lastRewardVal = -1000
            needToReset = True
        else:
            if self.isAgentOnGold():
                lastRewardVal = 1000
                needToReset = True
            else:
                if exploredNewTile:
                    lastRewardVal += 3
                    if self.lastAction.is_attack(): #attacked tile hadn't observed yet
                        if "Kill" in self.currentMapObservations[self.indexToCurrentMapIndex(obs_index)].observation_type:
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

        #update stored info:
        self.currentMemory.add(self.lastObservationCollection,self.lastAction,self.rewardForLastAction)
        self.currentActions.append(self.lastAction)
        self.previousIndex.append(self.lastCurrentIndex)
        self.cummulativeReward = self.rewardForLastAction
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

        return (newIndex,attackIndex)

    def reset(self,obsTilesToReset=[]):
        self.currentIndex = self.initalIndex
        self.previousIndex = []
        self.currentActions = []
        self.currentSteps = 0

        for i in obsTilesToReset:
            self.currentMapObservations[i].update()
        
##m = Memory()
##m.add(ObservationCollection(),"f",10,14)
###print(str(m.previous_history))
##g = GolemAgent(10,10,90,m)
##g.constructObservationCollection(90).print_observations()
###print(g.currentMapObservations)
###print(len(g.currentMapObservations))
###g.expectedRewardForAction()
##print(g.selectAction())
##print(g.selectAction())
##print(g.selectAction())
##g.constructObservationCollection(0).print_observations()
#g.currentMapObservations[0].update("U")
#for i in range(100):
#    x = g.indexToCurrentMapIndex(i)
#    y = g.currentMapIndexToIndex(x)
#    print("{} {} {}".format(i,x,y))


#to make action:
#   -call perform action
#   -get observation from map
#   -pass it to update
#   -reset if necessary
