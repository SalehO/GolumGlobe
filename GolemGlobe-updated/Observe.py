observations = ["Smell","Breeze","Glitter","Fell","Mauled","Killed","Clear","Unknown","Wall"]
observation_map = {}
for (k,v) in zip(list(map(lambda x: x[0], observations)),observations): observation_map.update({k:v}) #populates observation_map

class Observation:
    def __init__(self,obs_type="Unknown"):
         self.observation_type = set()
         self._construct_obs_type(obs_type)

    def update(self,obs_type="Unknown"):
        self.observation_type = set()
        self._construct_obs_type(obs_type)

    def isUnknown(self):
        return "Unknown" in self.observation_type

    def isWall(self):
        return "Wall" in self.observation_type

    def isAgentDead(self):
        return "Mauled" in self.observation_type or "Fell" in self.observation_type

    def isGoldOnTile(self):
        return "Glitter" in self.observation_type

    def _construct_obs_type(self,obs_type):
        if type(obs_type) == str:
            if len(obs_type) == 1 and obs_type not in observation_map.keys():
                raise KeyError("{} is an invalid obs".format(obs_type))
            if obs_type in observations:
                self.observation_type.add(obs_type)
            elif obs_type in observation_map.keys():
                self.observation_type.add(observation_map[obs_type])
            else:
                for each_obs in obs_type:
                    self._construct_obs_type(each_obs)
            
        elif type(obs_type) == list:
            for each_observation in obs_type:
                self._construct_obs_type(each_observation)
                
        else:
            raise TypeError("obs_type was {}, expected str or list of strs".format(type(obs_type)))

    def __repr__(self):
        toReturn = ""
        for each_obs in self.observation_type:
            toReturn += each_obs[0]
        return "".join(sorted(toReturn))
        
