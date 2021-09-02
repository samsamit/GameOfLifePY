import time
from cell import Cell
from map import Map
from ui import Ui
import pygame as pg
import sys


class Game:
    UI_HEIGHT = 0.1  # Percent of the window height
    EVOLVE_INTERVAL = 0.5  # second

    def __init__(self) -> None:
        # Game
        pg.init()
        pg.display.set_caption("Game Of Life")
        self.clock = pg.time.Clock()
        self.running = True
        self.evolvePlay = False
        self.evolveTick = 0

        # Settings
        self.cellsPerRow = 50

        # Window
        self.window_size = (700, 500)
        self.window = pg.display.set_mode(self.window_size, pg.RESIZABLE)

        # Ui
        self.ui = Ui(self)

        # map
        self.map = Map(self)

        # cells
        self.cells = self.getCells()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
            self.handleAutoEvolve()

    def update(self):
        self.ui.update()
        self.map.update()
        pass

    def handleAutoEvolve(self):
        if self.evolvePlay and self.EVOLVE_INTERVAL < time.time() - self.evolveTick:
            self.evolve()
            self.evolveTick = time.time()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.VIDEORESIZE:
                self.handleResize()
            if event.type == pg.MOUSEBUTTONUP:
                self.handleClick(pg.mouse.get_pos())

    def draw(self):
        self.map.draw()
        self.ui.draw()
        pg.display.flip()

    def handleResize(self):
        self.window_size = pg.display.get_surface().get_size()
        self.ui.resize()
        self.map.resize()

    def quit(self):
        pg.quit()
        sys.exit()

    def getCells(self):
        newCells = []
        for i in range(self.cellsPerRow):
            newRow = []
            for j in range(self.cellsPerRow):
                newCell = Cell(self.map, (i, j))
                newRow.append(newCell)
            newCells.append(newRow)
        return newCells

    def handleClick(self, clickPos):
        for i in range(self.cellsPerRow):
            for j in range(self.cellsPerRow):
                self.cells[i][j].onClick(clickPos)

        self.ui.onClick(clickPos)

    def evolve(self):
        for i in range(self.cellsPerRow):
            for j in range(self.cellsPerRow):
                self.cells[i][j].prepareEvolution()
        for i in range(self.cellsPerRow):
            for j in range(self.cellsPerRow):
                self.cells[i][j].evolve()

    def changeCellCount(self, change):
        newCellCount = self.cellsPerRow + change
        if newCellCount < 1:
            return
        self.cellsPerRow = newCellCount
        self.cells = self.getCells()
        print(f"new cell count = {self.cellsPerRow}")
        self.handleResize()


game = Game()
while True:
    game.run()
