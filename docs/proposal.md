---
layout: default
title: Proposal
---

#### Summary of the Project 
Our project is inspired by Wumpus World. 

The AI will be required to navigate through a platform while they are under the effects of the blindness potion. They must locate the gold that is placed randomly on the platform while avoiding the golem. If the golem is in the way of the gold and there is no other way except to kill the monster, the AI must kill the golem, retrieve the gold, and return to their starting point (where they initially spawn).  


#### AI/ML Algorithms 
We will be using Reinforcement Learning and Dijkstra's Shortest Path Algorithm. 

###### Costs and Rewards 
1) Death: high costs 
2) Finds gold: high reward 
3) Returns to starting point with gold: highest reward 

#### Evaluation Plan 

##### Quantitative Evaluation 
    The project will use a cost and reward system. If the AI dies they will lose a large number of points. However if they survive and attain the gold they will receive a large reward. If they die while trying to return to their starting point with the gold then they will lose a large number of points. If they survive and manage to return to their starting point with the gold then they win the game and receive a large reward. 

We will consider the project a success when the AI finds the gold and doesn't die on a map that it has never seen before. 

#### Appointment with the Instructor 
Wednesday, April 24, 2019 
DBH 4204 
