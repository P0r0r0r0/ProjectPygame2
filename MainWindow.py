import pygame
from functions import myFunction
from functions import openInstruction
from PlayBut import PlayBut
from people import people_1
from Ball import Ball
from Ground import Ground
from Net import Net
from people2 import people_2
from stenki import Border
import random
from functions import return_home
from functions import new_game

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    objects = []
    home = []
    game_over = []
    sp = []
    goals = [0, 0]

    running = True
    group = pygame.sprite.Group()
    borders = pygame.sprite.Group()
    ground = Ground(group)
    net = Net(group)
    bord1 = Border(borders, 1, 1, 1, 750)
    bord2 = Border(borders, 1499, 1, 1499, 750)
    pep1 = people_1(group, 60, 470, bord1, net)
    pep2 = people_2(group, 1100, 470, bord2, net)
    ball = Ball(group, random.choice([100, 1000, 500, 1300]), 200, goals, net, ground, pep1, pep2)
    PlayBut(30, 30, 200, 50, screen, home, sp, 'Home', return_home)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if not sp:
                screen.fill(pygame.Color(250, 170, 80))
                PlayBut(270, 200, 400, 100, screen, objects, sp, 'Play', myFunction)
                PlayBut(270, 330, 400, 100, screen, objects, sp, 'Instruction', openInstruction)
            for object in objects:
                if not sp:
                    object.process()
        if 'Home' in sp or 'Return Home' in sp:
            sp.clear()
            goals[0] = 0
            goals[1] = 0
            new_game(pep1, pep2, ball)

        if 'Play' in sp:
            screen.fill(pygame.Color(100, 200, 100))
            font = pygame.font.Font(None, 150)
            text = f'{goals[0]}:{goals[1]}'
            string_rendered = font.render(text, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 50
            intro_rect.x = 670
            screen.blit(string_rendered, intro_rect)
            group.update(event)
            group.draw(screen)
            borders.update(event)
            borders.draw(screen)
            home[0].process()
        if 'Instruction' in sp:
            home[0].process()

        if goals[0] == 5 or goals[1] == 5:
            screen.fill(pygame.Color(200, 200, 100))
            font = pygame.font.Font(None, 100)
            if goals[0] == 5:
                text = 'left won'
            else:
                text = 'right won'
            string_rendered = font.render(text, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 200
            intro_rect.x = 500
            screen.blit(string_rendered, intro_rect)
            PlayBut(450, 300, 500, 200, screen, game_over, sp, 'Return Home', return_home)
            game_over[0].process()

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
