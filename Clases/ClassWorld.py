import pygame

class World():
    def __init__(self, data, tile_size):
        self.tile_list = []
        #load images
        tile_img = pygame.image.load('Recursos\darker_tile.png')
        stone_img = pygame.image.load('Recursos\stone.png')
        lava_img = pygame.image.load('Recursos\lava.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(tile_img, (tile_size,tile_size))
                    #convertimos en un rectangulo para poder usar sus atributos, coordenadas colisiones
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(stone_img, (tile_size,tile_size))
                    #convertimos en un rectangulo para poder usar sus atributos, coordenadas colisiones
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(lava_img, (tile_size,tile_size))
                    #convertimos en un rectangulo para poder usar sus atributos, coordenadas colisiones
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255,255,255), tile[1], 2)
