import sys

import pygame


class PlayBut:  # создание кнопок
    def __init__(self, x, y, width, height, screen, objects, perem, buttonText, onclickFunction=None):
        font = pygame.font.SysFont('Arial', 40)  # их внешний вид
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.alreadyPressed = False
        self.screen = screen
        self.perem = perem
        self.text = buttonText
        self.onePress = True
        self.button = True

        self.fillColors = {'normal': '#ffffff', 'hover': '#666666', 'pressed': '#333333'}

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(self.text, True, (20, 20, 20))
        objects.append(self)

    def process(self):  # их поведение
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.perem.append(self.text)
                    self.onclickFunction()
                    if self.text != 'Home':
                        self.button = False
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        if self.button:
            self.screen.blit(self.buttonSurface, self.buttonRect)
