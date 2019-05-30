from Action import Action, actions_map

class Reward:
    def __init__(self,action,reward_val,final_reward=0):
        self.action = action
        self.reward_val = reward_val
        self.final_reward = final_reward

    def update_final_reward(self,new_final):
        self.final_reward = new_final

    def __repr__(self):
        return "({}:{}:{})".format(str(self.action),str(self.reward_val),str(self.final_reward))

    
