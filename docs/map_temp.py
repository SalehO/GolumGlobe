from __future__ import print_function
# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #2: Run simple mission using raw XML

from builtins import range
import MalmoPython
import os
import sys
import time

if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

# More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"

missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Hello world!</Summary>
              </About>

              <ServerSection>
              <ServerInitialConditions>
                  <Time>
                    <StartTime>15000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                  </Time>
              </ServerInitialConditions>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;5*1,35:15;1;village(size=10)"/>
                  <DrawingDecorator>


                      <DrawBlock x="0" y="7" z="1" type="air"/>
                      <DrawBlock x="1" y="7" z="1" type="air"/>
                      <DrawBlock x="2" y="7" z="1" type="air"/>
                      <DrawBlock x="3" y="7" z="1" type="air"/>
                      <DrawBlock x="4" y="7" z="1" type="air"/>
                      <DrawBlock x="5" y="7" z="1" type="air"/>
                      <DrawBlock x="6" y="7" z="1" type="air"/>
                      <DrawBlock x="7" y="7" z="1" type="air"/>
                      <DrawBlock x="8" y="7" z="1" type="air"/>
                      <DrawBlock x="9" y="7" z="1" type="air"/>

                      <DrawBlock x="0" y="7" z="2" type="air"/>
                      <DrawBlock x="1" y="7" z="2" type="air"/>
                      <DrawBlock x="2" y="7" z="2" type="air"/>
                      <DrawBlock x="3" y="7" z="2" type="air"/>
                      <DrawBlock x="4" y="7" z="2" type="air"/>
                      <DrawBlock x="5" y="7" z="2" type="air"/>
                      <DrawBlock x="6" y="7" z="2" type="air"/>
                      <DrawBlock x="7" y="7" z="2" type="air"/>
                      <DrawBlock x="8" y="7" z="2" type="air"/>
                      <DrawBlock x="9" y="7" z="2" type="air"/> 

                      <DrawBlock x="0" y="7" z="3" type="air"/>
                      <DrawBlock x="1" y="7" z="3" type="air"/>
                      <DrawBlock x="2" y="7" z="3" type="air"/>
                      <DrawBlock x="3" y="7" z="3" type="air"/>
                      <DrawBlock x="4" y="7" z="3" type="air"/>
                      <DrawBlock x="5" y="7" z="3" type="air"/>
                      <DrawBlock x="6" y="7" z="3" type="air"/>
                      <DrawBlock x="7" y="7" z="3" type="air"/>
                      <DrawBlock x="8" y="7" z="3" type="air"/>
                      <DrawBlock x="9" y="7" z="3" type="air"/>

                      <DrawBlock x="0" y="7" z="4" type="air"/>
                      <DrawBlock x="1" y="7" z="4" type="air"/>
                      <DrawBlock x="2" y="7" z="4" type="air"/>
                      <DrawBlock x="3" y="7" z="4" type="air"/>
                      <DrawBlock x="4" y="7" z="4" type="air"/>
                      <DrawBlock x="5" y="7" z="4" type="air"/>
                      <DrawBlock x="6" y="7" z="4" type="air"/>
                      <DrawBlock x="7" y="7" z="4" type="air"/>
                      <DrawBlock x="8" y="7" z="4" type="air"/>
                      <DrawBlock x="9" y="7" z="4" type="air"/>

                      <DrawBlock x="0" y="7" z="5" type="air"/>
                      <DrawBlock x="1" y="7" z="5" type="air"/>
                      <DrawBlock x="2" y="7" z="5" type="air"/>
                      <DrawBlock x="3" y="7" z="5" type="air"/>
                      <DrawBlock x="4" y="7" z="5" type="air"/>
                      <DrawBlock x="5" y="7" z="5" type="air"/>
                      <DrawBlock x="6" y="7" z="5" type="air"/>
                      <DrawBlock x="7" y="7" z="5" type="air"/>
                      <DrawBlock x="8" y="7" z="5" type="air"/>
                      <DrawBlock x="9" y="7" z="5" type="air"/>


                      <DrawBlock x="0" y="7" z="6" type="air"/>
                      <DrawBlock x="1" y="7" z="6" type="air"/>
                      <DrawBlock x="2" y="7" z="6" type="air"/>
                      <DrawBlock x="3" y="7" z="6" type="air"/>
                      <DrawBlock x="4" y="7" z="6" type="air"/>
                      <DrawBlock x="5" y="7" z="6" type="air"/>
                      <DrawBlock x="6" y="7" z="6" type="air"/>
                      <DrawBlock x="7" y="7" z="6" type="air"/>
                      <DrawBlock x="8" y="7" z="6" type="air"/>
                      <DrawBlock x="9" y="7" z="6" type="air"/>
  

                      <DrawBlock x="0" y="7" z="7" type="air"/>
                      <DrawBlock x="1" y="7" z="7" type="air"/>
                      <DrawBlock x="2" y="7" z="7" type="air"/>
                      <DrawBlock x="3" y="7" z="7" type="air"/>
                      <DrawBlock x="4" y="7" z="7" type="air"/>
                      <DrawBlock x="5" y="7" z="7" type="air"/>
                      <DrawBlock x="6" y="7" z="7" type="air"/>
                      <DrawBlock x="7" y="7" z="7" type="air"/>
                      <DrawBlock x="8" y="7" z="7" type="air"/>
                      <DrawBlock x="9" y="7" z="7" type="air"/>

                      <DrawBlock x="0" y="7" z="8" type="air"/>
                      <DrawBlock x="1" y="7" z="8" type="air"/>
                      <DrawBlock x="2" y="7" z="8" type="air"/>
                      <DrawBlock x="3" y="7" z="8" type="air"/>
                      <DrawBlock x="4" y="7" z="8" type="air"/>
                      <DrawBlock x="5" y="7" z="8" type="air"/>
                      <DrawBlock x="6" y="7" z="8" type="air"/>
                      <DrawBlock x="7" y="7" z="8" type="air"/>
                      <DrawBlock x="8" y="7" z="8" type="air"/>
                      <DrawBlock x="9" y="7" z="8" type="air"/>

                      <DrawBlock x="0" y="7" z="9" type="air"/>
                      <DrawBlock x="1" y="7" z="9" type="air"/>
                      <DrawBlock x="2" y="7" z="9" type="air"/>
                      <DrawBlock x="3" y="7" z="9" type="air"/>
                      <DrawBlock x="4" y="7" z="9" type="air"/>
                      <DrawBlock x="5" y="7" z="9" type="air"/>
                      <DrawBlock x="6" y="7" z="9" type="air"/>
                      <DrawBlock x="7" y="7" z="9" type="air"/>
                      <DrawBlock x="8" y="7" z="9" type="air"/>
                      <DrawBlock x="9" y="7" z="9" type="air"/>

                      <DrawBlock x="0" y="7" z="10" type="air"/>
                      <DrawBlock x="1" y="7" z="10" type="air"/>
                      <DrawBlock x="2" y="7" z="10" type="air"/>
                      <DrawBlock x="3" y="7" z="10" type="air"/>
                      <DrawBlock x="4" y="7" z="10" type="air"/>
                      <DrawBlock x="5" y="7" z="10" type="air"/>
                      <DrawBlock x="6" y="7" z="10" type="air"/>
                      <DrawBlock x="7" y="7" z="10" type="air"/>
                      <DrawBlock x="8" y="7" z="10" type="air"/>
                      <DrawBlock x="9" y="7" z="10" type="air"/>
                      












                      <DrawBlock x="3" y="7" z="4" type="air"/>
                      <DrawBlock x="3" y="6" z="4" type="diamond_block"/>
                      <DrawEntity x="3.5"  y="9" z="4.5" type="Creeper" />
                      
                      <DrawBlock x="1" y="6" z="9" type="air"/>











                      <DrawBlock x="0" y="8" z="1" type="emerald_block"/>
                      <DrawBlock x="1" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="1" type="diamond_block"/>

                      <DrawBlock x="0" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="2" type="diamond_block"/> 

                      <DrawBlock x="0" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="3" type="diamond_block"/>

                      <DrawBlock x="0" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="4" type="air"/>
                      <DrawBlock x="8" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="4" type="diamond_block"/>

                      <DrawBlock x="0" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="5" type="diamond_block"/>


                      <DrawBlock x="0" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="6" type="diamond_block"/>
  

                      <DrawBlock x="0" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="7" type="air"/>
                      <DrawBlock x="4" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="7" type="diamond_block"/>

                      <DrawBlock x="0" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="8" type="gold_block"/>
                      <DrawItem x="4" y="9" z="8" type="gold_nugget"/>

                      <DrawBlock x="5" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="8" type="diamond_block"/>

                      <DrawBlock x="0" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="9" type="diamond_block"/>

                      <DrawBlock x="0" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="10" type="diamond_block"/>
                      






                  </DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="300000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Creative">
                <Name>GolumGlobe</Name>
                <AgentStart>
                    <Placement x="0.0" y="9.0" z="1.0" yaw="0"/>
                </AgentStart>
                <AgentHandlers>
                  <ChatCommands/>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

# Create default Malmo objects:

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:',e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print("Waiting for the mission to start ", end=' ')
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission running ", end=' ')

# Loop until mission ends:
while world_state.is_mission_running:
    print(".", end="")
    time.sleep(0.1)
    agent_host.sendCommand("chat /give @p diamond_sword 1 0 {ench:[{id:16,lvl:9001},{id:19,lvl:100}]}")

    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission ended")
# Mission has ended.
