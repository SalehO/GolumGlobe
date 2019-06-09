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

![](https://github.com/soberanc/GolemGlobe/blob/master/docs/observations_map.jpg)

In Golem Globe, the environment consists of: 
- A single emerald block as the starting point 
- A single gold block where the gold/treasure is located
- Multiple redstone blocks where a monster stands - these blocks can be located within pits 
  - For the purpose of this game (traversal and observations) we often refer to the monster as the wumpus, the golem, or a specific type of monster (ie. a zombie) depending on what appears on the map. 
  
#### The Observations 
  

## Approaches 

## Evaluation

## References 
