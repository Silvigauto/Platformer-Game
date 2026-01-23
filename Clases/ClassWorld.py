import pygame
from Clases.ClassEnemy import Enemy
from Clases.ClassLava import Lava
from Clases.ClassExit import Exit
from Clases.ClassCoin import Coin



class World():
    def __init__(self, data, tile_size, ghost_group,lava_group,exit_group,coin_group, screen):
        self.tile_list = []
        #load images
        tile_img = pygame.image.load('Recursos\darker_tile.png')
        stone_img = pygame.image.load('Recursos\stone.png')
        lava_img = pygame.image.load('Recursos\lava.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1: #piedra violeta
                    img = pygame.transform.scale(tile_img, (tile_size,tile_size))
                    #convertimos en un rectangulo para poder usar sus atributos, coordenadas colisiones
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2: #piedra gris
                    img = pygame.transform.scale(stone_img, (tile_size,tile_size))
                    #convertimos en un rectangulo para poder usar sus atributos, coordenadas colisiones
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3: #lava
                    lava = Lava(col_count * tile_size, row_count * tile_size  + (tile_size // 2), tile_size )
                    lava_group.add(lava)

                if tile == 4: #enemigo
                    ghost = Enemy(col_count * tile_size, row_count * tile_size + 50) #+50 so it can be on top of the tile 
                    ghost_group.add(ghost)
                if tile == 5: #salida
                    exit = Exit(col_count * tile_size,  row_count * tile_size, tile_size)
                    exit_group.add(exit)
                if tile == 6: #moneda
                    coin = Coin(col_count * tile_size + (tile_size //2 ), row_count * tile_size  + (tile_size // 2), tile_size )
                    coin_group.add(coin)
                col_count += 1
            row_count += 1

            
    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255,255,255), tile[1], 2)
