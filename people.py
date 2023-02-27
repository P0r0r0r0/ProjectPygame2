import pygame

from functions import load_image


class people_1(pygame.sprite.Sprite):  # спрайт левого игрока
    STEP = 10
    """
    аргументы:
    group - pygame.sprite.Group
    x_coord, y_coord - координаты (int)
    bord1 - стенка (Border)
    net - сетка (Net)

    """
    def __init__(self, group, x_coord, y_coord, bord1, net):
        super().__init__(group)
        self.index = 0
        self.File_name = 'low.png'
        self.image = load_image(self.File_name)
        self.image = pygame.transform.scale(self.image, (350, 350))

        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.mask = pygame.mask.from_surface(self.image)
        self.bord1 = bord1
        self.net = net

    def update(self, *args):  # обработка нажатий клавиш и движений
        if args and args[0].type == pygame.TEXTINPUT:
            if args[0].text == 'a' or args[0].text == 'ф':
                if not pygame.sprite.collide_mask(self, self.bord1):
                    self.rect.x -= self.STEP
            elif args[0].text == 'd' or args[0].text == 'в':
                if not pygame.sprite.collide_mask(self, self.net):
                    self.rect.x += self.STEP
            elif args[0].text == 'w' or args[0].text == 'ц':
                self.File_name = 'high.png'
                self.image = load_image(self.File_name)
                self.image = pygame.transform.scale(self.image, (350, 350))
                self.mask = pygame.mask.from_surface(self.image)
            elif args[0].text == 's' or args[0].text == 'ы':
                self.File_name = 'low.png'
                self.image = load_image(self.File_name)
                self.image = pygame.transform.scale(self.image, (350, 350))
                self.mask = pygame.mask.from_surface(self.image)
