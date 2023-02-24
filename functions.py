import os
import sys
import pygame
from GameBoard import Level
from Instructions import Instruction


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
