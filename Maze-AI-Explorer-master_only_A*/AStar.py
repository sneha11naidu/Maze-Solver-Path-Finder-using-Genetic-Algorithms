from utils import pathfinding, manhattan

class MazeSolver:
    def __init__(self, init, end, maze):
        self.init = init
        self.end = end
        self.maze = maze

    def solve(self):
        path = pathfinding(self.init, self.end, self.maze.getMaze())
        if path:
            print("Path found:", path)
            return path  # Return the found path
        else:
            print("No path found")
            return []  # Return an empty list if no path is found

    def display_path(self, path):
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if (y, x) in path:
                    print("*", end="")
                elif self.maze.getMaze()[y][x] == (255, 255, 255):
                    print(" ", end="")
                else:
                    print("#", end="")
            print()


