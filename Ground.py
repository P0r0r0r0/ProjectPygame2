import pygame


class Ground(pygame.sprite.Sprite):  # спрайт земли

    """
    аргументы:
    group - pygame.sprite.Group
     """
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.Surface([2000, 50])
        self.image.fill(pygame.Color(150, 100, 50))

        self.rect = self.image.get_rect()
        self.rect.x = -250
        self.rect.y = 750
