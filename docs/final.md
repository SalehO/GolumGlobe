---
layout: default
title: Final Report
--- 

## Video 
Welcome to Golem Globe where we trained a Minecraft agent how to play our own variation of Wumpus World. In this video we will describe the rules of the game, how we trained our agent, how well it did in the beginning stages of training, and how well it did after. This video is only a brief description of the project. For more details please read the following project report. 

## Project Summary 
Golem Globe, inspired by Wumpus World, is an environment in which a Minecraft agent must traverse through a platform that contains a single block of gold, multiple pits, and multiple monsters. The goal of this project was to create a Minecraft AI that can navigate through a platform of pits and monsters to locate the treasure/gold without falling into a pit or being killed by a monster during its journey. To survive, the agent must make observations of their immediate surroundings and decide which direction will be most rewarding (or least dangerous) for them. If the agent smells a stench it is an indication that they are beside a monster; a breeze indicates that the agent is beside a pit; the sparkles of glitter indicate that the agent has found the gold and have completed their mission. These percepts will help the agent navigate through the platforms. For more information regarding the rules of Golem Globe and a more in-depth explanation of the game please vist our [Home Page](https://soberanc.github.io/GolemGlobe/). 

## Approaches 
To train our agent we incorporated reinforcement learning through Q-Tables in which the agent will record their observations made on a given map as they explore that map in search of the gold. An agent at all times has their "current" memory, which has stored in it the observations and resulting rewards of their current run. If an agent has already been trained on an environment then the agent will not only have their "current" memory but also their "previous" memory to help them make decisions regarding their traversals. 

To start, the agent was trained on a single map that does not change with only one pit and one monster. As the agent explores their environment in search of the gold they are rewarded for accomplishing their mission (locating the gold) and penalized for dying (either from falling into a pit or being killed by a monster). 

During a traversal, an agent is penalized or rewarded based on the actions they take and the observations that they make. These actions and observations, along with the respective reward, is stored in their "current" memory. In addition, the agent also takes note of the tiles that have already been explored. To encourage the agent to explore newer tiles the agent is rewarded some points. 

When the agent is done traversing (either by finding the gold or from dying) it maps all the previous actions it made to the total rewards received and logs their "current" memory into their "previous" memory, clearing their "current" memory for their next attempt at the mission. We created our agent to prioritize the long-term reward, and added some randomness so that it would have a chance to explore new unexplored blocks and encounter more scenarios. 

By running the agent on the same map and recording the results of previous attempts in "previous" memory, the agent begins to associate the observations it made with the reward that it was given, and thus learns which actions to undertake to maximize the reward. 

### Reward System 
The agent begins with 0 points at the start of every mission. 

The agent is rewarded (+) or penalized(-) for the following actions

| _ +/- Points _ |  Action _ |
| :--- | :--- | 
| -2 | - Every step an agent takes | 
| + 3 | - The agent explores a new tile | 
| -200 | - The agent feels a breeze or smells a stench | 
| + 250 | - Kill a monster | 
| -20 | - Swing the sword and miss 
| -1000| - Killed (fell into a pit, killed by a monster, reached maximum number of allowed steps) | 
| +1000 | - Gold has been located (agent is standing on the tile of gold and can see the glitter) |

For every step that an agent takes, be it to an explored tile or to a new tile, they are awarded with -2 points. Every new tile that an agent explores however awards the agent with +3 points. So on an agent's very first attempt on a map every step that leads them to explore a new tile awards them with (+3) + (-2) = +1 point. This encourages an agent to explore the environment. This is especially helpful if the agent has explored most of the tiles on the 10x10 grid and have yet to locate the gold. The agent is encouraged to explore the unexplored areas in hopes of locating the gold. 

If the agent steps on a tile and observes either a breeze or a stench they receive -200 points. This discourages the agent from attempting the same blocks on their next attempt due to the danger surrounding it and encourages them to explore other areas of their environment. The loss in points however still allows the agent to attempt these tiles if they find no other way around it. 

In addition to losing points on a tile with a stench the agent is forced to make a decision - they are forced to attack a monster but must decide in which direction to attack (up/forward, down/backwards, left, or right). If the agent swings its sword and misses they receive -20 points which discourages blind/uneducated attacks. If the monster is killed then the agent is awarded with 250 points. 

If the agent dies for any reason (it fell into a pit, it is killed by a monster, or it reaches its maximum number of allowed steps) it receives -1000 points every time it dies. 

Once the agent locates the gold (is standing on a block of gold) they receive +1000 points for completing their mission. 

### Q-Table Reinforced Learning 
Throughout their missions an agent will always have a "current" memory that retains all observations and actions of the agent as well as the respective rewards. This "current" memory is a Q-Table of 3x3 grids of the map that the agent has already explored containing the observations the agent has made, the actions they have taken, and the respective rewards that they received from each tile. 

<img align="left" src="https://github.com/soberanc/GolemGlobe/blob/master/docs/observations_map.jpg">

Below is an illustrative view of the "current" memory an agent would have stored from traversing the bottom half of the map to the left. 

<img src="https://github.com/soberanc/GolemGlobe/blob/master/docs/3x3_grid.PNG"> <img src="https://github.com/soberanc/GolemGlobe/blob/master/docs/3x3_grid_shifted_once.PNG"> <img src="https://github.com/soberanc/GolemGlobe/blob/master/docs/3x3_grid_shifted_twice.PNG">

In addition to a "current" memory, an agent, if they have already had a chance to explore their environment (and failed or succeeded), also retains a "previous" memory that stores the "current" memory from all of their previous explorations. 

This "previous" memory is also a Q-Table of 3x3 grids of the map that the agent has already explored (cummulative - for all attempts) that consolidates all previous attempt's data. 

Although an agent is influenced by their "previous" memories they are mostly influenced by their "current" memory. "Previous" memory is mainly used for discouraging an agent to make fatal decisions (any kind of decision that will cause they to die). This knowledge of fatal mistakes assists the agent in surviving long enough for them to find a new fatal step or for them to find the gold. 

## Evaluation
The evaluate the performance of our agent we are using a combinatino of qualitative and quantitative metrics. 

### Quantitative: 
The primary quantitative metrics we will use is the cummulative reward received and the success rate. The cummulative reward is calculated by simply summing up the agents rewards from all action that it took. The succes rate is the ratio of successful traversals to total attempts made. If our agent receives on average a higher cummulative reward, and achieve a greater success rate we consider that a successful implementation. 

### Qualitative: 
To verify that the project works we will begin the AI on a controlled map that will not change (training data). If the AI succeeds they will move on to randomized maps for testing and learning. Qualitatively, we will consider the difficulty of the maps our agent can successfully traverse, and how easily it can adapt to new maps. 

Our mooonshot case is to create an agent that stops dying and is always able to retrieve the gold for every map. 

## References 
