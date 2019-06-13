class ActionHistory:
    def __init__(self):
        self.actionNumber = 0
        self.actions = []
        self.rewards = []
        self.observationCollections = []

    def add(self,collection,action,reward):
        self.actions.append(action)
        self.observationCollections.append(collection)
        self.rewards.append(reward)
        self.actionNumber += 1

    def _get_final_reards(self,gamma):
        total_rewards = []
        for i in reversed(self.rewards):
            total_rewards = list(map(lambda x: x * gamma,total_rewards))
            total_rewards.append(i)
        return sum(total_rewards)

    def _calculate_final_reward(self,gamma):
        toReturn = []
        total_rewards = []
        j = len(self.rewards) - 1
        for i in reversed(self.rewards):
            total_rewards = list(map(lambda x: x * gamma,total_rewards))
            total_rewards.append(i)
            toReturn.append((self.observationCollections[j],self.actions[j],self.rewards[j],sum(total_rewards)))
            j -= 1
        return toReturn

    def reset(self,gamma):
       toReturn = self._calculate_final_reward(gamma)       
       self.actionNumber = 0
       self.actions = []
       self.rewards = []
       self.observationCollections = []
       return toReturn

    def __repr__(self):
        toreturn = ""
        for i in range(self.actionNumber):
            print("{}: {} {} {}".format(i,self.actions[i],self.rewards[i],self.observationCollections[i]))
        return toreturn

        
