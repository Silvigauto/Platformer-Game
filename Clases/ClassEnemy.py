import pygame

class Enemy(pygame.sprite.Sprite): #draw and update already there
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self) #super().__init__()
        self.image = pygame.image.load('Recursos/ghost.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
    
    def update(self): #overwrite the method
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
    