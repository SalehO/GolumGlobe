actions = ["move_left","move_forward","move_right","move_backward","attack_Left","attack_Forward","attack_Right","attack_Backward"]
actions_map = {}
for (k,v) in zip(list(map(lambda x: x.split("_")[-1][0], actions)),actions): actions_map.update({k:v}) #populates actions_map

class Action:
    def __init__(self,action):
        self.action = ""
        self._set_action(action)

    def _set_action(self,action):
        if action in actions:
            self.action = action
        elif action in actions_map.keys():
            self.action = actions_map[action]
        else:
            raise KeyError("{} is an invalid action.".format(action))

    def is_attack(self):
        return "attack" in self.action

    def take_action(self,orientation,index,num_rows,num_cols):
        #return tuple containning new index and where attacked
        movedTo = index
        attackedTo = -1

        #print("act",orientation,index,num_rows,num_cols)

        #print(self.action)

        if "move" in self.action:
            ind = actions.index(self.action) #when using 4 elements list style orientation, make sure actions index correspond o orienttion index
            #print("mid",ind)
            movedTo = index + orientation[ind]
            #print(movedTo)
        if "attack" in self.action:
            ind = actions.index(self.action) - 4 #minus number of moves before
            #print("aid",ind)
            attackedTo = index + orientation[ind]
        return (movedTo,attackedTo)

    def __repr__(self):
        return self.action.split("_")[-1][0]
