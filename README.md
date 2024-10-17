# Maze-Solver-Path-Finder-using-Genetic-Algorithms

Whole PDf of Research is given in pdf with code

Abstract.

In the realm of computational problem-solving, finding efficient
paths is key, especially when it comes to navigating through mazes.
This project focuses on improving maze-solving efficiency by combining
Genetic Algorithms (GA) with the A* pathfinding algorithm.
We begin by demonstrating the A* algorithm’s ability to immediately
pinpoint the ideal path using a heuristic-based method. To
build upon this, we integrate GA, capitalizing on its iterative selection,
crossover, and mutation processes to further optimize our solutions.
In addition, the performance of GA as an independently mazesolving
method is evaluated.


The results show while the A* algorithm solves mazes quickly,
combining it with GA produces even more optimal solutions in a
manageable timescale, in contrast to the significantly slower performance
of GA when used alone. This project investigates the possibility
of improving problem-solving approaches by combining traditional
rule-based algorithms with evolutionary algorithms, with the
goal of developing more sophisticated and effective solutions.



Experiments and results

A. A* Approach : The Foundation


The initial phase of my study focuses on the A* pathfinding algorithm.
To build a performance baseline, it was critical to understand
A*’s independent performance in maze-solving scenarios. This exploration
on A*’s independent capabilities was important for identifying
its strengths and limitations. This fundamental understanding
of A* served as the foundation for developing and testing the hybrid
approach with GA.


1. Explanation
Initial Pathfinding with A*: The A* algorithm makes use of the
Manhattan Distance heuristic, which is particularly well-suited for
applications that are grid-based. By calculating the sum of the absolute
differences in the coordinates of the nodes, this heuristic
makes the process of estimating the cost between the nodes more
straightforward. To broaden our understanding and explore alternative
heuristics, we also implemented the A* algorithm using Euclidean
Distance in certain scenarios. Unlike Manhattan Distance,
Euclidean Distance measures the straight-line distance between two
points, which can be more direct but less reflective of actual path
costs in a grid maze.

Output:
![image](https://github.com/user-attachments/assets/543c0fd6-8df1-4cd0-9535-706b9de17cd4)

The output from the A* algorithm provided a direct, unambiguous
path through the maze, as opposed to the iterative approach seen with
Genetic Algorithms (GA). The result was a clear sequence of coordinates,
illustrating the step-by-step journey from the maze’s entrance
to the exit.


B. Hybrid Approach: A* Enhanced by GA

The hybrid technique merges the heuristic accuracy of A* with the
evolutionary problem-solving abilities of GA. The main objective is
to utilize the efficient pathfinding capabilities of the A* algorithm as
a foundation, which is subsequently improved and optimized by the
Genetic Algorithm (GA) over multiple generations. 

Incorporating A* Path into GA: The Genetic Algorithm (GA) then
takes over, using the path found by A* as one of its initial potential
solutions. This inclusion ensures that the GA has a solid, viable
starting point, influencing its evolutionary process greatly. In our GA
setup, a population of these path solutions are created . To add genetic
diversity, the population with different versions of the A* path
are chosen.

Output:
![image](https://github.com/user-attachments/assets/6d0cec45-79b6-4a1d-a7ee-75b454705b38)



C. Genetic Algorithm: Independent Exploration

After diving into the technique of integrating the A* algorithm with
Genetic Algorithms (GA) and studying A*’s standalone capabilities
in maze solution, it’s time to turn our attention entirely to the Genetic
Algorithm. This independent examination of GA will not only highlight
its strengths and limitations but also provide a comprehensive
comparison with the previously discussed A* algorithm and A* and
GA Hybrid approach.



Whole PDf of Research is given in pdf with code. 


