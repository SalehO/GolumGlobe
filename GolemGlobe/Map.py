from builtins import range
from builtins import object
from past.utils import old_div
import MalmoPython
import os
import random
import sys
import time
import json
import copy
import errno
import math
import xml.etree.ElementTree
import malmoutils

from Helpers import *
from Board import *
import random

#size of Golem Maze:
SIZE_X = 10
SIZE_Y = 10
SIZE_Z = SIZE_Y

REWARD_PER_BLOCK = 10
REWARD_FOR_COMPLETION = 100

pallette = ["air", "air", "mycelium","glowstone","netherrack","slime"]
recolour_pallettes = ['<BlockTypeOnCorrectPlacement type="fire" /> <BlockTypeOnIncorrectPlacement type="redstone_block" />',
                      '<BlockTypeOnCorrectPlacement type="emerald_block" /> <BlockTypeOnIncorrectPlacement type="redstone_block" />',
                      '',
                      '<BlockTypeOnCorrectPlacement type="sea_lantern" />']

video_requirements = ''#'<VideoProducer><Width>860</Width><Height>480</Height></VideoProducer>' if agent_host.receivedArgument("record_video") else ''



#functions:
def createTestStructure(sx, sz):
    while True:
        s = [[(random.randint(0,len(pallette))) for z in range(sz)] for x in range(sx)]
        # Check we didn't create a block entirely made of air:
        if sum(s[x][z] > 1 for x in range(sx) for z in range(sz)):
            break
    print(s)
    return s

def structureToXML(structure, xorg, yorg, zorg):
    # Take the structure and create a drawing decorator and inventory spec from it.
    print(structure,xorg, yorg, zorg)
    drawing = ""
    inventory = {}
    expected_reward = 0
    for z in range(SIZE_Z):
        for x in range(SIZE_X):
            value = structure[x][z]
            type = pallette[value % len(pallette)]
            type_string = ' type="' + type + '"'
            drawing += '<DrawBlock x="' + str(x + xorg) + '" y="' + str(yorg) + '" z="' + str(z + zorg) + '" ' + type_string + '/>'
            inventory[type] = inventory.get(type, 0) + 1
            if type != "air":
                expected_reward += REWARD_PER_BLOCK
    drawingdecorator = "<DrawingDecorator>"
    # "Blank out" the volume, in case if overlaps with old structures and throws the test.
    drawingdecorator += '<DrawCuboid x1="' + str(xorg) + '" y1="' + str(yorg) + '" z1="' + str(zorg) + '" x2="' + str(xorg + SIZE_X + 1 + SIZE_X) + '" y2="' + str(yorg) + '" z2="' + str(zorg + SIZE_Z - 1) + '" type="air"/>'
    drawingdecorator += '<DrawCuboid x1="' + str(xorg) + '" y1="' + str(yorg-1) + '" z1="' + str(zorg) + '" x2="' + str(xorg + SIZE_X - 1) + '" y2="' + str(yorg-1) + '" z2="' + str(zorg + SIZE_Z - 1) + '" type="red_sandstone"/>'
    drawingdecorator += '<DrawCuboid x1="' + str(xorg + SIZE_X + 1) + '" y1="' + str(yorg-1) + '" z1="' + str(zorg) + '" x2="' + str(xorg + 2*SIZE_X) + '" y2="' + str(yorg-1) + '" z2="' + str(zorg + SIZE_Z - 1) + '" type="red_sandstone"/>'
    drawingdecorator += drawing + "</DrawingDecorator>"
    inventoryxml = '<Inventory>'
    slot = 0
    for i in range(0, len(inventory)):
        if list(inventory.keys())[i] != "air":
            inventoryxml += '<InventoryBlock slot="'+str(slot)+'" type="'+list(inventory.keys())[i] + '" quantity="' + str(list(inventory.values())[i]) + '"/>'
            slot += 1
    inventoryxml += '</Inventory>'
    expected_reward += REWARD_FOR_COMPLETION
    return drawingdecorator, inventoryxml, expected_reward

def getMissionXML(forceReset, structure):
    # Draw a structure directly in front of the player.
    xpos = 0
    zpos = 0
    xorg = xpos - int(old_div(SIZE_X, 2))
    yorg = 1
    zorg = zpos + 1
    structureXML, inventoryXML, expected_reward = structureToXML(structure, xorg, yorg, zorg)
    startpos = ()
    recolourXML = random.choice(recolour_pallettes)

    return '''<?xml version="1.0" encoding="UTF-8" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <About>
        <Summary>Test build battles</Summary>
    </About>
     
    <ServerSection>
        <ServerHandlers>
            <FlatWorldGenerator generatorString="3;168:1;8;" forceReset=''' + forceReset + '''/>''' + structureXML + '''
            <BuildBattleDecorator>
                <GoalStructureBounds>
                    <min x="''' + str(xorg) + '''" y="''' + str(yorg) + '''" z="''' + str(zorg) + '''"/>
                    <max x="''' + str(xorg + SIZE_X - 1) + '''" y="''' + str(yorg) + '''" z="''' + str(zorg + SIZE_Z - 1) + '''"/>
                </GoalStructureBounds>
                <PlayerStructureBounds>
                    <min x="''' + str(1 + xorg + SIZE_X) + '''" y="''' + str(yorg) + '''" z="''' + str(zorg) + '''"/>
                    <max x="''' + str(xorg + 2*SIZE_X) + '''" y="''' + str(yorg) + '''" z="''' + str(zorg + SIZE_Z - 1) + '''"/>
                </PlayerStructureBounds>''' + recolourXML + '''
            </BuildBattleDecorator>
            <ServerQuitWhenAnyAgentFinishes />
            <ServerQuitFromTimeUp timeLimitMs="25000" description="Ran out of time."/>
        </ServerHandlers>
    </ServerSection>

    <AgentSection mode="Survival">
        <Name>Han van Meegeren</Name>
        <AgentStart>
            <Placement x="''' + str(xpos + 0.5) + '''" y="1.0" z="''' + str(zpos + 0.5) + '''"/>''' + inventoryXML + '''
        </AgentStart>
        <AgentHandlers>
            <ContinuousMovementCommands />
            <DiscreteMovementCommands />
            <InventoryCommands />
            <ObservationFromFullStats/>
            <RewardForStructureCopying rewardScale="''' + str(REWARD_PER_BLOCK) + '''" rewardForCompletion="''' + str(REWARD_FOR_COMPLETION) + '''">
                <RewardDensity>PER_BLOCK</RewardDensity>
                <AddQuitProducer description="Build successful!"/>
            </RewardForStructureCopying>
            <ObservationFromRay/>
            <ObservationFromHotBar/>''' + video_requirements + '''
            </AgentHandlers>
    </AgentSection>

  </Mission>''', expected_reward


def GetMissionXML(summary):
    ''' Build an XML mission string that uses the RewardForCollectingItem mission handler.'''

    #positions = buildPositionList(items)

    return '''<?xml version="1.0" encoding="UTF-8" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <About>
            <Summary>Hello World!</Summary>
        </About>

        <ModSettings>
            <MsPerTick>100</MsPerTick>
        </ModSettings>

        <ServerSection>
            <ServerInitialConditions>
                <Time>
                    <StartTime>6000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                </Time>
                <Weather>clear</Weather>
                <AllowSpawning>false</AllowSpawning>
            </ServerInitialConditions>
            <ServerHandlers>
                <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1" />
                <DrawingDecorator>
                    <DrawCuboid x1="-50" y1="226" z1="-50" x2="50" y2="228" z2="50" type="air" />
                    <DrawCuboid x1="-50" y1="226" z1="-50" x2="50" y2="226" z2="50" type="monster_egg" variant="chiseled_brick" />
                    <DrawCuboid x1="-3" y1="226" z1="-3" x2="3" y2="226" z2="3" type="dirt" />
                    <DrawBlock x="-0" y="226" z="0" type="diamond_block"/>
                </DrawingDecorator>
                <ServerQuitWhenAnyAgentFinishes />
            </ServerHandlers>
        </ServerSection>

        <AgentSection mode="Survival">
            <Name>Odie</Name>
            <AgentStart>
                <Placement x="0.5" y="227.0" z="0.5"/>
                <Inventory>
                    <InventoryItem slot="9" type="planks" variant="acacia"/>
                    <InventoryItem slot="10" type="brown_mushroom"/>
                    <InventoryItem slot="11" type="planks" variant="spruce"/>
                    <InventoryItem slot="12" type="brown_mushroom"/>
                </Inventory>
            </AgentStart>
            <AgentHandlers>
                <ContinuousMovementCommands turnSpeedDegs="480"/>
                <AbsoluteMovementCommands/>
                <SimpleCraftCommands/>
                <MissionQuitCommands/>
                <InventoryCommands/>
                <ObservationFromNearbyEntities>
                    <Range name="entities" xrange="40" yrange="40" zrange="40"/>
                </ObservationFromNearbyEntities>
                <ObservationFromFullInventory/>
                <AgentQuitFromCollectingItem>
                    <Item type="rabbit_stew" description="Supper's Up!!"/>
                </AgentQuitFromCollectingItem>
            </AgentHandlers>
        </AgentSection>

    </Mission>'''

DEBUG_MODE_ON = True

if True:
    #initalize client:
    debug_print("Initalizing Client",DEBUG_MODE_ON)
    expected_reward = 3390
    my_client_pool = MalmoPython.ClientPool()
    my_client_pool.add(MalmoPython.ClientInfo("127.0.0.1", 10000))

    agent_host = MalmoPython.AgentHost()



    #inialize board:
    debug_print("Initalizing Board of size {}x{}".format(SIZE_X,SIZE_Y),DEBUG_MODE_ON)
    board = Board()
    board.generate(SIZE_X,SIZE_Y) #create random board

    #create map:
    debug_print("Creating map of size {}x{}".format(SIZE_X,SIZE_Y),DEBUG_MODE_ON)
    #structure = createTestStructure(SIZE_X, SIZE_Z)
    structure = [[]]
    missionXML, expected_reward = getMissionXML('"false"', structure)
    #my_mission = MalmoPython.MissionSpec(GetMissionXML("hello"),True) 
    my_mission = MalmoPython.MissionSpec(missionXML,True)
    my_mission_record = MalmoPython.MissionRecordSpec()  # Records nothing by default
    my_mission.requestVideo(800, 500)
    my_mission.setViewpoint(1)

    #start screen:
    debug_print("Start Screen Recording",DEBUG_MODE_ON)
    #my_mission_record = MalmoPython.MissionRecordSpec()  # Records nothing by default
    #my_mission.requestVideo(800, 500)
    #my_mission.setViewpoint(1)
    #start mission:
    debug_print("Start Mission:",DEBUG_MODE_ON)
    agent_host.startMission(my_mission, my_client_pool, my_mission_record, 0, "Odie")
