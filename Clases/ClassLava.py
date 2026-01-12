import pygame

class Lava(pygame.sprite.Sprite): #draw and update already there
    def __init__ (self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self) #super().__init__()
        img = pygame.image.load('Recursos\lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size//2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        