#!/usr/local/bin/python3
# solver2022.py : 2022 Sliding tile puzzle solver
#
# Code by: Shrirang Mhalgi srmhalgi
#
# Based on skeleton code by D. Crandall & B551 Staff, Fall 2022
#

from copy import deepcopy
from ipaddress import summarize_address_range
import sys
import numpy as np

ROWS=5
COLS=5

def printable_board(board):
    return [ ('%3d ') * COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]

# check if we've reached the goal
def is_goal(state):
    for i in range(len(state)):
        for  j in range(len(state[0])):
            if state[i][j] != (i * 5) + (j + 1):
                return False
    
    return True

# return a list of possible successor states
def successors(state):
    successor_list = []
    for i in range(len(state)):
        successor_list.append(move_right(deepcopy(state), i))
        successor_list.append(move_left(deepcopy(state), i))
        successor_list.append(move_up(deepcopy(state), i))
        successor_list.append(move_down(deepcopy(state), i))
    
    successor_list.append(move_outer_counter_clockwise(state))
    successor_list.append(move_outer_clockwise(state))
    successor_list.append(move_inner_clockwise(state))
    successor_list.append(move_inner_counter_clockwise(state))

    return successor_list

# function to get the the successors when the tile is moved one step to the right
def move_right(board, row):
    board[row] = board[row][-1:] + board[row][:-1]
    return (board, h(board), f"R{row + 1}")


# function to get the successors when the tile is moved one step to the left
def move_left(board, row):
    board[row] = board[row][1:] + board[row][:1]
    return (board, h(board), f"L{row + 1}")

# function to get the successors when the tile is moved one step to the up
def move_up(board, column):
    new_board = np.transpose(board).tolist()
    new_board, _, _ = move_left(new_board, column)
    new_board = np.transpose(new_board).tolist()
    return (new_board, h(new_board), f"U{column + 1}")

# function to get the successors when the tile is moved one step to the up
def move_down(board, column):
    new_board = np.transpose(board).tolist()
    new_board, _, _ = move_right(new_board, column)
    new_board = np.transpose(new_board).tolist()
    return (new_board, h(new_board), f"D{column + 1}")

# function to move the outer ring clockwise
def move_outer_clockwise(board):
    new_board = deepcopy(board)
    new_board[1][0] = board[2][0]
    new_board[0][0] = board[1][0]
    new_board[0][1] = board[0][0]
    new_board[0][2] = board[0][1] 
    new_board[0][3] = board[0][2]
    new_board[0][4] = board[0][3]
    new_board[1][4] = board[0][4]
    new_board[2][4] = board[1][4]
    new_board[3][4] = board[2][4]
    new_board[4][4] = board[3][4]
    new_board[4][3] = board[4][4]
    new_board[4][2] = board[4][3]
    new_board[4][1] = board[4][2]
    new_board[4][0] = board[4][1]
    new_board[3][0] = board[4][0]
    new_board[2][0] = board[3][0]
        
    return (new_board, h(new_board), f"Oc")

# function to move the outer ring counter clockwise
def move_outer_counter_clockwise(board):
    new_board = deepcopy(board)
    new_board[1][0] = board[0][0]
    new_board[0][0] = board[0][1]
    new_board[0][1] = board[0][2]
    new_board[0][2] = board[0][3]
    new_board[0][3] = board[0][4]
    new_board[0][4] = board[1][4]
    new_board[1][4] = board[2][4]
    new_board[2][4] = board[3][4]
    new_board[3][4] = board[4][4]
    new_board[4][4] = board[4][3]
    new_board[4][3] = board[4][2]
    new_board[4][2] = board[4][1]
    new_board[4][1] = board[4][0]
    new_board[4][0] = board[3][0]
    new_board[3][0] = board[2][0]
    new_board[2][0] = board[1][0]
        
    return (new_board, h(new_board), f"Occ")

# function to move inner board clockwise
def move_inner_clockwise(board):
    new_board = deepcopy(board)
    new_board[1][1] = board[2][1]
    new_board[1][2] = board[1][1]
    new_board[1][3] = board[1][2]
    new_board[2][3] = board[1][3]
    new_board[3][3] = board[2][3]
    new_board[3][2] = board[3][3]
    new_board[3][1] = board[3][2]
    new_board[2][1] = board[3][1]
    
    return (new_board, h(new_board), f"Ic")

# function to move inner board counter clockwise
def move_inner_counter_clockwise(board):
    new_board = deepcopy(board)
    new_board[1][1] = board[1][2]
    new_board[1][2] = board[1][3]
    new_board[1][3] = board[2][3]
    new_board[2][3] = board[3][3]
    new_board[3][3] = board[3][2]
    new_board[3][2] = board[3][1]
    new_board[3][1] = board[2][1]
    new_board[2][1] = board[1][1]
    
    return (new_board, h(new_board), f"Icc")

# heuristic function to calculate the manhattan distance
def h(board):
    sum_manhattan_distance = 0
    actual_row = -1
    actual_column = -1
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] % 5 == 0:
                actual_row = board[i][j] // 5 - 1
                actual_column = len(board) - 1
            else:
                actual_row = board[i][j] // 5
                actual_column = board[i][j] % 5 - 1
            
            sum_manhattan_distance += abs(actual_row - i) + abs(actual_column - j)
        
    return sum_manhattan_distance

# main function to solve the problem
from queue import PriorityQueue
def solve(initial_board):
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return 
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """
    board = np.array(initial_board).reshape(ROWS, COLS).tolist() 
    
    fringe = PriorityQueue()
    fringe.put((h((board)), ((board), h(board), [])))
    visited_list = []
    board_heuristic = -1
    
    while fringe:
        state_tuple = fringe.get()
        (_, (state, board_heuristic, path)) = state_tuple
        
        visited_list.append(state)

        if is_goal(state):
            return path

        successor_states = successors((state))

        for s in successor_states:
            if s[0] not in visited_list:
                board_heuristic = h(s[0]) + ((len(path) ** 2) * 0.3)
                fringe.put((board_heuristic, (s[0], board_heuristic, path+[s[2],])))
                visited_list.append(s[0])

# Please don't modify anything below this line
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))
    
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))


# there will be 24 states
# slide row left (5 states)
# slide row right (5 states)
# slide row top (5 states)
# slide row bottom (5 states)
# rotating the inner board clockwise
# rotating the inner board anticlockwise
# rotating the outer board clockwise
# rotating the outer board anticlockwise
# write the functions for each of them
# after that use the part 1 logic to formulate the solution 
# heuristic will be sum of manhattan distances from start to end
# choose the best possible move chosen from priority queue