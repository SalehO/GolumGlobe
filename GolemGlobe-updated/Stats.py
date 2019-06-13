class Stats:
    def __init__(self):
        self.lastRewardVals = []
        self.cummulativeRewardVals = []
        self.foundGold = []
        self.totalSteps = []

    def add(self,lastReward,cr,ts,foundGold=False,printRun=True):
        self.lastRewardVals.append(lastReward)
        self.totalSteps.append(ts)
        self.cummulativeRewardVals.append(cr)
        self.foundGold.append(foundGold)

    def strForIt(self,it):
        return "trial #{}: result = {} (total_reward = {}, last_reward = {}, total_steps = {})".format(it+1,"Success" if self.foundGold[it] else "Fail",self.cummulativeRewardVals[it], self.lastRewardVals[it], self.totalSteps[it])

    def printIteration(self,it):
        print(self.trForIt(it))

    def numberOfRuns(self):
        return len(self.foundGold)

    def numberOfSuccess(self):
        return sum(list(map(lambda x: 1 if x else 0,self.foundGold)))

    def getRates(self):
        return (self.numberOfSuccess()/self.numberOfRuns(),sum(self.lastRewardVals)/self.numberOfRuns(),sum(self.cummulativeRewardVals)/self.numberOfRuns(),sum(self.totalSteps)/self.numberOfRuns())

    def statString(self):
        (sr,lr,cr,ts) = self.getRates()
        num = self.numberOfRuns()

    def __repr__(self):
        toReturn = "Trials:\n"
        for i in range(self.numberOfRuns()):
            toReturn += "\t{}\n".format(self.strForIt(i))
        toReturn += "Overal:\n"
        (sr,lr,cr,ts) = self.getRates()
        toReturn += "\tSucessRate = {}, Avg. LastReward = {}, Avg. Total Reward = {}, Avg. Steps = {}\n".format(sr,lr,cr,ts)
        return toReturn
#s = Stats()
#s.add(10,10,10,False)

#print(s)
