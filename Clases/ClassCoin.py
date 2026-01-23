import pygame

# TODO agregar animacion a las monedas (flotantes)
class Coin(pygame.sprite.Sprite): #draw and update already there
    def __init__ (self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self) #super().__init__()
        img = pygame.image.load('Recursos\coin.png')
        self.image = pygame.transform.scale(img, (tile_size//2, tile_size//2))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y ) #midpoint instead of the top left corner

        