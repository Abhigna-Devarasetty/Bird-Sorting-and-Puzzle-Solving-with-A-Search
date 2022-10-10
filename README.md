# scheedu-srmhalgi-vdevaras-a1

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
