---
layout: default
title: Status
---

<iframe width="560" height="315"
src="https://www.youtube.com/embed/-EcSR30vwDM" 
frameborder="0" 
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

## Project Summary
Our project is called Golem Globe, which is a modified implementation of Wumpus World in Minecraft. 
The goal of our project is to create a Minecraft AI agent that can navigate through a maze containing pits and monsters to find the treasure/gold then go back to the start position.

## Approach
We begin by trainning our agent on a static map. The agent learns through the use of a tabular q-table which rewards the agent for successful traversals and penalizes the agent for failing to traverse the map. During a traversal, the agent stores in memory all previous observations it made and associates them with a respective reward. When the agent is done traversing (either by finding the gold, or dying) it maps all the previous actions it made to the total rewards received. We created our agent to prioritize the long-term reward, and added some randomness so that it would encounter more scenarios. 

By running the agent on the same map and recording the results of previous attempts, the agent begins to associate the observations it made with the reward it was given, and thus learns which actions to undertake to maximize the reward.

## Evaluation 
To evaluate the performance of our agent we are using a combination of qualitive and quantitative metrics.

### Quantitative:
The primary quantitative metrics we will use is the cummulative reward received and the sucess rate. The cummulative reward is calculated by simply summing up the agents rewards from all action it took, while the success rate is the ratio of succeesful traversal to total attempts made. If our agent recieves on average a higher cummulative reward, and achieve a greater success rate we consider that a successful implementation.

As an example here are our results both for training and validation: 


#### Pre-Training Quantitative Results 
As you can see here the agent continuously failed to complete his missions. 

| Test#   | Result  | Reward  | Steps |
|:-------:|:-------:|:-------:|:-----:|
| Test 1  | Fail    | -1016   | 16    |
| Test 2  | Fail    | -1054   | 54    |
| Test 3  | Fail    | -1115   | 115   |
| Test 4  | Fail    | -1010   | 10    |
| Test 5  | Fail    | -1036   | 36    |
| Average | 0%      | -1046.2 | 46.2  |


#### Post-Training Quantitative Results 
These results show that after a large number of training sessions the agent is not only able to complete its missions but is also able to find the shortest paths to the gold.

| Test#   | Result  | Reward | Steps |
|:-------:|:-------:|:------:|:-----:|
| Test 1  | Success | 989    | 11    |
| Test 2  | Success | 987    | 13    |
| Test 3  | Success | 985    | 15    |
| Test 4  | Success | 981    | 19    |
| Test 5  | Success | 981    | 19    |
| Average | 100%    | 984.6  | 15.4  | 


### Qualitative:
To verify that the project works we will begin the AI on a controlled map that will not change (traning data). If the AI succeeds they will move on to randomized maps for testing and learning. Qualitatively, we will consider the difficulty of hte maps our agent can successfuly traverse, and how easily it can adapt to new maps. 

Our moonshot case is to create an agent that stops dying and is always able to retrieve the gold for every map. 

## Remaining Goals and Challenges 

### Goals
- Right now, our main remaining goal is to make our agent's traversal algorithm to be more general and able to adapt to new maps. Right now, our agent uses a Q-table to travese a map, which means that the learning is specific to a given map. We plan to generalize our agent by using the information stored in the q-table and feeding it into a neural network, that will predict the anticipated reward of a given tile, by looking at the obserations made from all its adjacent tiles.
- Place the gold within a pit with a monster requiring the AI to first realize that the gold is in the pit then to kill the monster before going into the pit, retrieve the gold, and then exit the map. 
- Include a reward for killing the monsters. Monsters wouldn't necessarily be on top of the gold, but could also be blocking the path to the gold.
- We might also have the monster move around the map

### Challenges 
- Our current algorithm tends to repeatedly visit certain blocks. A solution to this issue could be creating temporary rewards that will help prevent them from going back and forth to the same blocks. 
- There are random pauses during traversals which need to be fixed. 
- Find a monster that is big enough to be seen above the pit without being able to jump or step out of the pit or figure out a way to keep the monster from running around other than having it stuck in a hole. 
- What is the best way to kill monsters? Is there a kill command? 

## Resources Used  
Below is a list of resources we found helpful throughout the development of our project
 - [For monster and item types that can be placed on the map upon start of the mission](https://github.com/microsoft/malmo/blob/master/Schemas/Types.xsd.in)
 - [Tabular Q Learning](https://github.com/Microsoft/malmo/blob/master/Malmo/samples/Python_examples/tabular_q_learning.py)
