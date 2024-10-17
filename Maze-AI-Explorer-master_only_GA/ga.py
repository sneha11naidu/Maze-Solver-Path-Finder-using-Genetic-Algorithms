from Player import *

class GA:
    population = []
    bestp = []
    victory = False
    bestPlayer = None

    def __init__(self, gen, popsize, mr, init, end, maze):
        self.gen = gen
        self.curgen = 0
        self.popsize = popsize
        self.mr = mr
        self.init = init
        self.end = end
        self.initPopulation(init, end, maze)

    def initPopulation(self, init, end, maze):
        for i in range(self.popsize):
            self.population.append(Player(init, end, maze))
        self._fitness()

    def getMaxFitness(self):
        return max(p.fitness for p in self.population)

    def _fitness(self):
        for p in self.population:
            p.evaluate()

    def _selection(self):
        selected = []
        for i in range(self.popsize):
            parentA, parentB = random.sample(self.population, 2)
            child = parentA.crossover(parentB)
            selected.append(child)
        self.population = selected

    def _mutation(self):
        for p in self.population:
            if random.random() <= self.mr:
                p.mutate()

    def nextGen(self):
        self.curgen += 1
        self._selection()
        self._mutation()
        self._fitness()
        self.bestPlayer = max(self.population, key=lambda x: x.fitness)
        if self.bestPlayer.fitness == 1:
            self.victory = True










