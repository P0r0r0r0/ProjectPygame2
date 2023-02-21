import pygame
from functions import load_image
from myFunction  import myFunction
from PlayBut import PlayBut
from GameBoard import Level

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    objects = []
    level = False

    running = True
    group = pygame.sprite.Group()
    PlayBut(30, 30, 400, 100, screen, objects, 'Button One (onePress)', myFunction)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if not level:
                screen.fill(pygame.Color(250, 170, 80))
                level = True
            for object in objects:
                object.process()

        group.draw(screen)
        group.update(event)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
