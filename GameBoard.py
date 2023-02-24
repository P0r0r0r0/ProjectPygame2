import pygame


class Level:
    def __init__(self):  # настройка основного окна игры
        game_size = width, height = 1500, 800
        self.game_screen = pygame.display.set_mode(game_size)
        # self.game_screen.fill(pygame.Color(150, 255, 150))

#
#
# size = width, height = 500, 500
# screen = pygame.display.set_mode(size)
#
# group = pygame.sprite.Group()
# running = True
# clock = pygame.time.Clock()

# people_1(group, 0, 0)
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 running = False
#
#     screen.fill(pygame.Color(255, 255, 255))
#     group.draw(screen)
#     group.update(event)
#
#     pygame.display.flip()
#
#     clock.tick(15)
#
#
# pygame.quit()
