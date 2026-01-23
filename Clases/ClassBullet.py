import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.image.load('Recursos\\bullet.png') #TODO poder pasar una imagen por parametro, abstraer mas
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 10
        self.direction = direction #1 right -1 left

    def update(self):
        self.rect.x += self.speed * self.direction

        #delete if it goes out of the window game
        if self.rect.right < 0 or self.rect.left > 1500:
            self.kill()
