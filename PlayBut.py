import sys

import pygame

font = pygame.font.SysFont('Arial', 40)


class PlayBut:
    def __init__(self, x, y, width, height, buttonText='Play', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.oneclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {'normal': '#ffffff', 'hover': '#666666', 'pressed': '#333333'}

        self.buttonSurface = pygame.Surfase((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))