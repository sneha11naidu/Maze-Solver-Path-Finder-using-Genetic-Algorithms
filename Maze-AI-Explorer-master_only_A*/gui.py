import pygame, os
from maze import Maze
from AStar import *
import config as cf
class MainWindow:
    width = 100
    height = 100
    blockSize = 10
    title = ""
    display = None
    pixelArray = None
    maze = None
    def __init__(self, title, width, height, blocksize):
        self.title  = title
        self.maze = Maze(width, height)
        self.blockSize = blocksize
        self.width = self.maze.width*self.blockSize
        self.height = self.maze.height*self.blockSize
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.pixelArray = pygame.PixelArray(self.display)

    def _drawPixel(self, x, y, color):
        if 0<=x<self.width and 0<=y<self.height:
            self.pixelArray[x, y] = color

    def drawRectangle(self, sx, sy, width, height, color):
        for y in range(sy,sy+height):
            for x in range(sx, sx+width):
                self._drawPixel(x,y, color)
        pygame.display.update()
    def genMaze(self):
        genMaze = True
        while genMaze:
            pygame.time.Clock()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    genMaze = False
                    break
            for y, x in self.maze.getToDraw():
                self.drawRectangle(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize,
                                     self.maze.getColor(y, x))
            if len(self.maze.frontier) == 0:
                genMaze = False
                break
            pygame.display.update()
            self.maze.workOneStep()


"""
    to change configuration, change config.py
"""
if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    window = MainWindow(cf.WINDOW_TITLE, cf.MAZE_WIDTH, cf.MAZE_HEIGHT, cf.BLOCK_SIZE)
    window.genMaze()

    # Initialize MazeSolver with start and end coordinates, and the maze
    maze_solver = MazeSolver(cf.START_COORDS, cf.END_COORDS, window.maze)

    # Solve the maze
    path = maze_solver.solve()  # This should return the path

    run = True
    while run:
        pygame.time.Clock().tick(60)  # Control the frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Draw the path
        if path:  # Ensure path is not None
            for y, x in path:
                window.drawRectangle(x * window.blockSize, y * window.blockSize, window.blockSize, window.blockSize, (0, 255, 0))  # Drawing path in green

        pygame.display.update()

    pygame.quit()
