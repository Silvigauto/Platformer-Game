import pygame

class HUD:
    def __init__(self, screen):
        self.screen = screen
        self.heart_img = pygame.image.load("Recursos\heart.png")
        self.heart_img = pygame.transform.scale(self.heart_img, (30, 30))

    def draw(self, player):
        for i in range(player.lives):
            self.screen.blit(self.heart_img, (20 + i * 35, 20))
