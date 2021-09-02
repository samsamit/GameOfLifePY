from Colors import BLACK, BUTTON_COLOR
import pygame as pg


class Ui:
    nroOfButtons = 4
    buttonBorderSize = 2
    buttonColor = BUTTON_COLOR
    textColor = BLACK

    def __init__(self, game) -> None:
        self.game = game
        self.resize()
        pass

    def update(self):
        self.uiSurface.fill(BLACK)

    def draw(self):
        pg.draw.rect(self.uiSurface, self.buttonColor, self.evolveButton)
        self.uiSurface.blit(self.evolveButtonText, self.evolveButton.topleft)
        pg.draw.rect(self.uiSurface, self.buttonColor, self.playButton)
        self.uiSurface.blit(
            (self.pauseButtonText if self.game.evolvePlay else self.playButtonText),
            self.playButton.topleft,
        )
        pg.draw.rect(self.uiSurface, self.buttonColor, self.addCellsButton)
        self.uiSurface.blit(self.addCellsButtonText, self.addCellsButton.topleft)
        pg.draw.rect(self.uiSurface, self.buttonColor, self.removeCellsButton)
        self.uiSurface.blit(self.removeCellsButtonText, self.removeCellsButton.topleft)
        self.game.window.blit(
            self.uiSurface,
            (
                0,
                self.game.window_size[1]
                - int(self.game.window_size[1] * self.game.UI_HEIGHT),
            ),
        )

    def resize(self):
        self.uiSurface = pg.Surface(
            (
                self.game.window_size[0],
                int(self.game.window_size[1] * self.game.UI_HEIGHT),
            )
        )
        buttonHeight = (int(self.game.window_size[1] * self.game.UI_HEIGHT)) - (
            self.buttonBorderSize * 2
        )
        buttonWidth = (self.game.window_size[0] / self.nroOfButtons) - (
            self.buttonBorderSize * 2
        )

        font = pg.font.SysFont("arial", buttonHeight)

        self.playButton = pg.Rect(
            ((self.buttonBorderSize * 1), self.buttonBorderSize),
            (buttonWidth, buttonHeight),
        )
        self.playButtonText = font.render("Play", True, self.textColor)
        self.pauseButtonText = font.render("Pause", True, self.textColor)

        self.evolveButton = pg.Rect(
            ((self.buttonBorderSize * 3) + buttonWidth, self.buttonBorderSize),
            (buttonWidth, buttonHeight),
        )
        self.evolveButtonText = font.render("EVOLVE", True, self.textColor)

        self.addCellsButton = pg.Rect(
            (
                (self.buttonBorderSize * 5 + (buttonWidth * 2), self.buttonBorderSize),
                (buttonWidth, buttonHeight),
            )
        )
        self.addCellsButtonText = font.render("+ Cells", True, self.textColor)

        self.removeCellsButton = pg.Rect(
            ((self.buttonBorderSize * 7) + (buttonWidth * 3), self.buttonBorderSize),
            (buttonWidth, buttonHeight),
        )
        self.removeCellsButtonText = font.render("- Cells", True, self.textColor)

    def onClick(self, clickPos):
        posX = clickPos[0]
        posY = clickPos[1] - (
            self.game.window_size[1]
            - int(self.game.window_size[1] * self.game.UI_HEIGHT)
        )
        if self.playButton.collidepoint((posX, posY)):
            print("autoevolve")
            self.game.evolvePlay = not self.game.evolvePlay
        if self.evolveButton.collidepoint((posX, posY)):
            self.game.evolve()
        if self.addCellsButton.collidepoint((posX, posY)):
            self.game.changeCellCount(1)
        if self.removeCellsButton.collidepoint((posX, posY)):
            self.game.changeCellCount(-1)
