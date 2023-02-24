import pygame


class Net(pygame.sprite.Sprite):  # спрайт сетки

    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.Surface([20, 400])
        self.image.fill(pygame.Color(255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.x = 740
        self.rect.y = 350
