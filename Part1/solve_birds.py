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
    step_counter = 0

    while fringe:
        state_tuple = fringe.get()
        (_, (state, path)) = state_tuple
        
        if is_goal(state):
            return path+[state,]

        successor_states = successors(state)
        for s in successor_states:
            # instead of fringe it should be a priority queue sort the queue as per the heuristic function
            fringe.put((h(s) + step_counter, (s, path+[state,])))

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
    