# GolemGlobe

![](https://www.ics.uci.edu/~wschallo/golemGlobe.png)

## What is Golem Globe?

Golem Globe, is a modified implementation of Wumpus World in Minecraft. The world is a 10x10 grid map that contains a moster, gold and any number of pits. The agent only has observation of the current bock it is on, in other words, it does not know where the gold,pits, or moster is located on the map. However when the agent in near a pit it feels/observes a breeze, and when when it is near the monster it smells a bad smell and when it is on the block that has the gold it feels glitter. To win the game the agent needs to navigate through the map to find the gold then go back to the starting position without falling into a pit or getting killed by the mosnter. 

## How does the agent works? 
The agent navigates through the map by utilizing a Q-table algorithim as well as neaural network algirithim. The agent remembers observations from previous maps and uses those observations of previous maps along with the Q-table from the current map to learn and choose what step to take next. After the agent finds the gold, it used Dijkstra's shortest path algorithim to find the shortest path back to the starting position.
