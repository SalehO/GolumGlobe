#fills in the grid
def load_grid(world_state):
    """
    Used the agent observation API to get a 21 X 21 grid box around the agent (the agent is in the middle).

    Args
        world_state:    <object>    current agent world state

    Returns
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)
    """
    while world_state.is_mission_running:
        #sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors) > 0:
            raise AssertionError('Could not load grid.')

        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            observations = json.loads(msg)
            grid = observations.get(u'floorAll', 0)
            break
    return grid

def find_start_end(grid):
    """
    Finds the source and destination block indexes from the list.

    Args
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)

    Returns
        start: <int>   source block index in the list
        end:   <int>   destination block index in the list
    """
    #------------------------------------
    #
    #   Fill and submit this code
    #
    source = 0
    dest  = 0
    for i in range(len(grid)):
        if grid[i] == "gold_block":
            source = i
        elif grid[i] == "emerald_block":
            dest = i
    return (source, dest)
    #-------------------------------------

def extract_action_list_from_path(path_list):
    """
    Converts a block idx path to action list.

    Args
        path_list:  <list>  list of block idx from source block to dest block.

    Returns
        action_list: <list> list of string discrete action commands (e.g. ['movesouth 1', 'movewest 1', ...]
    """
    action_trans = {-21: 'movenorth 1', 21: 'movesouth 1', -1: 'movewest 1', 1: 'moveeast 1'}
    alist = []
    for i in range(len(path_list) - 1):
        curr_block, next_block = path_list[i:(i + 2)]
        alist.append(action_trans[next_block - curr_block])

    return alist

def dijkstra_shortest_path(grid_obs, source, dest):
    """
    Finds the shortest path from source to destination on the map. It used the grid observation as the graph.
    See example on the Tutorial.pdf file for knowing which index should be north, south, west and east.

    Args
        grid_obs:   <list>  list of block types string representing the blocks on the map.
        source:     <int>   source block index.
        dest:       <int>   destination block index.

    Returns
        path_list:  <list>  block indexes representing a path from source (first element) to destination (last)
    """
    #------------------------------------
    #
    #   Fill and submit this code
    #
    dist = []
    prev = []
    Que = PQ()
    without_air = []
    valid_neighbours= []
    dijkstra = [] # for returning path
    count = len(grid_obs) # number of cells in grid

    #insert all cells to queue
    #set start to 0 and rest to infinity
    for i in range(count):
        if i == source:
             dist.append(0)
        else:
             dist.append(float('inf'))
        prev.append(-1)
        Que[i] = dist[i]

    #get rid of air and zombie blocks and add to new list
    for index in range(count):
        if grid_obs[index] != "air":
            if grid_obs[index] != "redstone_block":
                without_air.append(index)

    #return list with all valid neighbors
    #helper function
    def neigh(u):
        r_list = []
        r_list.append(u+1)
        r_list.append(u+21)
        r_list.append(u-1)
        r_list.append(u-21)
        return r_list
    #return min Q from priority queue
    def extract_min(p_q):
        if len(p_q) != 0:
            value = p_q.smallest()
            del p_q[value]
            return value
        else:
            return None

    while len(Que) > 0:
        u = extract_min(Que)
        for n in neigh(u):
            if (n) in without_air:
                valid_neighbours.append(n)
            for v in valid_neighbours:
                alt = 1 + dist[u] #lenght/cost always = 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    Que[v] = alt
                    
    #add moves to list 
    for d in range(len(prev) +1):
        if dest == source:
            dijkstra.append(source)
            dijkstra.reverse()
            return dijkstra
        else:
            dijkstra.append(dest)
            dest = prev[dest]        

    #-------------------------------------