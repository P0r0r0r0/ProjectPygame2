import pygame
from functions import load_image

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    running = True
    group = pygame.sprite.Group()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(pygame.Color(250, 170, 80))
        group.draw(screen)
        group.update(event)

        pygame.display.flip()
        clock.tick(15)

    pygame.quit()
