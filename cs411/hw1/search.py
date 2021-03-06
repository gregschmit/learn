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

from game import Directions as D
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
    return  [s, s, w, s, w, w, s, w]

def backtrack(last, visited):
    """
    Backtrack a path to the "z" or origin node and return the path from origin
    to the final destination.
    """
    p = []
    next_node = last[0][0]
    for n in reversed(visited):
        if not n[1]: # at origin
            break
        if n[0][0] == next_node:
            p.append(n[0][1])
            next_node = n[1]
    return list(reversed(p))

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()
    visited = []
    stack = util.Stack()
    stack.push(((state, ''), None))
    cur = None
    while stack.list:
        # pop item off stack and mark it visited
        cur = stack.pop()
        visited.append(cur)
        # break if this is our goal
        if problem.isGoalState(cur[0][0]):
            break
        # add successors to stack unless we already visited them
        nexts = problem.getSuccessors(cur[0][0])
        for x in nexts:
            if not any(x[0] == y[0][0] for y in visited):
                stack.push((x, cur[0][0]))
                # do we push everything to the stack? maybe we should dive in
                #visited.append((x, cur[0][0]))
    return backtrack(cur, visited)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()
    visited = []
    discovered = []
    queue = util.Queue()
    queue.push(((state, ''), None)) # ((state, direction), parent)
    discovered.append(((state, ''), None));
    cur = None
    while queue.list:
        # pop item off queue
        cur = queue.pop()
        visited.append(cur)
        # break if this is our goal
        if problem.isGoalState(cur[0][0]):
            break
        # add successors to queue unless we already visited them
        nexts = problem.getSuccessors(cur[0][0])
        for x in nexts:
            if not any(x[0] == y[0][0] for y in visited+discovered):
                queue.push((x, cur[0][0]))
                discovered.append((x, cur[0][0]))
    return backtrack(cur, visited)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    state = problem.getStartState()
    visited = []
    discovered = []
    queue = util.PriorityQueue()
    queue.push(((state, ''), None, [], 0), 0) # (state, direction), parent, actions, cost
    discovered.append(((state, ''), None, [], 0))
    cur = None
    while queue.heap:
        # pop item off queue
        cur = queue.pop()
        visited.append(cur)
        # break if this is our goal
        if problem.isGoalState(cur[0][0]):
            break
        # add successors to queue unless we already visited them
        nexts = problem.getSuccessors(cur[0][0])
        for x in nexts:
            if not any(x[0] == y[0][0] for y in visited+discovered):
                dirs = cur[2] + [x[1]]
                cost = problem.getCostOfActions(dirs)
                queue.push((x, cur[0][0], dirs, cur[3] + cost), cur[3] + cost)
                discovered.append((x, cur[0][0], dirs, cur[3] + cost))
    return cur[2]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
