import pygame
from pygame.locals import * 
from Clases.ClassWorld import World
from Clases.ClassPlayer import Player
from Clases.ClassLava import Lava
from Clases.ClassButton import Button

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
tile_size = 100
game_over = 0 
main_menu = True



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

restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)


run = True
while run:
    clock.tick(fps)
    screen.blit(background_image, (0,0))

    if main_menu:
        if exit_button.draw(screen):
            run = False
        if start_button.draw(screen):
            main_menu = False
    else:
        #game logic
        world.draw(screen)

        if game_over == 0:
            ghost_group.update() #when go is -1 it stops moving

        ghost_group.draw(screen) #but it doesnt stop showing
        lava_group.draw(screen)

        for ghost in ghost_group:
            pygame.draw.rect(screen, (255,255,255), ghost.rect, 2) #draw it here so it stays showing

        game_over =  player.update(screen, world, ghost_group, lava_group, game_over)

        #if player has died
        if game_over == -1:
            if restart_button.draw(screen):
                player.reset(100, screen_height - 180)
                game_over = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()