from Colors import CELL_COLOR, DEAD_CELL_COLOR
import random
import pygame as pg
from enum import Enum


class CellState(Enum):
    EMPTY = DEAD_CELL_COLOR
    ALIVE = CELL_COLOR


class Cell:
    CELL_BORDER_SIZE = 1  # percent of th ebase size

    def __init__(self, gameMap, pos) -> None:
        self.map = gameMap
        self.pos = pos
        self.state = CellState.EMPTY
        self.prepareState = CellState.EMPTY
        pass

    def update(self):
        pass

    def draw(self, pos):
        self.calcNeighbours()
        self.base = pg.Surface((self.map.cellSize, self.map.cellSize))
        self.baseRect = self.base.get_rect()
        self.baseRect.topleft = pos
        self.base.fill(pg.Color("pink"))
        borderSize = self.CELL_BORDER_SIZE
        if borderSize < 1:
            borderSize = 1
        cellSize = self.map.cellSize - (borderSize * 2)
        self.cell = pg.Rect((borderSize, borderSize), (cellSize, cellSize))
        pg.draw.rect(self.base, self.state.value, self.cell)
        self.map.mapSurface.blit(self.base, pos)

    def onClick(self, clickPos):
        x = clickPos[0] - self.map.mapPos[0]
        y = clickPos[1] - self.map.mapPos[1]
        if self.baseRect.collidepoint((x, y)):
            if self.state == CellState.EMPTY:
                self.state = CellState.ALIVE
            elif self.state == CellState.ALIVE:
                self.state = CellState.EMPTY

    def calcNeighbours(self):
        x, y = self.pos
        self.neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nX = x + i
                nY = y + j
                if nX == x and nY == y:
                    continue
                try:
                    if self.map.game.cells[nX][nY].state == CellState.ALIVE:
                        #                        print(nX, nY)
                        self.neighbours += 1
                except Exception:
                    pass

    def prepareEvolution(self):
        if self.state == CellState.ALIVE:
            if self.neighbours < 2 or self.neighbours > 3:
                self.prepareState = CellState.EMPTY
            else:
                self.prepareState = CellState.ALIVE
        if self.state == CellState.EMPTY:
            if self.neighbours == 3:
                self.prepareState = CellState.ALIVE

    def evolve(self):
        self.state = self.prepareState
