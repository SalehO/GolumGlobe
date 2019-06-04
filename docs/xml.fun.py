from __future__ import print_function
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
Filename = open('C:\\Users\\omarh\Malmo-0.36.0-Windows-64bit_withBoost_Python3.6\\Python_Examples\\okkk.txt') 
x = 0
y =0      
input_xml = "" 
# test_xml = ""    redstone_block      
while True:
    c = Filename.read(1)
    if not c:
        break
    if c != '\n':
      y = y +1
    else:
        y = 0
        x= x+1
    if c == 'G':
      input_xml+= "<DrawEntity x= "+ "\"" +str(x+0.5-1)+"\""+ " y=\"9\" z="+ "\""+str(y+1+0.5-1)+"\""+" type=\"Zombie\" />\n"
      input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"6\" z= " +"\""+ str(y+1)+"\"" +" type=\"redstone_block\" />\n"
    if c == 'P':
      input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"6\" z= " +"\""+ str(y+1)+"\"" +" type=\"air\" />\n"
    if c == 'T':
      input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"6\" z= " +"\""+ str(y+1)+"\"" +" type=\"air\" />\n"
      input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"6\" z= " +"\""+ str(y+1)+"\"" +" type=\"gold_block\" />\n"
    

# print(input_xml)

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
                      












                    












                      <DrawBlock x="0" y="8" z="1" type="emerald_block"/>
                      <DrawBlock x="1" y="8" z="1" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="1" type="lapis_block"/>
                      <DrawBlock x="3" y="8" z="1" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="1" type="lapis_block"/>
                      <DrawBlock x="5" y="8" z="1" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="1" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="1" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="1" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="1" type="lapis_block"/>

                      <DrawBlock x="0" y="8" z="2" type="lapis_block"/>
                      <DrawBlock x="1" y="8" z="2" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="2" type="lapis_block"/>
                      <DrawBlock x="3" y="8" z="2" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="2" type="lapis_block"/>
                      <DrawBlock x="5" y="8" z="2" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="2" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="2" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="2" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="2" type="lapis_block"/> 

                      <DrawBlock x="0" y="8" z="3" type="lapis_block"/>
                      <DrawBlock x="1" y="8" z="3" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="3" type="lapis_block"/>
                      <DrawBlock x="3" y="8" z="3" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="3" type="lapis_block"/>
                      <DrawBlock x="5" y="8" z="3" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="3" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="3" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="3" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="3" type="lapis_block"/>

                      <DrawBlock x="0" y="8" z="4" type="lapis_block"/>
                      <DrawBlock x="1" y="8" z="4" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="4" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="4" type="lapis_block"/>
                      <DrawBlock x="5" y="8" z="4" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="4" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="4" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="4" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="4" type="lapis_block"/>

                      <DrawBlock x="0" y="8" z="5" type="lapis_block"/>
                      <DrawBlock x="1" y="8" z="5" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="5" type="lapis_block"/>
                      <DrawBlock x="3" y="8" z="5" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="5" type="lapis_block"/>
                      <DrawBlock x="5" y="8" z="5" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="5" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="5" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="5" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="5" type="lapis_block"/>


                      <DrawBlock x="0" y="8" z="6" type="lapis_block"/>
                      <DrawBlock x="1" y="8" z="6" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="6" type="lapis_block"/>
                      <DrawBlock x="3" y="8" z="6" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="6" type="lapis_block"/>
                      <DrawBlock x="5" y="8" z="6" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="6" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="6" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="6" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="6" type="lapis_block"/>
  

                      <DrawBlock x="0" y="8" z="7" type="lapis_block"/>
                      <DrawBlock x="1" y="8" z="7" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="7" type="lapis_block"/>
                      <DrawBlock x="3" y="8" z="7" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="7" type="lapis_block"/>
                      <DrawBlock x="5" y="8" z="7" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="7" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="7" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="7" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="7" type="lapis_block"/>

                      <DrawBlock x="0" y="8" z="8" type="lapis_block"/>
                      <DrawBlock x="1" y="8" z="8" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="8" type="lapis_block"/>
                      <DrawBlock x="3" y="8" z="8" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="8" type="lapis_block"/>

                      <DrawBlock x="5" y="8" z="8" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="8" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="8" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="8" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="8" type="lapis_block"/>

                      <DrawBlock x="0" y="8" z="9" type="lapis_block"/>
                      <DrawBlock x="1" y="8" z="9" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="9" type="lapis_block"/>
                      <DrawBlock x="3" y="8" z="9" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="9" type="lapis_block"/>
                      <DrawBlock x="5" y="8" z="9" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="9" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="9" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="9" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="9" type="lapis_block"/>

                      <DrawBlock x="0" y="8" z="10" type="lapis_block"/>
                      <DrawBlock x="1" y="8" z="10" type="lapis_block"/>
                      <DrawBlock x="2" y="8" z="10" type="lapis_block"/>
                      <DrawBlock x="3" y="8" z="10" type="lapis_block"/>
                      <DrawBlock x="4" y="8" z="10" type="lapis_block"/>
                      <DrawBlock x="5" y="8" z="10" type="lapis_block"/>
                      <DrawBlock x="6" y="8" z="10" type="lapis_block"/>
                      <DrawBlock x="7" y="8" z="10" type="lapis_block"/>
                      <DrawBlock x="8" y="8" z="10" type="lapis_block"/>
                      <DrawBlock x="9" y="8" z="10" type="lapis_block"/>


                      '''+input_xml+'''



                  </DrawingDecorator>
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
# /effect @e 2 1000000 255 true      /kill @e[type=YourMob]     /effect give @p blindness 99999 255
# Loop until mission ends:
sword = 0
while world_state.is_mission_running:
    print(".", end="")
    time.sleep(0.1)
    if(sword ==0):
        agent_host.sendCommand("chat /give @p diamond_sword 1 0 {ench:[{id:16,lvl:9001},{id:19,lvl:100}]}") #buff sword
        agent_host.sendCommand("chat /effect @e[type=Zombie] 2 1000000 127 true") #freeze wumbus
        # agent_host.sendCommand("chat /kill @e[type=Zombie] ") #kill wumbus if stepped on 
        agent_host.sendCommand("chat /effect @p blindness 99999 255") #blind
        # agent_host.sendCommand("chat  Squirrel Fun") print command
        sword =1
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission ended")
# Mission has ended.
