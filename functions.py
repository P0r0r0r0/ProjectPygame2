import os
import sys
import pygame
from GameBoard import Level
from Instructions import Instruction
import random


def load_image(name):  # функция для загрузки картинок
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def myFunction():  # функция для открытия поля для игры
    Level()


def openInstruction():  # функция для открытия инструкции
    Instruction()


def new_round(pep1, pep2):
    pep1.rect.x = 60
    pep1.rect.y = 470
    pep2.rect.x = 1100
    pep2.rect.y = 470


def return_home():
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(250, 170, 80))


def new_game(pep1, pep2, ball):
    pep1.rect.x = 60
    pep1.rect.y = 470
    pep2.rect.x = 1100
    pep2.rect.y = 470
    ball.STEP = 5
    ball.fl = False
    ball.flag1 = False
    ball.flag2 = False
    ball.flag3 = False
    ball.flag4 = False
    ball.spflag1 = False
    ball.spflag2 = False
    ball.spflag3 = False
    ball.spflag4 = False
    ball.rect.x = random.choice([100, 1000, 500, 1300])
    ball.rect.y = 200
