from collections import defaultdict
from ObservationCollection import ObservationCollection,Observation
from Reward import Reward, Action, actions_map

class Memory:
    def __init__(self):
        self.previous_history = defaultdict(list)
        self.isEmpty = True
        
    def add(self,collection,action,reward,final_reward=0):
        try:
            self.previous_history[str(collection)].append(Reward(action,reward,final_reward))
            self.isEmpty = False
        except:
            pass

    def mergeMemory(self,memory):
        for key in memory.previous_history:
            for each_val in memory.previous_history[key]:
                self.previous_history.append(each_val)
        
    def hasEncounteredScenario(self,collection):
        #print(str(collection))
        return str(collection) in self.previous_history.keys()
    def get_rewards(self,collection,final_rewards=False):
        toReturn = defaultdict(list)
        if self.hasEncounteredScenario:
            for each_reward in self.previous_history[str(collection)]:
                if final_rewards:
                    toReturn[str(each_reward.action)].append(each_reward.final_reward)
                else:
                    toReturn[str(each_reward.action)].append(each_reward.reward_val)
        return toReturn
    def get_max_reward_vals(self,collection):
        maxVals = {}
        if self.hasEncounteredScenario:
            toParse = self.get_rewards(collection)
            for (k,v) in toParse.items():
                maxVals[k] = max(v)
        return maxVals

    def get_avg_reward_vals(self,collection):
        avgVals = {}
        if self.hasEncounteredScenario:
            toParse = self.get_rewards(collection)
            for (k,v) in toParse.items():
                avgVals[k] = sum(v)/(len(v) * 1.0)
        return avgVals

    def get_max_final_rewards(self,collection):
        maxVals = {}
        if self.hasEncounteredScenario:
            toParse = self.get_rewards(collection,True)
            for (k,v) in toParse.items():
                maxVals[k] = max(v)
        return maxVals

    def get_avg_final_rewards(self,collection):
        avgVals = {}
        if self.hasEncounteredScenario:
            toParse = self.get_rewards(collection,True)
            for (k,v) in toParse.items():
                avgVals[k] = sum(v)/(len(v) * 1.0)
        return avgVals

    def expected_reward_for_action(self,collection,average=True,gamma=0.0):
        toParse = {}
        if average:
            reward_vals = self.get_avg_reward_vals(collection)
            final_rewards = self.get_avg_final_rewards(collection)
        else:
            reward_vals = self.get_max_reward_vals(collection)
            final_rewards = self.get_max_final_rewards(collection)
        for key in final_rewards:
            val = ((1 - gamma) * reward_vals[key]) + (gamma*final_rewards[key])
            toParse.update({key:val})
        return toParse
                
            
    def best_actions(self,collection,average=True,gamma=0.0):
        toReturn = []
        best = -1
        toParse = self.expected_reward_for_action(collection,average,gamma)
        for key in toParse:
            if toReturn == [] or best < toParse[key]:
                toReturn = [key]
                best = toParse[key]
            elif best == toParse[key]:
                toReturn.append(key)
        return toReturn

    def __repr__(self):
        toReturn = ""
        for obs_str in self.previous_history.keys():
            toReturn += obs_str + ":\n"
            for act in self.previous_history[obs_str]:
                toReturn += "\t" + str(act) + "\n"
        return toReturn

    def saveMemory(self, path):
        file = open(path,"a+")
        file.write(self.__repr__())
        file.close()

    def loadMemory(self, path):
        with open(path) as file:
            obsCollection = None
            for line in file.readlines():
                if line[0] == "\t":
                    actReward = line.replace("\t","").replace("(","").replace(")","").split(":")

                    actStr = actions_map[actReward[0]]
                    action = Action(actStr)
                    shortTermReward = float(actReward[1])
                    longTermReward = float(actReward[2])

                    self.add(obsCollection,action,shortTermReward,longTermReward)
                    
                else:
                    obsString = line.replace(":","").strip()
                    obsCollection = ObservationCollection(obsString)
                    
    def getVals(self):
        for collection in self.previous_history.keys():
            c = ObservationCollection(collection)
            needToPrint = False
            theMax = self.get_max_final_rewards(c)
            for (k,v) in sorted(self.get_avg_reward_vals(c).items(),key = lambda x: x[1]):
                if v < -1000:
                    print("{}: {}: {} {}\n".format(c,k,v,theMax[k]))
                else:
                    continue


if __name__ == "__main__":
    m = Memory()
    m.loadMemory("C:\\Users\\wills\\Desktop\\CS_175\\cummulativeMemory.txt")
    m.getVals()
        
