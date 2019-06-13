#from Map import *
from Board import *
from Helpers import *
from Map import *
#from GolemGlobeAgent import *
#from GolemAgent import *
from GolemAgent2 import *
import MalmoPython


#coding environment, details:
DEBUG_MODE_ON = True
indexDifference = [0,0,0,0]
recordPath = "C:\\Users\\wills\\Desktop\\CS_175\\recordings_hd\\{}"

def initalizeIndexDifference(numberOfCols):
    #initalize with agent facing right
    global indexDifference
    
    indexDifference = [-numberOfCols,1,numberOfCols,-1]

def getObservationsForCurrentIndex(board):
    return board.getObservationForIndex()

def getObservationsForIndex(board,index,successfulAttack):
    return board.getObservationForIndex(index)

def getIndexOfValidMoves(board):
    return board.getIndexOfValidMoves()

#agent internal controls:
def _shiftIndexesOnLeftTurn():
    global indexDifference
    indexDifference = [indexDifference[-1]] + indexDifference[:-1]

def _shiftIndexesOnRightTurn():
    global indexDifference
    indexDifference  = indexDifference[1:] + [indexDifference[0]]

def _turn(agent,direction=-1):
    #to turn left=-1,right = +1
    _shiftIndexesOnLeftTurn() if direction == -1 else _shiftIndexesOnRightTurn()
    agent.sendCommand("turn {}".format(direction))
    time.sleep(0.25)
    agent.sendCommand("turn 0")
    time.sleep(0.25)
    
def _moveForward(agent):
    agent.sendCommand("move 1")
    time.sleep(0.25)
    agent.sendCommand("move 0")
    time.sleep(0.25)

def _turnAround(agent):
    _turn(agent)
    _turn(agent)

def _convertIndexToXZ(index,rows,cols):
    z = index%cols + 1
    x = abs(rows - index//cols -1)
    #print(x,z)
    return (x,z)

def _tpToIndex(agent,index,rows,cols,y=18):
    (x,z) = _convertIndexToXZ(index,rows,cols)
    agent.sendCommand("chat /tp {}.5 {} {}.5".format(x,y,z))
 

#agent external controls:
def move(agent,originalIndex,newIndex,tp=True,turn=False,rows=10,cols=10):
    moveToMake = indexDifference.index(newIndex-originalIndex)

    if turn:
        if moveToMake == 0:
            _turn(agent,-1)
        elif moveToMake == 2:
            _turn(agent,1)
        elif moveToMake == 3:
            _turnAround(agent)
    if tp:
        print(agent,newIndex)
        _tpToIndex(agent,newIndex,rows,cols)
        time.sleep(0.25)
    else:
        _moveForward(agent)
    return True

def attack(agent_host,board,attack_index,currentIndex=-1):
    #to do: swing sword
    if attack_index - currentIndex == -1:
        #behind
        #_turn(agent_host,-1)
        #_turn(agent_host,-1)
        agent_host.sendCommand("chat /tp @p ~ ~ ~ 180 ~")
        time.sleep(0.25)
        agent_host.sendCommand("attack 1")
        agent_host.sendCommand("attack 0")
        time.sleep(0.25)
        agent_host.sendCommand("chat /tp @p ~ ~ ~ 0 ~")
        time.sleep(0.25)
        #_turn(agent_host,+1)
        #_turn(agent_host,+1)
    elif (attack_index - currentIndex) < 0 :
        #left
        #_turn(agent_host,-1)
        agent_host.sendCommand("chat /tp @p ~ ~ ~ 270 ~")
        time.sleep(0.25)
        agent_host.sendCommand("attack 1")
        agent_host.sendCommand("attack 0")
        time.sleep(0.25)
        agent_host.sendCommand("chat /tp @p ~ ~ ~ 0 ~")
        time.sleep(0.25)
        #_turn(agent_host,+1)
    elif (attack_index - currentIndex) > 1:
        #_turn(agent_host,+1)
        agent_host.sendCommand("chat /tp @p ~ ~ ~ 90 ~")
        time.sleep(0.25)
        agent_host.sendCommand("attack 1")
        agent_host.sendCommand("attack 0")
        time.sleep(0.25)
        agent_host.sendCommand("chat /tp @p ~ ~ ~ 0 ~")
        time.sleep(0.25)
        #_turn(agent_host,-1)
    else:
        time.sleep(0.25)
        agent_host.sendCommand("attack 1")
        agent_host.sendCommand("attack 0")
        time.sleep(0.25)
    return board.attack(attack_index)
        

def resetAgent(agent_host,agent):
    agent_host.sendCommand("quit")
    _tpToIndex(agent_host,agent.initalIndex,agent.num_rows,agent.num_cols)

def killAllGolems(agent_host):
    print("killing all golems")
    agent_host.sendCommand("chat /kill @e[type=Zombie]")

def killGolemAtIndex(agent_host,index,board,y=18):
    (x,z) = _convertIndexToXZ(index,board.rows,board.cols)
    agent_host.sendCommand("chat /kill @e[type=Zombie,x={},y={},z={},r=1]".format(x,y,z))

def spawnGolemAtIndex(agent_host,board,y=19,index = -1):
    if index == -1:
        toSpawn = board.golemIndexes
    else:
        toSpawn = [index]
    for eachGolemIndex in toSpawn:
        (x,z) = _convertIndexToXZ(eachGolemIndex,board.rows,board.cols)
        agent_host.sendCommand("chat /summon minecraft:zombie {} {} {} ".format(x+0.5,y,z+0.5) + "{Attributes:[{Name:\"generic.movementSpeed\",Base:0f}]}")
    

#start minecraft:
def initalizeMinecraftMap(xml):
    agent_host = MalmoPython.AgentHost()
    
    my_mission = MalmoPython.MissionSpec(xml, True)
    recordedFileName = recordPath.format("final_take0_bad.tgz") #comment out to not capture video
    #my_mission_record = MalmoPython.MissionRecordSpec()
    my_mission_record = MalmoPython.MissionRecordSpec(recordedFileName) #comment out to not capture video
    my_mission.requestVideo(1200,720)
    my_mission_record.recordMP4(30, 2000000) #comment out to not capture video
    my_mission.setViewpoint(1)
    my_clients = MalmoPython.ClientPool()
    my_clients.add(MalmoPython.ClientInfo('127.0.0.1', 10000)) # add Minecraft machines here as available

    return (my_mission,agent_host,my_clients,my_mission_record)



def tryStartUp(agent_host,my_mission, my_clients, my_mission_record,agent):
    max_retries = 1
    for retry in range(max_retries):
        try:
            agent_host.startMission(my_mission, my_clients, my_mission_record, 0, "%s-%d" % ('Moshe', retry) )
            agent.reset()

        except RuntimeError as e:
            if retry == max_retries - 1:
                print("Error starting mission:",e)
                exit(1)
            else:
                time.sleep(2)

    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        print(".", end="")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:",error.text)

    return world_state

def setAgent(agent,path):
    agent.loadMemory(path)

def runOnMap(agent,world_state,board,agent_host):
    initalizeIndexDifference(board.cols)
    
    #inialize board:
    need_inalitize = True
    complete = False
    obs_index = 0
    originalIndex = 0
    foundGolemIndex = []
    successfulAttack = False

    test_num = 1
    sword = 0
    
    while world_state.is_mission_running:
        agent_host.sendCommand("chat /give @p diamond_sword 1 0 {ench:[{id:16,lvl:9001},{id:19,lvl:100}]}")
        agent_host.sendCommand("chat /effect @e[type=Zombie] 2 1000000 127 true")
        if(sword ==0):
            agent_host.sendCommand("chat /give @p diamond_sword 1 0 {ench:[{id:16,lvl:9001},{id:19,lvl:100}]}")
            #agent_host.sendCommand("chat /clear")
            agent_host.sendCommand("chat /give @p diamond_sword 1 0 {ench:[{id:16,lvl:9001},{id:19,lvl:100}]}") #buff sword
            agent_host.sendCommand("chat /effect @e[type=Zombie] 2 1000000 127 true")
            sword =1
        else:
            agent_host.sendCommand("chat /effect @e[type=Zombie] 2 1000000 127 true")
        
        if test_num > 15:
            complete = True
            killAllGolems(agent_host)
            #agent_host.sendCommand("chat /clear")
            break
        

        #print(need_inalitize)

        
        if need_inalitize:
            current_obs = getObservationsForCurrentIndex(board)
            agent.updateObservationAtIndex(agent.currentIndex,current_obs)
            if current_obs.showObs():
                agent_host.sendCommand("chat {}".format(current_obs.obsString()))
            #killAllGolems(agent_host) #uncomment this to spawn golem
            #spawnGolemAtIndex(agent_host,board) #uncomment this to spawn golem
            need_inalitize = False
        else:
            new_obs = getObservationsForIndex(board,obs_index,successfulAttack)
            agent.update(new_obs,obs_index)

            if new_obs.showObs():
                agent_host.sendCommand("chat {}".format(new_obs.obsString()))

        
        

        #update index:
        successfulAttack = False
        originalIndex = agent.currentIndex

        #check if need to reset:
        if agent.needToReset():
            print("test num {}".format(test_num))
            print("result: died, {} steps, {} reward".format(agent.currentSteps,agent.rewardForLastAction))
            test_num += 1
            agent.reset(foundGolemIndex)
            originalIndex = agent.initalIndex
            board.reset(foundGolemIndex)
            resetAgent(agent_host,agent)
            need_inalitize = True
            continue
        elif agent.finished():
            print("test num {}".format(test_num))
            print("result: found gold, {} steps, {} reward".format(agent.currentSteps,agent.rewardForLastAction))
            test_num += 1
            originalIndex = agent.initalIndex
            agent.reset(foundGolemIndex)
            board.reset(foundGolemIndex)
            resetAgent(agent_host,agent)
            need_inalitize = True
            killAllGolems(agent_host)
            #agent_host.sendCommand("chat /clear")
            break
        else:
            need_inalitize = False

        #choose action:
        (newIndex,newAttack) = agent.performAction()
        #print(newIndex,newAttack)
        #a = input()
        #print(newIndex)
        board.currentIndex = newIndex

        #move/attack with avatar
        if newAttack != -1:
            #b = input()
            if board.board[newAttack].isGolem():
                #killGolemAtIndex(agent_host,newAttack,board,18)
                pass
            successfulAttack = attack(agent_host,board,newAttack,board.currentIndex)
            if successfulAttack:
                #print("success")
                foundGolemIndex.append(newAttack)
                
                 #uncomment this to spawn golem
                #a = input()
            obs_index = newAttack
        else:
            #print("moving")
            move(agent_host,originalIndex,newIndex)
            obs_index = newIndex
        

        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:",error.text)


def runManualTesting(board_path,memory_path):
    test_num = 1

    stats =[]
    board = Board(board_path)
    agent = GolemAgent(board.rows,board.cols,board.currentIndex,Memory())
    #setAgent(agent,memory_path)
    xmlForMap = generateXMLFromBoard(board)
    (my_mission,agent_host,my_clients,my_mission_record) = initalizeMinecraftMap(xmlForMap)
    world_state = tryStartUp(agent_host,my_mission, my_clients, my_mission_record,agent)
    agent_host.sendCommand("chat /gamerule sendCommandFeedback false")
    
    while True:
        getInput = input("Begin test #{}?".format(test_num))
        if getInput.strip().lower() != "y":
            break
        else:
            print("Starting test #{}:".format(test_num))
            board = Board(board_path) #test board
            agent = GolemAgent(board.rows,board.cols,board.currentIndex,Memory())
            #setAgent(agent,memory_path)
            #xmlForMap = generateXMLFromBoard(board)
            #(my_mission,agent_host,my_clients,my_mission_record) = initalizeMinecraftMap(xmlForMap)
            #world_state = tryStartUp(agent_host,my_mission, my_clients, my_mission_record,agent)
            #agent_host.sendCommand("chat /gamerule sendCommandFeedback false")#silence print
            print("Begin test #{}:".format(test_num))
            runOnMap(agent,world_state,board,agent_host)
            agent.saveMemory(memory_path)
            stats.append(agent.stats)
            print(agent.stats)
            print("Results from test #{}".format(test_num))
            test_num += 1
    return stats
        
                

if __name__ == "__main__":

    #theStats = runManualTesting("C:\\Users\\wills\\Desktop\\CS_175\\maps\\test.txt","C:\\Users\\wills\\Desktop\\CS_175\\cummulativeMemory.txt")
    theStats = runManualTesting("C:\\Users\\wills\\Desktop\\CS_175\\maps\\map7.txt","C:\\Users\\wills\\Desktop\\CS_175\\memory0.txt")
    #theStats = runManualTesting("C:\\Users\\wills\\Desktop\\CS_175\\maps\\map6.txt","C:\\Users\\wills\\Desktop\\CS_175\\cummulativeMemory.txt")
    #theStats = runManualTesting("C:\\Users\\wills\\Desktop\\CS_175\\maps\\test.txt","C:\\Users\\wills\\Desktop\\CS_175\\cummulativeMemory3.txt")
    for i in theStats:
        print(i)
    

    """
    #for i in boards:
    board = Board("C:\\Users\\wills\\Desktop\\CS_175\\maps\\test.txt") #test board
    #board = Board(i)

    agent = GolemAgent(board.rows,board.cols,board.currentIndex,Memory())

    xmlForMap = generateXMLFromBoard(board)


    
    (my_mission,agent_host,my_clients,my_mission_record) = initalizeMinecraftMap(xmlForMap)
    #agent_host.sendCommand("chat /gamerule commandBlockOutput false") 
    #agent_host.sendCommand("chat /gamerule logAdminCommands false")

    setAgent(agent,"C:\\Users\\wills\\Desktop\\CS_175\\cummulativeMemory.txt")
   
    
    world_state = tryStartUp(agent_host,my_mission, my_clients, my_mission_record)
    agent_host.sendCommand("chat /gamerule sendCommandFeedback false")#silence print
    runOnMap(agent,world_state,board)


    
    

    

    print()
    #print(agent.currentMemory)
    print("Mission ended")
    print(agent.stats)
    agent.saveMemory("C:\\Users\\wills\\Desktop\\CS_175\\cummulativeMemory.txt")
    """
