import random

class Player:
    fitness = 0
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    canwalk = True
    win = False

    def __init__(self, init, end, maze):
        self.path = [init]
        self.maze = maze
        self.end = end
        self.color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))

    def __str__(self):
        return str(self.path) + " Fitness: " + str(self.fitness)

    def _inside(self, y, x):
        return 0 <= x < self.maze.width and 0 <= y < self.maze.height

    def _getnewpos(self, d):
        return self.path[-1][0] + d[0], self.path[-1][1] + d[1]

    def _isvaliddir(self, d):
        newpos = self._getnewpos(d)
        return self._inside(newpos[0],newpos[1]) and self.maze.getMaze()[newpos[0]][newpos[1]] == (255,255,255) and newpos not in self.path

    def onestep(self):
        if self.canwalk:
            validDirections = list(filter(lambda d: self._isvaliddir(d), self.dirs))
            if len(validDirections) > 0:
                self.path.append(self._getnewpos(random.choice(validDirections)))
                if self.path[-1] == self.end:
                    self.canwalk = False
                    self.win = True
            else:
                self.canwalk = False

    def walk(self):
        while self.canwalk:
            self.onestep()

    def evaluate(self):
        self.walk()
        if self.win:
            self.fitness = 1  # Max fitness if the player reaches the end
        else:
            self.fitness = 1 / (1 + len(self.path))  # Fitness based on the length of the path

    def crossover(self, partner):
        child = Player(self.path[0], self.end, self.maze)
        index = 80 * len(self.path) // 100
        child.path = self.path[:index] + partner.path[index:]
        return child

    def mutate(self):
        if len(self.path) > 1:
            self.path = self.path[:-1]  # Remove the last element in the path









