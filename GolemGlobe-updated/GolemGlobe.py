#from Map import *
from Board import *
from Helpers import *
from Map import *
#from GolemGlobeAgent import *
from GolemAgent import *
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

def _tpToIndex(agent,index,rows,cols):
    (x,z) = _convertIndexToXZ(index,rows,cols)
    agent.sendCommand("tp {}.5 9 {}.5".format(x,z))
 

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
        _tpToIndex(agent,newIndex,rows,cols)
        time.sleep(0.05)
    else:
        _moveForward(agent)
    return True

def attack(agent,board,attack_index):
    #to do: swing sword
    print(attack_index)
    return board.attack(attack_index)
        

def resetAgent(agent_host,agent):
    agent_host.sendCommand("quit")
    _tpToIndex(agent_host,agent.initalIndex,agent.num_rows,agent.num_cols)

if __name__ == "__main__":
    

    #inialize board:
    need_inalitize = True
    complete = False
    obs_index = 0
    originalIndex = 0
    foundGolemIndex = []
    successfulAttack = False

    board = Board("C:\\Users\\wills\\Desktop\\CS_175\\maps\\test.txt") #test board


    agent = GolemAgent(board.rows,board.cols,board.currentIndex,Memory())
    initalizeIndexDifference(board.cols)

    #start Malmo:
    agent_host = MalmoPython.AgentHost()
    
    my_mission = MalmoPython.MissionSpec(missionXML, True)
    #recordedFileName = recordPath.format("speed_up_1.tgz")
    my_mission_record = MalmoPython.MissionRecordSpec()
    #my_mission_record = MalmoPython.MissionRecordSpec(recordedFileName) #allow recording if pass recordPath instead of nothing
    my_mission.requestVideo(1200,720)
    #my_mission_record.recordMP4(30, 2000000); #record video
    #my_mission.requestVideo(1200, 720)
    my_mission.setViewpoint(1)
    my_clients = MalmoPython.ClientPool()
    my_clients.add(MalmoPython.ClientInfo('127.0.0.1', 10000)) # add Minecraft machines here as available

    max_retries = 1
    test_num = 1
    for retry in range(max_retries):

        
        
        if complete:
            break
        try:
            
            agent_host.startMission( my_mission, my_clients, my_mission_record, 0, "%s-%d" % ('Moshe', retry) )
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


        print()

        while world_state.is_mission_running:
            if test_num > 15:
                complete = True
                break

            
            if (need_inalitize):
                current_obs = getObservationsForCurrentIndex(board)
                agent.updateObservationAtIndex(agent.currentIndex,current_obs)
                need_inalitize = False
            else:
                new_obs = getObservationsForIndex(board,obs_index,successfulAttack)
                agent.update(new_obs,obs_index)


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
                #break

            if agent.finished():
                print("test num {}".format(test_num))
                print("result: found gold, {} steps, {} reward".format(agent.currentSteps,agent.rewardForLastAction))
                test_num += 1
                originalIndex = agent.initalIndex
                agent.reset(foundGolemIndex)
                board.reset(foundGolemIndex)
                resetAgent(agent_host,agent)
                need_inalitize = True
                #complete = True
                #break
                continue

            #choose action:
            (newIndex,newAttack) = agent.performAction()
            board.currentIndex = newIndex

            #move/attack with avatar
            if newAttack != -1:
                successfulAttack = attack(agent_host,board,newAttack)
                if successfulAttack:
                    foundGolemIndex.append(newAttack)
                obs_index = newAttack
            else:
                #print(originalIndex,newIndex)
                move(agent_host,originalIndex,newIndex)
                obs_index = newIndex
            

            world_state = agent_host.getWorldState()
            for error in world_state.errors:
                print("Error:",error.text)

    print()
    print(agent.currentMemory)
    print("Mission ended")
