from Colors import BLACK
import pygame as pg


class Map:
    def __init__(self, game) -> None:
        self.game = game
        self.resize()

    def update(self):
        self.mapSurface.fill(BLACK)

    def draw(self):
        self.drawCells()
        self.game.window.blit(self.mapSurface, self.mapPos)

    def getMapSize(self):
        w, h = self.mapArea
        if w > h:
            size = (h, h)
            pos = ((w - h) / 2, 0)
        else:
            size = (w, w)
            pos = (0, (h - w) / 2)
        return size, pos

    def getMApPosition(self):
        w, h = self.mapArea

    def resize(self):
        self.mapArea = (
            self.game.window_size[0],
            int(self.game.window_size[1] * (1.0 - self.game.UI_HEIGHT)),
        )
        print(self.mapArea)
        self.mapSize, self.mapPos = self.getMapSize()
        self.mapSurface = pg.Surface(self.mapSize)
        self.cellSize = int(self.mapSize[0] / self.game.cellsPerRow)

    def drawCells(self):
        for i in range(self.game.cellsPerRow):
            for j in range(self.game.cellsPerRow):
                thisCell = self.game.cells[i][j]
                thisCell.draw(((i * self.cellSize), (j * self.cellSize)))
