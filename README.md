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

# Part 3 : Road Trip!


The Goal of the problem is to find the best route from given source to destination. We also have to calculate the total number of segments covered, distance travelled in miles and the cost and time incurred to travel the calculated distance. Additional to this we also need to calculate the number of hours that would take to make a delivery drive.

In our given dataset of major highway segments of the United States (and parts of southern Canada and northern Mexico), we have some missing data points too. For these missing points, we are not provided with any latitude or longitude positions for that position. In these cases, we have considered the average latitude and logitude of neighboorhood locations for the given place and placed an approximate latitude and longitude values.

The best route can be found in different ways. Our approach is to find take latitude and longitude for both source and destination and calculate the difference between them, i.e, basically calculating the distance between both the locations.

As we have to use a heuristic function and A* algorithm to find best orute. To apply the A* algorithm, we need to define a heuristic function and get the next intermidiate distance based on the priprity decided by the heuristic function. Our Heuristic function would calculate the distanc between the source and destination nodes.

Implementation of solution goes as follows,

1. In the get_route(), we push the initial (start point to the fringe) and have list of visited nodes and path, which would prevent us from coming to the same place again and again.

2. Then we find the successor node, the successor node would be one of the neighbooring nodes which ever distance is less to destination when compared to other negihbooring nodes.

3. We also have helper functions for total segment cost, total time cost, total distance cost and one for total delivery distance cost. These functions would return the total cost incurred after reaching th the successor node.

4. In the helper functions mentioned in the above step, we add up the current total cost, current cost and heuristic cost after reaching every location.

5. Here we also have to calculate one more step for delivery drive, if the delivery truck exceeds a spped limit of 50 mph, then the items in the truch would be destroyed. So the cost of this trip would be more for this. In this case, the driver goes back to source node after reaching the destination. That would be the double the cost of time and distance.

6. By performing all the above steps until we reach the destination, we will have our total time, distance and segmentation cost for the trip.
