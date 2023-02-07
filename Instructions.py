import pygame


class Instruction:
    def __init__(self):
        game_size = width, height = 1000, 800
        self.screen = pygame.display.set_mode(game_size)
        self.screen.fill(pygame.Color(50, 50, 50))
        intro_text = ["Управление", "",
                      "Правила игры",
                      "Если в правилах несколько строк,",
                      "приходится выводить их построчно"]

        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)
