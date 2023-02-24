import pygame

from functions import load_image


class Ball(pygame.sprite.Sprite):  # спрайт мяча
    File_name = 'voleyball_ball.png'
    STEP = 10

    def __init__(self, group, x_coord, y_coord):
        super().__init__(group)

        self.image = load_image(self.File_name)
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord

    def update(self, *args):  # его поведение
        pass