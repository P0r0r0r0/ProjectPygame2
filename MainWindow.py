import pygame
from functions import load_image
from functions import myFunction
from functions import openInstruction
from PlayBut import PlayBut
from GameBoard import Level
from people import people_1
from Ball import Ball
from Ground import Ground
from Net import Net
from people2 import people_2
from stenki import Border

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    objects = []
    sp = []

    running = True
    group = pygame.sprite.Group()
    borders = pygame.sprite.Group()
    clock = pygame.time.Clock()
    ground = Ground(group)
    net = Net(group)
    bord1 = Border(borders, 1, 1, 1, 750)
    bord2 = Border(borders, 1499, 1, 1499, 750)
    pep1 = people_1(group, 60, 470, bord1, net)
    pep2 = people_2(group, 1100, 470, bord2, net)
    ball = Ball(group, 500, 500, net, ground, pep1, pep2)

    PlayBut(30, 30, 400, 100, screen, objects, sp, 'Play', myFunction)
    PlayBut(30, 150, 400, 100, screen, objects, sp, 'Instruction', openInstruction)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if not sp:
                screen.fill(pygame.Color(250, 170, 80))

            for object in objects:
                if not sp:
                    object.process()
        if 'Play' in sp:
            screen.fill(pygame.Color(150, 255, 150))
            group.update(event)
            group.draw(screen)
            borders.update(event)
            borders.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
