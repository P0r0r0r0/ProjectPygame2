import sys
import os
import pygame
from GameBoard import Level
from Instructions import Instruction


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def myFunction():
    Level()

def openInstruction():
    Instruction()