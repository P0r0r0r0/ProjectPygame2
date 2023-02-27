import pygame
import random

from functions import load_image
from functions import new_round


class Ball(pygame.sprite.Sprite):  # спрайт мячика
    """аргументы:
    group - спрайт мяча (pygame.sprite.Group)
    x_coord, y_coord - координаты мяча (int)
    goals - счетчик голов (List)
    net - сетка (Net)
    ground - земля (Ground)
    pep1 - левый человечек (people_1)
    pep2 - правый человечек (people_2)
    """
    File_name = 'voleyball_ball.png'
    STEP = 5

    def __init__(self, group, x_coord, y_coord, goals, net, ground, pep1, pep2):
        super().__init__(group)

        self.image = load_image(self.File_name)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.goals = goals
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.net = net
        self.ground = ground
        self.pep1 = pep1
        self.pep2 = pep2
        self.fl = False
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False
        self.flag4 = False
        self.spflag1 = False
        self.spflag2 = False
        self.spflag3 = False
        self.spflag4 = False

    def update(self, *args):  # его поведение
        """обрабатывает поведение мяча и его столкновения с разными объектами"""
        if self.STEP == 5:
            if args and (args[0].type == pygame.KEYDOWN or args[0].type == pygame.TEXTINPUT):
                self.fl = True
        if pygame.sprite.collide_mask(self, self.pep1):  # столкновение с левым человеком
            self.flag2 = False
            self.flag1 = True
            self.fl = False
            self.diff = self.rect.x
            self.y = self.rect.y
            self.spflag3 = False
            self.spflag4 = False
            """учитывает верхнюю и нижнюю подачю"""
            if self.pep1.File_name == 'high.png':
                self.spflag1 = True
            elif self.pep1.File_name == 'low.png':
                self.spflag2 = True

        elif pygame.sprite.collide_mask(self, self.pep2):  # столкновение с правым человеком
            self.flag1 = False
            self.flag2 = True
            self.fl = False
            self.spflag1 = False
            self.spflag2 = False
            self.diff = self.rect.x
            self.y = self.rect.y
            """учитывает верхнюю и нижнюю подачю"""
            if self.pep2.File_name == 'high2.png':
                self.spflag3 = True
            elif self.pep2.File_name == 'low2.png':
                self.spflag4 = True

        elif pygame.sprite.collide_mask(self, self.ground):  # столкновение с землей
            self.flag1 = False
            self.flag2 = False
            self.fl = False
            self.flag3 = True

        elif pygame.sprite.collide_mask(self, self.net):  # столкновение с сеткой
            self.fl = False
            self.flag1 = False
            self.flag2 = False
            self.flag4 = True

        if self.fl:
            self.rect.y += self.STEP

        elif self.flag1:
            if self.spflag1:
                x = self.rect.x - self.diff - 260
                y = int(((1 / 150) * x ** 2) - 450)
                self.rect.y = self.y + y
                self.STEP = 4
            elif self.spflag2:
                x = self.rect.x - self.diff - 442
                y = int(((1 / 650) * x ** 2) - 300)
                self.rect.y = self.y + y
                self.STEP = 7
            self.rect.x += self.STEP

        elif self.flag2:
            if self.spflag3:
                x = self.rect.x - self.diff + 260
                y = int(((1 / 150) * x ** 2) - 450)
                self.rect.y = self.y + y
                self.STEP = -4
            elif self.spflag4:
                x = self.rect.x - self.diff + 442
                y = int(((1 / 650) * x ** 2) - 300)
                self.rect.y = self.y + y
                self.STEP = -7
            self.rect.x += self.STEP

        elif self.flag3:
            if self.rect.x < 750:
                self.goals[1] += 1
            else:
                self.goals[0] += 1
            self.flag3 = False
            new_round(self.pep1, self.pep2)
            self.STEP = 5
            self.fl = False
            self.flag1 = False
            self.flag2 = False
            self.flag3 = False
            self.flag4 = False
            self.spflag1 = False
            self.spflag2 = False
            self.spflag3 = False
            self.spflag4 = False
            self.rect.x = random.choice([100, 1000, 500, 1300])
            self.rect.y = 200


        elif self.flag4:
            if self.rect.x < 750:
                self.goals[1] += 1
            else:
                self.goals[0] += 1
            self.flag4 = False
            self.spflag = True
            new_round(self.pep1, self.pep2)
            self.STEP = 5
            self.fl = False
            self.flag1 = False
            self.flag2 = False
            self.flag3 = False
            self.flag4 = False
            self.spflag1 = False
            self.spflag2 = False
            self.spflag3 = False
            self.spflag4 = False
            self.rect.x = random.choice([100, 1000, 500, 1300])
            self.rect.y = 200
