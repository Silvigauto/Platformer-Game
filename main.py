import pygame
from pygame.locals import * 
from Clases.ClassWorld import World
from Clases.ClassPlayer import Player
from Clases.ClassLava import Lava

pygame.init()

clock = pygame.time.Clock() #add for animaiton
fps = 60

screen_width = 1500
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#load images
background_image = pygame.image.load("Recursos\\fondo2.jpg")
background_image = pygame.transform.smoothscale(background_image, (screen_width, screen_height))

#define game variables
tile_size = 100
game_over = 0 



#15 x 8
world_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,4,0,0,0,1],
    [1,1,0,0,1,0,0,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,4,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,4,0,0,1,1,1],
    [1,1,1,1,3,3,3,3,1,1,1,1,1,1,1],

]

#creating the instances

ghost_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
world = World(world_data, tile_size, ghost_group,lava_group,screen)
player = Player(100, screen_height - 180)


run = True
while run:
    clock.tick(fps)
    screen.blit(background_image, (0,0))

    world.draw(screen)

    if game_over == 0:
        ghost_group.update()
        
    ghost_group.draw(screen)

    lava_group.draw(screen)

    for ghost in ghost_group:
        pygame.draw.rect(screen, (255,255,255), ghost.rect, 2) #draw it here so it stays showing

    game_over =  player.update(screen, world, ghost_group, lava_group, game_over)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()