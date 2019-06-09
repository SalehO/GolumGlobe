---
layout: default
title: Final Report
--- 

## Video 

## Project Summary 

Golem Globe, inspired by Wumpus World, is an environment in which a Minecraft agent must traverse through a platform that contains a single block of gold, multiple pits, and multiple monsters. The goal of this project was to create a Minecraft AI that can navigate through a platform of pits and monsters to locate and retrieve the treasure/gold without falling into a pit or being killed by a monster during its journey. To survive, the agent must make observations of their immediate surroundings and decide which direction will be most rewarding (or least dangerous) for them. 

### Rules of the Game 
- An agent's observations are limited to that of the blocks that they have been to already (explored). 
- An agent may nly move up, down, left, or right - no diagonal movements - a single space at a time. 
- Observations made on a single block applies only to blocks that are above, below, to the left, or to the right of the block. 
- If an agent falls into a pit they die and they have failed their mission 
- If an agent is killed by a monster they have failed their mission
- An agent must stand on a gold block to "retrieve" the treasure 
- There is ever only one block of gold (treasure) in every map. 
- There is a limited number of steps that the agent can take per mission. If they pass that limit then they "die" and fail their mission. 

#### The Environment 
In Golem Globe, the environment consists of: 

<img align="left" width="175" height="175" src="https://github.com/soberanc/GolemGlobe/blob/master/docs/observations_map.jpg">

- A single emerald block as the starting point 
- A single gold block where the gold/treasure is located
- At least one redstone blocks where a monster stands - these blocks can be located within pits 
  - For the purpose of this game (traversal and observations) we often refer to the monster as the wumpus, the golem, or a specific type of monster (ie. a zombie) depending on what appears on the map. 
- At least one pit in the platform. 
  
#### The Observations 
To survive their mission the agent must make observations of their immediate surroundings (the block that they are on), remember these observations, and make decisions based on their observations. An agent is not able to determine what is adjacent to them (up, down, left, or right) unless they have already been on that block. 

Possible Percepts: 

- “Smell” : If the agent smells a stench, there is a monster adjacent to (up, down, left, or right) the current block 
- “Breeze: If the agent feels a breeze, there is a pit adjacent to (up, down, left, or right) the current block  
- “Glitter”: If the agent sees glitter, they have located the gold 


If the agent does not observe any of the above percepts then they are free to move in any direction (up, down, left, or right) without fear of running into a pit. 

For example: 

<img align="left" src="https://github.com/soberanc/GolemGlobe/blob/master/docs/observation_exp1.PNG">

If the agent is standing on a block and they "smell" a stench, it is an indicator that there is a monster adjacent to them (up, down, left, or right). For example, say the agent :smiley: has only been to the block it is on now. The only observations it has made from this 3x3 grid is that they smell a stench. Their only knowledge at this point is that anywhere "A" adjacent to them there must be a monster. 

<img align="right" src="https://github.com/soberanc/GolemGlobe/blob/master/docs/observation_exp2.PNG">

Now imagine (image on the right) that the agent has the observations :alien: and is currently standing on the block :smiley:. Now their observations show that above their current location there is a smell however in their current location they do not observe anything. 

<img align="left" src="https://github.com/soberanc/GolemGlobe/blob/master/docs/observation_exp3.PNG">

Now let's say that the agent decides to go on to this new block :smiley: (image on the left). Their observations include all of the observations it made from previous moves :alien:. 

At this point the agent observes a smell on this block indicating that there is a monster adjacent to their current block. With all of their previous observations they can now infer that the block above their current position has a high likelihood that there is a monster there due to the fact that the block "B" also exhibits a stench. 

## Approaches 
To train our agent we incorporated reinforcement learning through Q-Tables in which the agent will record their observations made on a given map as they explore that map in search of the gold. 

To start, the agent was trained on a static map with only one pit and one monster. As the agent explores their environment in search of the gold they are rewarded for successful traversals and penalized for dying (either from falling into a pit or being killed by a monster). During a traversal, the agent stores in memory all previous observations it made and associates them with a respective reward. When the agent is done traversing (either by finding the gold or from dying) it maps all the previous actions it made to the total rewards received. We created our agent to prioritize the long-term reward, and added some randomness so that it would encounter more scenarios. 

By running the agent on the same map and recording the results of previous attempts, the agent begins to associate the observations it made with the reward that it was given, and thus learns which actions to undertake to maximize the reward. 

### Reward System 
The agent begins with 0 points at the start of every mission. 

The agent is rewarded (+) or penalized(-) for the following actions:
  
![](https://github.com/soberanc/GolemGlobe/blob/master/docs/table%20of%20rewards.PNG)
## Evaluation

## References 
