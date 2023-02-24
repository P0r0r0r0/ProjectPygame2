import pygame


class Level:
    def __init__(self, left=0, right=0):  # настройка основного окна игры
        game_size = width, height = 1500, 800
        self.screen = pygame.display.set_mode(game_size)

