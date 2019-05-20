#from Map import *
from Board import *
from Helpers import *
from GolemGlobeAgent import *
import MalmoPython



#coding environment, details:
DEBUG_MODE_ON = True

def getObservationsForCurrentIndex(board):
    return board.getObservationForIndex()

def getIndexOfValidMoves(board):
    return board.getIndexOfValidMoves()
    

if __name__ == "__main__":
    

    #inialize board:
    #debug_print("Initalizing Board of size {}x{}".format(SIZE_X,SIZE_Y),DEBUG_MODE_ON)
    board = Board("C:\\Users\\wills\\Desktop\\CS_175\\maps\\test.txt") #test board
    #board.generate(SIZE_X,SIZE_Y) #create random board

    #initalizeAgent:
    agent = GolemGlobeAgent(board.rows,board.cols,board.currentIndex)

    #create map:
    #debug_print("Creating map of size {}x{}".format(SIZE_X,SIZE_Y),DEBUG_MODE_ON)
    #structure = createTestStructure(SIZE_X, SIZE_Z)
    #missionXML, expected_reward = getMissionXML('"false"', structure)
    #my_mission = MalmoPython.MissionSpec(missionXML, True)

    #start screen:
    #debug_print("Start Screen Recording",DEBUG_MODE_ON)
    #my_mission_record = MalmoPython.MissionRecordSpec()  # Records nothing by default
    #my_mission.requestVideo(800, 500)
    #my_mission.setViewpoint(1)

    #initalize client:
    #debug_print("Initalizing Client",DEBUG_MODE_ON)
    #agent_host = MalmoPython.AgentHost()
    #my_clients = MalmoPython.ClientPool()
    #my_clients.add(MalmoPython.ClientInfo('127.0.0.1', 1000))

    #start mission:
    #debug_print("Start Mission:",DEBUG_MODE_ON)
    #agent_host.startMission(my_mission, my_clients, my_mission_record, 0, "Odie")

    complete = False
    while not complete:
        print("reset")
        board.currentIndex = 90
        agent.reset()
        while True:
            #get current observation:
            current_obs = getObservationsForCurrentIndex(board)
            agent.observations[agent.currentIndex] = current_obs

            #update reward:
            agent.currentTotalReward += current_obs.rewardFromObservation()

            #check if can continue or dead:
            if agent.needToReset():
                #dead
                break

            if agent.finished():
                #found gold
                print("found gold")
                complete = True
                break
            
            #get current moves:
            agent.currentActions = getIndexOfValidMoves(board)
            print(agent.currentIndex)

            #choose action:
            action = agent.selectAction()
            agent.moveToIndex(action)
            board.currentIndex = agent.currentIndex
