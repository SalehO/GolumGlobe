---
layout: default
title: Final Report
--- 

## Video 
Welcome to Golem Globe where we trained a Minecraft agent how to play our own variation of Wumpus World. In this video we will describe the rules of the game, how we trained our agent, how well it did in the beginning stages of training, and how well it did after. This video is only a brief description of the project. For more details please read the following project report. 

## Project Summary 
Golem Globe, inspired by Wumpus World, is an environment in which a Minecraft agent must traverse through a platform that contains a single block of gold, multiple pits, and multiple monsters. The goal of this project was to create a Minecraft AI that can navigate through a platform of pits and monsters to locate and retrieve the treasure/gold without falling into a pit or being killed by a monster during its journey. To survive, the agent must make observations of their immediate surroundings and decide which direction will be most rewarding (or least dangerous) for them. 

## Approaches 
To train our agent we incorporated reinforcement learning through Q-Tables in which the agent will record their observations made on a given map as they explore that map in search of the gold. 

To start, the agent was trained on a static map with only one pit and one monster. As the agent explores their environment in search of the gold they are rewarded for successful traversals and penalized for dying (either from falling into a pit or being killed by a monster). During a traversal, the agent stores in memory all previous observations it made and associates them with a respective reward. When the agent is done traversing (either by finding the gold or from dying) it maps all the previous actions it made to the total rewards received. We created our agent to prioritize the long-term reward, and added some randomness so that it would encounter more scenarios. 

By running the agent on the same map and recording the results of previous attempts, the agent begins to associate the observations it made with the reward that it was given, and thus learns which actions to undertake to maximize the reward. 

### Reward System 
The agent begins with 0 points at the start of every mission. 

The agent is rewarded (+) or penalized(-) for the following actions

<img src="https://github.com/soberanc/GolemGlobe/blob/master/docs/table_of_rewards.PNG">

## Evaluation

## References 
