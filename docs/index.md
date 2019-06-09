---
layout: default
title: Golem Globe
---

# Golem Globe

![](https://www.ics.uci.edu/~wschallo/golemGlobe.png)

## What is Golem Globe?

Golem Globe, is a modified implementation of Wumpus World in Minecraft. The world is a 10x10 grid map that contains a moster, gold and any number of pits. The agent only has observation of the current bock it is on, in other words, it does not know where the gold, pits, or monster is located on the map. However when the agent is adjacent to a pit it feels/observes a breeze, and when when it is adjacent to the monster it smells a stench and when it is on the block that has the gold it feels glitter. To win the game the agent needs to navigate through the map to find the gold.  

## How does the agent work? 
The agent navigates through the map by utilizing a reinforced learning algorithm incorporating a Q-Table to store observations. The agent remembers observations from previous maps and uses those observations of previous maps along with the Q-table from the current map to learn and choose what step to take next. 

## Source code:
[Proposal](https://github.com/soberanc/GolemGlobe)



### Resports:

 - [Proposal](https://github.com/soberanc/GolemGlobe/blob/master/docs/proposal.md)
 - [Status Report](https://soberanc.github.io/GolemGlobe/status.html)
 - [Final (coming soon)]()
