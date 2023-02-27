import pygame


class Net(pygame.sprite.Sprite):  # спрайт сетки
    """аргументы:
         group - pygame.sprite.Group
         """
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.Surface([20, 400])
        self.image.fill(pygame.Color(255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.x = 740
        self.rect.y = 350
        self.mask = pygame.mask.from_surface(self.image)
