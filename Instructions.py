import pygame


class Instruction:
    def __init__(self):
        game_size = width, height = 1000, 800
        self.screen = pygame.display.set_mode(game_size)
        self.screen.fill(pygame.Color(50, 50, 50))
        center_column = ["Управление",
                         "",
                         "",
                         "Движение влево",
                         "Движение вправо",
                         "Нижняя стойка",
                         "Верхняя стойка"]

        left_column = ["",
                       "Левый игрок",
                       "",
                       "A",
                       "D",
                       "S",
                       "W"]

        right_column = ["",
                        "Правый игрок",
                        "",
                        "<-",
                        "->",
                        "v",
                        "^"]
        font = pygame.font.Font(None, 50)
        text_coord = 70
        for line in left_column:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 40
            intro_rect.top = text_coord
            intro_rect.x = 50
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        text_coord = 70
        for line2 in center_column:
            string_rendered = font.render(line2, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 40
            intro_rect.top = text_coord
            intro_rect.x = 350
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        text_coord = 70
        for line3 in right_column:
            string_rendered = font.render(line3, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 40
            intro_rect.top = text_coord
            intro_rect.x = 700
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        string_rendered = font.render("|", 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 470
        intro_rect.x = 705
        self.screen.blit(string_rendered, intro_rect)

        string_rendered = font.render("|", 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 560
        intro_rect.x = 705
        self.screen.blit(string_rendered, intro_rect)
