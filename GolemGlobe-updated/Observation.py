observations = ["Smell","Breeze","Glitter","Fell","Killed","Clear","Unknown","Wall"]

class Observation:
    def __init__(self,row_num,col_num,index,obs_type=["Unknown"]):
        self.obs = obs_type

        self.row = row_num
        self.col = col_num
        self.index = index

    def rewardFromObservation(self):
        toReturn = 0
        obs_type = self.obs
        if "Fell" in obs_type or "Killed" in obs_type:
            return -1000
        elif "Glitter" in obs_type:
            return 1000
        elif "Smell" in obs_type or "Breeze" in obs_type:
            return -200
        elif "Unknown" in obs_type or "Wall" in obs_type:
            return 0
        elif "Clear" in obs_type:
            return 10
        return 0

    def needToReset(self):
        return ("Fell" in self.obs or "Killed" in self.obs)

    def finished(self):
        return ("Glitter" in self.obs)

    def __repr__(self):
        toReturn = ""
        for i in set(self.obs):
            if i == "":
                toReturn += "N"
            else:
                toReturn += i[0]
        else:
            return toReturn
