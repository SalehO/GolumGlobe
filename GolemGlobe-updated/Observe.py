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

    def showObs(self):
        return self.isSmell() or self.isBreeze() or self.isGoldOnTile()

    def obsString(self):
        toReturn = "You "
        hasSomething = False
        hasSomething2 = False
        if self.isGoldOnTile():
            toReturn += "see something glitter at your feet"
            hasSomething = True

        if self.isSmell():
            if hasSomething:
               toReturn += "and smell something funky"
               hasSomething2 = True
            else:
                toReturn += "smell something funky"
                hasSomething = True

        if self.isBreeze():
            if hasSomething2 or hasSomething:
                toReturn += "and feel a breeze."
            else:
                toReturn += "feel a breeze."

        return toReturn
            
    def isUnknown(self):
        return "Unknown" in self.observation_type

    def isWall(self):
        return "Wall" in self.observation_type
    
    def isFall(self):
        return "Fell" in self.observation_type

    def isAgentDead(self):
        return "Mauled" in self.observation_type or "Fell" in self.observation_type

    def isGoldOnTile(self):
        return "Glitter" in self.observation_type

    def isSmell(self):
        return "Smell" in self.observation_type

    def isBreeze(self):
        return "Breeze" in self.observation_type

    def isMauled(self):
        return "Mauled" in self.observation_type

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
        
