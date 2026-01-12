import pygame

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self, screen):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #0 = left button
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0: #if you release the button it resets (and you can click it again)
            self.clicked = False


        #draw button
        screen.blit(self.image, self.rect)

        return action