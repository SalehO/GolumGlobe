from Observe import Observation
from Action import actions_map

#internal parameters:
GRID_SIZE = 3

class ObservationCollection:
    def __init__(self,obs_string="",delimeter=" "):
        self.obs_string = obs_string
        self.observations = []

        self._build_observation_collection(obs_string,delimeter)

    def _add_observation(self,obs_string="Unknown"):
        #print(obs_string)
        self.observations.append(Observation(obs_string))

    def _build_observation_collection(self,obs_string="",delimeter=" "):
        if obs_string=="":
            for i in range(GRID_SIZE * GRID_SIZE): self._add_observation("Unknown")
        else:
            toParse = obs_string.split(delimeter)
            #print(toParse)
            if len(toParse) == (GRID_SIZE * GRID_SIZE):
                for each_obs in toParse:
                    self._add_observation(each_obs)
            else:
                if len(toParse) != (GRID_SIZE * GRID_SIZE):
                    toParse = ["W"] * (GRID_SIZE * GRID_SIZE)
                for each_obs in toParse:
                    self._add_observation(each_obs)
    def __repr__(self):
        toReturn = ""
        for each_obs in self.observations:
            toReturn += str(each_obs) +" "
        return toReturn

    def get_valid_actions(self,all_action_short_strs):
        #assume 3 x 3 grid:
        toReturn = []
        check = {"l":3,"f":1,"r":5,"b":7}
        for i in all_action_short_strs:
            toCheck = i.lower()
            if toCheck in check.keys():
                #print(toCheck,self.observations[check[toCheck]].isWall(),self)
                if not self.observations[check[toCheck]].isWall():
                    toReturn.append(i)
            else:
                raise KeyError("{} not in check for obs collection".format(i))
        return toReturn 
        
        
    def print_observations(self):
        toReturn = ""
        i = 0
        for each_obs in self.observations:
            toReturn += str(each_obs)
            i += 1
            if (i) % GRID_SIZE == 0:
                toReturn += "\n"
        print(toReturn.strip())
