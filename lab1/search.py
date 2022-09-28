# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    init_coords = problem.getStartState()
    queue = util.Queue()
    visited_cells = []
    path = {init_coords : []}
    queue.push(init_coords)

    while not queue.isEmpty():
        curr_coords = queue.pop()

        if problem.isGoalState(curr_coords):
            return path[curr_coords]

        if curr_coords in visited_cells:
            continue
            
        for next_coords, direction, _ in problem.getSuccessors(curr_coords):
            if not next_coords in path:
                path[next_coords] = path[curr_coords] + [direction]
                queue.push(next_coords)
        
        visited_cells.append(curr_coords)


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    init_coords = problem.getStartState()
    priority_queue = util.PriorityQueue()
    visited = []
    path = {init_coords : [[], 0]} ## coords: [dir, cost]
    priority_queue.push(init_coords, path[init_coords][1]) ## coords, cost

    while not priority_queue.isEmpty():
        curr_coords = priority_queue.pop()
           
        if problem.isGoalState(curr_coords):
            return path[curr_coords][0]

        if curr_coords in visited: 
            continue
            
        for next_coords, next_direction, next_cost in problem.getSuccessors(curr_coords):
            
            if next_coords in visited:
                continue
                
            new_cost = path[curr_coords][1] + next_cost + heuristic(next_coords, problem)

            if not next_coords in path or new_cost < path[next_coords][1]:
                path[next_coords] = [path[curr_coords][0] + [next_direction], path[curr_coords][1] + next_cost]
                priority_queue.update(next_coords, path[next_coords][1] + heuristic(next_coords, problem))
                        
        visited.append(curr_coords)
        
    
def greedySearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest heuristic."""
    init_coords = problem.getStartState()
    priority_queue = util.PriorityQueue()
    visited = []
    path = {init_coords : []} ## coords: [dir]
    priority_queue.push(init_coords, heuristic(init_coords, problem)) ## state, cost

    while not priority_queue.isEmpty():
        curr_coords = priority_queue.pop()
        
        if problem.isGoalState(curr_coords):
            return path[curr_coords]

        if curr_coords in visited: 
            continue
            
        for next_coords, next_direction, _ in problem.getSuccessors(curr_coords):
                 
            if next_coords in visited:
                continue

            path[next_coords] = path[curr_coords] + [next_direction]
            priority_queue.update(next_coords, heuristic(next_coords, problem))
                        
        visited.append(curr_coords)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
gs = greedySearch
