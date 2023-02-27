import pygame

from functions import load_image


class people_2(pygame.sprite.Sprite):  # спрайт правого игрока
    STEP = 10
    """
        аргументы:
        group - pygame.sprite.Group
        x_coord, y_coord - координаты (int)
        bord2 - стенка (Border)
        net - сетка (Net)
        """

    def __init__(self, group, x_coord, y_coord, bord2, net):
        super().__init__(group)
        self.File_name = 'low2.png'
        self.image = load_image(self.File_name)
        self.image = pygame.transform.scale(self.image, (350, 350))

        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.mask = pygame.mask.from_surface(self.image)
        self.bord2 = bord2
        self.net = net

    def update(self, *args):  # обработка нажатий клавиш и движений
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_LEFT:
                if not pygame.sprite.collide_mask(self, self.net):
                    self.rect.x -= self.STEP
            elif args[0].key == pygame.K_RIGHT:
                if not pygame.sprite.collide_mask(self, self.bord2):
                    self.rect.x += self.STEP
            elif args[0].key == pygame.K_UP:
                self.File_name = 'high2.png'
                self.image = load_image(self.File_name)
                self.image = pygame.transform.scale(self.image, (350, 350))
                self.mask = pygame.mask.from_surface(self.image)
            elif args[0].key == pygame.K_DOWN:
                self.File_name = 'low2.png'
                self.image = load_image(self.File_name)
                self.image = pygame.transform.scale(self.image, (350, 350))
                self.mask = pygame.mask.from_surface(self.image)
