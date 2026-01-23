import pygame
from pygame.locals import * 
from Clases.ClassWorld import World
from Clases.ClassPlayer import Player
from Clases.ClassLava import Lava
#from Clases.ClassCoin import Coin
from Clases.ClassButton import Button
import json #para el manejo de los niveles
from os import path #to handle non existing game levels

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
restart_img = pygame.image.load('Recursos\\buttons\\restart_btn.png')
start_img = pygame.image.load('Recursos\\buttons\\start_btn.png')
exit_img = pygame.image.load('Recursos\\buttons\\exit_btn.png')


#define game variables
tile_size = 50
game_over = 0 
main_menu = True
level = 1
max_levels = 3
score = 0




#15 x 8
# world_data = [
#     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,0,0,0,0,4,0,0,0,1],
#     [1,1,0,0,1,0,0,0,1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,0,4,0,0,0,0,0,0,1],
#     [1,1,1,1,1,1,1,1,1,0,1,0,0,0,1],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
#     [1,0,0,0,0,0,0,0,0,4,0,0,1,1,1],
#     [1,1,1,1,3,3,3,3,1,1,1,1,1,1,1],

# ]

#replace the string with the current level variable
if path.exists(f'Levels\level{level}.json'):
    with open(f'Levels\level{level}.json', 'r') as file:
        world_data = json.load(file)

#GROUPS
ghost_group = pygame.sprite.Group() # TODO sumar los groups a una lista y luego cambiar los parametros
lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()


#creating the instances
world = World(world_data, tile_size, ghost_group,lava_group,exit_group,coin_group,screen)
player = Player(100, screen_height - 400)

restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)

def reset_level(level):
    player.reset(100, screen_height - 400) #reset the player
    ghost_group.empty()
    lava_group.empty()
    exit_group.empty()
    if path.exists(f'Levels\level{level}.json'):
        with open(f'Levels\level{level}.json', 'r') as file:
            world_data = json.load(file)
    world = World(world_data, tile_size, ghost_group,lava_group,exit_group,coin_group,screen)
    return world


run = True
while run:
    clock.tick(fps)
    screen.blit(background_image, (0,0))

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if main_menu:
        if exit_button.draw(screen):
            run = False
        if start_button.draw(screen):
            main_menu = False

    else:
        # update(solo logica)

        if game_over == 0:
            ghost_group.update()
            bullet_group.update()
            game_over =  player.update(screen, world, ghost_group, lava_group,exit_group,bullet_group, game_over)

        #colisions (always)

        bullet_hits = pygame.sprite.groupcollide(ghost_group,bullet_group,True,True)

        #draws
        world.draw(screen)

        ghost_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)
        bullet_group.draw(screen)

        for ghost in ghost_group:
            pygame.draw.rect(screen, (255,255,255), ghost.rect, 2)

        # game_over: WIN
        if game_over == -1:
            if restart_button.draw(screen):
                world_data = []
                world = reset_level(level)
                game_over = 0

        elif game_over == 1:
            level += 1
            if level <= max_levels:
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                if restart_button.draw(screen):
                    level = 1
                    world_data = []
                    world = reset_level(level)
                    game_over = 0

    pygame.display.update()


pygame.quit()