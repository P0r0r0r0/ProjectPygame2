import pygame


class Border(pygame.sprite.Sprite):
    def __init__(self, group, x1, y1, x2, y2):
        super().__init__(group)
        self.image = pygame.Surface([1, y2 - y1])
        self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        self.mask = pygame.mask.from_surface(self.image)