import pygame


class Level:
    def __init__(self):
        game_size = width, height = 1500, 800
        self.game_screen = pygame.display.set_mode(game_size)
        self.game_screen.fill(pygame.Color(150, 255, 150))