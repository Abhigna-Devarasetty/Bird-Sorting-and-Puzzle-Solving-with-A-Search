# Part 1 : Birds, heuristics, and A*

The Goal of the problem is to arrange the given birds numbered from 1 to 5 under 10 seconds. The implemented code is taking time as it is exploring all the successor states. We need to tweak in a heuristic function that gives priority to the states which find the solution in minimum time.

The problem can be approached in various ways. The first thing which comes to our mind is the problem is actually a sorting problem and can be implemented using bubble sort (sorting 2 adjacent positions) until the whole list is sorted. This does not consider any heuristic function, and is purely a sorting problem.
<br>
However, we want to apply a heuristic function and A* algorithm to find solution to the problem. To apply the A* algorithm, we need to define a heuristic function and expand the next states according to highest priority (the state which takes us closer to goal state is expanded first).

The solution for problem 1 can be implemented in the following manner:
<br>
1. The fringe which is given as a list can be changed into Priority Queue. The reason for switching to priority queue is the fringe of greater importance was directly getting appended in the fringe list, and hence was taking time to expand the state and move closer to the goal position. To overcome this, we wanted to have some mechanism of sorting the elements according to priority. The Priority Queue is the best data structure to tackle this problem. After implementing the priority queue in the code, the problem was solved within 10 seconds.
2. The heuristic function (h(s)) which is applied is the Manhattan Distance absolute_value(orignal_position - current_position) that is summed over all the states.
f(s) = g(s) + h(s) 
where h(s) is the heuristic function and g(s) is the step count.
The code for heuristic function is given below:
<br>
def h(state):
<br>
&nbsp&nbsp&nbsp&nbsp    manhattan_dist = 0
    <br>
&nbsp&nbsp&nbsp&nbsp    for i in range(len(state)):
        <br>
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp        manhattan_dist += abs(i + 1 - state[i])
    <br>
&nbsp&nbsp&nbsp&nbsp    return manhattan_dist
<br>
<br>
3. The bird can only swipe positions with one of the adjacent birds. Hence there will be maximum 2 admissible successor states for this problem.

<h2>
  Approach to reach the solution
</h2>
1. Researched about the implementation of Priority Queue in Python. (https://towardsdatascience.com/introduction-to-priority-queues-in-python-83664d3178c3)
<br>
2. Changed the fringe from a list to the Priority Queue.
<br>
3. Implemented the manhattan heuristic function in h() method  

<br>
By doing all the above steps, the solution of problem 1 is coming under 10 seconds



# Part 2 : The 2022 Puzzle

<h2> 1. In this problem, what is the branching factor of the search tree? </h2>
There are 24 successor states. So each node will have 24 leaves and hence the branching factor of the search tree is 24.

<h2> 2. If the solution can be reached in 7 moves, about how many states would we need to explore before we
found it if we used BFS instead of A* search? A rough answer is fine. </h2>
If the solution can be reached in 7 moves then we will need to explore 7^24 states if we used BFS instead of A* search.

The Goal of the problem is to arrange a randomly shuffled board in the canonical form. The board can moved in 24 ways. 
1. sliding the row left (L1, L2, L3, L4, L5) -> 5 states
2. sliding the row right (R1, R2, R3, R4, R5) -> 5 states
3. sliding the row top (U1, U2, U3, U4, U5) -> 5 states
4. sliding the row bottom (D1, D2, D3, D4, D5) -> 5 states
5. rotating the board inner board clockwise -> 1 state
6. rotating the inner board anticlockwise -> 1 state
7. rotating the outer board clockwise -> 1 state
8. rotating the outer board anticlockwise -> 1 state
## Total States = 24

The heuristic function will be the sum of manhattan distances. This heuristic function works well on simple problems and is able to give solution to simple boards but fails for complex boards (board 1). So, we tried out the below heuristic functions
1. Manhattan Distance
2. Euclidian Distance
The above heuristic functions were giving suboptimal solution and the board was getting solved in around 20 moves. 
I observed that the optimal path was getting found in 11 moves, and the paths were getting explored for no reason.
So we needed to limit the path which was getting traversed hence I introduced the length of the path in the heuristic function and multiplied by a random factor 0.3 (found this number by randomly exploring the list of values) and finally the heuristic which works on board 2 and is solving the 2 test cases for board 0 and board 1
<br>
The final heuristic function which was implemented was : <b> h(s) = sum_of_manhattan_distance + (len(path) ^ 2) * 0.3 </b>
<br>

<h3> Coding Approach towards the problem : </h3>
1. First I figured out that there will be 24 successive states for the problem, and wrote the functions for each of them. There are 8 functions in the code,  
<br>
a. move_left -> (implements 5 states)
<br>
b. move_right -> (implements 5 states)
<br>
c. move_up -> (implements 5 states)
<br>
d. move_down -> (implements 5 states)
<br>
e. move_outer_clockwise -> (implements 1 state)
<br>
f. move_outer_counter_clockwise -> (implements 1 state)
<br>
g. move_inner_clockwise -> (implements 1 state)
<br>
h. move_inner_counter_clockwise -> (implements 1 state)
<br>
2. Then I wrote the peripheral code of getting the successor states and implemented the A* algorithm with Manhattan distance. 
3. Finally, explored the various heuristic functions and implemented the same to solve the problem

<br>
I have made sure that efficient coding practices are applied and the code runs in minimum time as possible. 

<h3> Problems Faced : </h3>
I implemented the successor states but the solution was not coming as the successor states were getting updated on the same board. I figured out the problem and understood that I was not using deepcopy function to preserve the orignal state of the board. Finally, I debuged and implemented the code and wrote the final successor functions and implemented the heuristic function to get the solution for board 0 and board 1.
<br>
Finding the heuristic function was difficult. I am not sure that the heuristic function works for other test cases but this heuristic function works for the 2 test cases which are provided, and we are getting the optimal solution in under 15 minutes.


# Part 3 : Road Trip!


The Goal of the problem is to find the best route from given source to destination. We also have to calculate the total number of segments covered, distance travelled in miles and the cost and time incurred to travel the calculated distance. Additional to this we also need to calculate the number of hours that would take to make a delivery drive.

In our given dataset of major highway segments of the United States (and parts of southern Canada and northern Mexico), we have some missing data points too. For these missing points, we are not provided with any latitude or longitude positions for that position. In these cases, we have considered the average latitude and logitude of neighboorhood locations for the given place and placed an approximate latitude and longitude values.

The best route can be found in different ways. Our approach is to find the distance between source and destination using Haversine Formula:
    hav(c)=hav(a-b)+sin(a)sin(b)hav(C)
Using this formula, we calculating the distance between 

As we have to use a heuristic function and A* algorithm to find best orute. To apply the A* algorithm, we need to define a heuristic function and get the next intermidiate distance based on the priprity decided by the heuristic function. Our Heuristic function would calculate the distanc between the source and destination nodes.

Implementation of solution goes as follows,

1. In the get_route(), we push the initial (start point to the fringe) and have list of visited nodes and path, which would prevent us from coming to the same place again and again.

2. Then we find the successor node, the successor node would be one of the neighbooring nodes which ever distance is less to destination when compared to other negihbooring nodes.

3. We also have helper functions for total segment cost, total time cost, total distance cost and one for total delivery distance cost. These functions would return the total cost incurred after reaching th the successor node.

4. In the helper functions mentioned in the above step, we add up the current total cost, current cost and heuristic cost after reaching every location.

5. Here we also have to calculate one more step for delivery drive, if the delivery truck exceeds a speed limit of 50 mph, then the items in the truch would be destroyed. So the cost of this trip would be more for this. In this case, the driver goes back to source node after reaching the destination. We calculate the distance based on the given formula, troad + p · 2(troad + ttrip)

6. By performing all the above steps until we reach the destination, we will have our distance in many routes, out of that we have a function which calculates and returns the minimum distance between given two locations
