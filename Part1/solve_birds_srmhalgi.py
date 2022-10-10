#!/usr/local/bin/python3
# solve_birds.py : Bird puzzle solver
#
# Code by: Shrirang Mhalgi srmhalgi
#
# Based on skeleton code by D. Crandall & B551 course staff, Fall 2022
#
# N birds stand in a row on a wire, each wearing a t-shirt with a number.
# In a single step, two adjacent birds can swap places. How can
# they rearrange themselves to be in order from 1 to N in the fewest
# possible steps?

# !/usr/bin/env python3
import sys

N=5

#####
# THE ABSTRACTION:
#
# Initial state:

# Goal state:
# given a state, returns True or False to indicate if it is the goal state
def is_goal(state):
    return state == list(range(1, N+1))

# Successor function:
# given a state, return a list of successor states
def successors(state):
    return [ state[0:n] + [state[n+1],] + [state[n],] + state[n+2:] for n in range(0, N-1) ]

# Heuristic function:
# given a state, return an estimate of the number of steps to a goal from that state
def h(state):
    manhattan_dist = 0
    for i in range(len(state)):
        manhattan_dist += abs(i + 1 - state[i])
    
    return manhattan_dist

#########
#
# THE ALGORITHM:
#
# This is a generic solver using BFS. 
#
from queue import PriorityQueue
def solve(initial_state):
    fringe = PriorityQueue()
    fringe.put((h(initial_state), (initial_state, [])))
    # fringe += [(h(initial_state), initial_state, []),]
    step_counter = 0

    while fringe:
        # (state, path, heuristic_value) = fringe.pop(0)
        state_tuple = fringe.get()
        (_, (state, path)) = state_tuple
        # print(f"successor state = {state}")
        # print(f"path = {path}")
        # print(f"heuristicvalue = {heuristic_value}")
        
        if is_goal(state):
            return path+[state,]

        successor_states = successors(state)
        # print(f"successor_states = {successor_states}")
        # print("--------------------------------------------")
        for s in successor_states:
            # instead of fringe it should be a priority queue sort the queue as per the heuristic function
            fringe.put((h(s) + step_counter, (s, path+[state,])))
            # fringe.sort(reverse=True)
        # print("***************")
        # print(fringe)

        step_counter += 1
        
    return []

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a test case filename"))

    test_cases = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            test_cases.append([ int(i) for i in line.split() ])
    for initial_state in test_cases:
        	print('From state ' + str(initial_state) + " found goal state by taking path: " + str(solve(initial_state)))

    
# notes
# take a priority queue according to order 1,2,3,4,5 and move the nodes accordingly
# code is like a insertion sort as 2 birds are moving adjecently (this is not using a heuristic function anywhere)
# heuristic function is the manhattan distance 
# added the heuristic function to the current list implementation of the fringes
# but then we needed to sort the list everytime because append was adding to the last of the queue
# researched about priority queue in python (https://towardsdatascience.com/introduction-to-priority-queues-in-python-83664d3178c3)
# implemented the priority function as the heuristic function and the other data as the tuple.. 
# changed the successor function while loop defination
# got the results out of the priority queue
# everything else is written in the code hence the code is running in a fraction after implementation of the priority queues 