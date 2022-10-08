# #!/usr/local/bin/python3
# # solver2022.py : 2022 Sliding tile puzzle solver
# #
# # Code by: name IU ID
# #
# # Based on skeleton code by D. Crandall & B551 Staff, Fall 2022
# #

# from copy import deepcopy
# from curses import nocbreak
# from ipaddress import summarize_address_range
# import sys
# import numpy as np

# ROWS=5
# COLS=5

# def printable_board(board):
#     return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]


# # return a list of possible successor states
# def successors(state):
#     initial_state = state
#     successor_list = []
#     for i in range(len(state)):
#         successor_list.append(move_left(deepcopy(state), i))
#         state = initial_state
#         successor_list.append(move_right(deepcopy(state), i))
#         state = initial_state
#         successor_list.append(move_up(deepcopy(state), i))
#         state = initial_state
#         successor_list.append(move_down(deepcopy(state), i))
#         state = initial_state
    
#     successor_list.append(move_inner_clockwise(deepcopy(state)))
#     state = initial_state
#     successor_list.append(move_inner_counter_clockwise(deepcopy(state)))
#     state = initial_state
#     successor_list.append(move_outer_clockwise(deepcopy(state)))
#     state = initial_state
#     successor_list.append(move_outer_counter_clockwise(deepcopy(state)))
    
#     return successor_list

# # check if we've reached the goal
# def is_goal(state):
#     for i in range(len(state)):
#         for j in range(len(state[0])):
#             if state[i][j] != (i * 5 + (j + 1)):
#                 return False

#     return True

# # function to get the the successors when the tile is moved one step to the right
# def move_right(board, row):
#     board[row] = board[row][-1:] + board[row][:-1]
#     # print(board)
#     return (board, f"R{row + 1}")

# # function to get the successors when the tile is moved one step to the left
# def move_left(board, row):
#     board[row] = board[row][1:] + board[row][0:1]
#     # print(board)
#     return (board, f"L{row + 1}")

# def move_up(board, column):
#     board = np.transpose(deepcopy(board)).tolist()
#     # print(board)
#     board, value = move_left(deepcopy(board), column)
#     board = np.transpose(board).tolist()
#     return (board, f"U{column + 1}")

# def move_down(board, column):
#     board = np.transpose(deepcopy(board)).tolist()
#     # print(board)
#     board, value = move_right(deepcopy(board), column)
#     board = np.transpose(board).tolist()
#     return (board, f"D{column + 1}")

# def move_outer_clockwise(board):
#     board, _ = move_right(deepcopy(board), 0)
#     board, _ = move_left(deepcopy(board), len(board) - 1)
#     board, _ = move_up(deepcopy(board), 0)
#     board, _ = move_down(deepcopy(board), len(board) - 1)
#     # print(board[0][len(board) - 1], board[1][len(board) - 1], board[len(board) - 1][0], board[len(board) - 2][0])
#     board[0][len(board) - 1], board[1][len(board) - 1], board[len(board) - 1][0], board[len(board) - 2][0] = board[1][len(board) - 1], board[len(board) - 1][0], board[len(board) - 2][0], board[0][len(board) - 1]
#     # print(board[0][len(board) - 1], board[1][len(board) - 1], board[len(board) - 1][0], board[len(board) - 2][0])
#     # print(board)
#     return (board, "Oc")

# def move_outer_counter_clockwise(board):
#     board, _ = move_left(deepcopy(board), 0)
#     board, _ = move_right(deepcopy(board), len(board) - 1)
#     board, _ = move_down(deepcopy(board), 0)
#     board, _ = move_up(deepcopy(board), len(board) - 1)
#     board[0][0], board[1][0], board[len(board) - 1][len(board) - 1], board[len(board) - 2][len(board) - 1] = board[1][0], board[len(board) - 1][len(board) - 1], board[len(board) - 2][len(board) - 1], board[0][0] 
#     return (board, "Occ")

# def move_inner_clockwise(board):
#     board[1][1], board[1][2], board[1][3], board[2][3], board[3][3], board[3][2], board[3][1], board[2][1] = board[2][1], board[1][1], board[1][2], board[1][3], board[2][3], board[3][3], board[3][2], board[3][1]
#     return (board, "Ic")

# def move_inner_counter_clockwise(board):
#     board[1][1], board[1][2], board[1][3], board[2][3], board[3][3], board[3][2], board[3][1], board[2][1] = board[1][2], board[1][3], board[2][3], board[3][3], board[3][2], board[3][1], board[2][1], board[1][1]
#     return (board, "Icc")

# # helper function for heuristics
# def get_correctly_placed_tiles(board):
#     correctly_placed_tiles_count = 0 
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             val = board[i][j]
#             val1 = i * 5 + j + 1
            
#             if val == val1:
#                 correctly_placed_tiles_count += 1
    
#     return (correctly_placed_tiles_count, 1 - correctly_placed_tiles_count) 

# # ---------------------------------------------------------------------

# def h(board):
#     canonical_config = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4), 
#                         6: (1, 0), 7: (1, 1), 8: (1, 2), 9: (1, 3), 10: (1, 4), 
#                         11: (2, 0), 12: (2, 1), 13: (2, 2), 14: (2, 3), 15: (2, 4), 
#                         16: (3, 0), 17: (3, 1), 18: (3, 2), 19: (3, 3), 20: (3, 4), 
#                         21: (4, 0), 22: (4, 1), 23: (4, 2), 24: (4, 3), 25: (4, 4)}

#     sum_manhattan_distance = 0.0

#     tuple_board = ()
#     for i in range(len(board)):
#         tuple_board += tuple(board[i])

#     # find the sum of manhattan distances for each element for all the 25 elements
#     for index, value in enumerate(tuple_board):
#         row, column = int(index / 5), index % 5
#         sum_manhattan_distance += abs(row - canonical_config[value][0]) + abs(column - canonical_config[value][1])
    
#     return sum_manhattan_distance

# # ---------------------------------------------------------------------

# from queue import PriorityQueue
# def solve(initial_board):
#     """
#     1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
#     2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
#        For testing we will call this function with single argument(initial_board) and it should return 
#        the solution.
#     3. Please do not use any global variables, as it may cause the testing code to fail.
#     4. You can assume that all test cases will be solvable.
#     5. The current code just returns a dummy solution.
#     """
#     board = np.array(initial_board).reshape(ROWS, COLS).tolist() 
    
#     # main code for execution.. just to change the heuristic function now...
#     fringe = PriorityQueue()
#     fringe.put((h(deepcopy(board)), (deepcopy(board), "")))
    
#     step_counter = 0
#     visited_list = []
    
#     while fringe:
#         step_counter += 1
#         state_tuple = fringe.get()
#         (_, (state, path)) = state_tuple
#         visited_list.append(state)

#         if is_goal(deepcopy(state)):
#             return path.split(" ")

#         successor_states = successors(deepcopy(board))
#         # print(successor_states)
#         # break

#         # print(f"----------step counter = {step_counter}-----------------")
#         for s in successor_states:
#             if s[0] not in visited_list:
#                 print((h(deepcopy(s[0])), (deepcopy(s[0]), path + " " + s[1])))
#                 fringe.put((h(deepcopy(s[0])), (deepcopy(s[0]), path + " " + s[1])))


# # Please don't modify anything below this line
# if __name__ == "__main__":
#     if(len(sys.argv) != 2):
#         raise(Exception("Error: expected a board filename"))

#     start_state = []
#     with open(sys.argv[1], 'r') as file:
#         for line in file:
#             start_state += [ int(i) for i in line.split() ]

#     if len(start_state) != ROWS*COLS:
#         raise(Exception("Error: couldn't parse start state file"))

#     print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

#     print("Solving...")
#     route = solve(tuple(start_state))
    
#     print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))


# # there will be 24 states
# # slide row left (5 states)
# # slide row right (5 states)
# # slide row top (5 states)
# # slide row bottom (5 states)
# # rotating the inner board clockwise
# # rotating the inner board anticlockwise

# # rotating the outer board clockwise
# # rotating the outer board anticlockwise
# # write the functions for each of them
# # after that use the part 1 logic to formulate the solution 
# # heuristic will be sum of manhattan distances from start to end
# # choose the best possible move chosen from priority queue

