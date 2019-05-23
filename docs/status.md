---
layout: default
title: Status
---

# Status Report due Friday May 24th, 2019

## Project Summary
Our project is called Golem Globe, which is an implementation of Wumpus World in Minecraft. 
The goal of our project is to create a Minecraft AI agent that can navigate through a maze contraing pits and monsters to find the treasure then go back to the initial state. 
## Approach
We begin by trainning our agent on a static map. The agent learns through the use of a Q-table implementation, that rewards the agent for successful traversals and penalizes the agent for failing to traverse the map. During a traversal, the agent stores in memory a recollection of all previous observations it made, and associates them with a resepctive reward. When the agent is done traversing (either by finding the gold, or dieing) it maps all the previous actions it made to total reward ammount recieved. We created our agent to prioritize the long-term reward, and added some randomeness so that it would encounter more scenarios. 

By running the agent on the same map and recording the results of previous attempts, the agent begins to associate the observations it made with the reward it was given, and thus learns which actions to undertake to maximize the reward.
## Evaluation 
To evaluate the performance of our agent we are using a combination of qualitive and quantitative metrics.
### Quantitative:
The primary quanttative metrics we will use is the cummulative reward reiecved, and the sucess rate. The cummulative reward is calculated by simply summing up the agents rewards from all action it took, while the success rate is the ratio of succeesful traversal to total attempts made. If our agent recieves on average a higher cummulative reward, and achieve a greater success rate we consider that a successful implementation.

### Qualitative:
To verify that the project works we will beging the AI on a controlled map
that will not change (traning data). If the AI succeeds they will move 
on to randomized maps for testing and learning. Qualtittively, we will consider the difficulty of the maps our agent can successfully traverse, and how easily it can adapt to new maps.
Our moonshot case is to create an agent that stops dying and is always able to retrieve the gold for every map. 


## Remaining Goals and Challenges 
Right now, our main remainning goal is to make our agent's traversal algorithm to be more general, to adapt to new maps. Right now, our agent uses a Q-table to travese a map, which means that the learning is specific to a given map. We plan to generalize our agent by using the information stored in the q-table and feeding into a neural network, that will predict the anticipated reward of a given tile, by looking at the obserations made from all its adjacent tiles.

## Resources Used  
Below, are a list of resoruces we used.
 - [For monster and item types that can be placed on the map upon start of the mission](https://github.com/microsoft/malmo/blob/master/Schemas/Types.xsd.in)
 - [Tabular Q Learning](https://github.com/Microsoft/malmo/blob/master/Malmo/samples/Python_examples/tabular_q_learning.py)
