import pygame

from functions import load_image


class Ball(pygame.sprite.Sprite):
    File_name = 'voleyball_ball.png'
    STEP = 10

    def __init__(self, group, x_coord, y_coord):
        super().__init__(group)

        self.image = load_image(self.File_name)
        self.image = pygame.transform.scale(self.image, (400, 400))

        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_LEFT:
                self.rect.x -= self.STEP
            elif args[0].key == pygame.K_RIGHT:
                self.rect.x += self.STEP
            elif args[0].key == pygame.K_UP:
                self.rect.y -= self.STEP
            elif args[0].key == pygame.K_DOWN:
                self.rect.y += self.STEP
