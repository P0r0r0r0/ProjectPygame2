import pygame

from functions import load_image


class Ball(pygame.sprite.Sprite):  # спрайт мяча
    File_name = 'voleyball_ball.png'
    STEP = 2

    def __init__(self, group, x_coord, y_coord, net, ground, pep1, pep2):
        super().__init__(group)

        self.image = load_image(self.File_name)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.net = net
        self.ground = ground
        self.pep1 = pep1
        self.pep2 = pep2
        self.flag1 = False
        self.flag2 = False

    def update(self, *args):  # его поведение
        if pygame.sprite.collide_mask(self, self.pep1):
            self.flag1 = True
            self.diff = self.rect.x
            self.y = self.rect.y

        if self.flag1:
            if self.pep1.File_name == 'high.png':
                x = self.rect.x - self.diff - 260
                y = int(((1 / 150) * x ** 2) - 450)
                self.rect.y = self.y + y
                self.STEP = 3
            elif self.pep1.File_name == 'low.png':
                x = self.rect.x - self.diff - 442
                y = int(((1 / 650) * x ** 2) - 300)
                self.rect.y = self.y + y
                self.STEP = 6
            self.rect.x += self.STEP
