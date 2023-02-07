import pygame
from functions import load_image
from functions import myFunction
from functions import openInstruction
from PlayBut import PlayBut
from GameBoard import Level

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    objects = []
    sp = []

    running = True
    group = pygame.sprite.Group()
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

        group.draw(screen)
        group.update(event)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
