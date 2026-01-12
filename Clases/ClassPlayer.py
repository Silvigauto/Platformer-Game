import pygame

class Player():
    def __init__(self,x,y):
        self.reset(x,y) 
    
    def update(self,screen, world, ghost_group, lava_group, game_over):
        screen_height = screen.get_height() #get the height of the screen through the parameters
        dx = 0
        dy = 0
        walk_cooldown = 10 #for the animation to go slower

        if game_over == 0:

            #move the player(calculate the future position and the move it)
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False: #to avoid double jumping
                self.vel_y =-20
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key [pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if  key [pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            #animations
            if self.counter > walk_cooldown: #to control the speed of the animation
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]
                

            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y 

            #check for collision
            self.in_air = True
            for tile in world.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in y direction (he can still move in x direction)
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground, when he is jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    #check if above the ground, when he is falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            #check for collision with enemies
            if pygame.sprite.spritecollide(self, ghost_group, False):
                game_over = -1
            
            #check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
                print(game_over)


            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

            # if self.rect.bottom > screen_height:
            #     self.rect.bottom = screen_height 
            #     dy = 0

        elif game_over == -1:   
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5
        
        #draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)
        
        return game_over

    def reset(self,x,y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1,5):
            img_right = pygame.image.load(f'Recursos\player\guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40,80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_left.append(img_left)
            self.images_right.append(img_right)
        dead_image = pygame.image.load('Recursos\player\guy_dead.png')
        self.dead_image = pygame.transform.scale(dead_image, (40,80))
        self.image = self.images_right[self.index] #i choose a default img from the list (i'll change later)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y= y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.vel_y = 0
        self.jumped = False #to avoid infinite jumping
        self.direction = 0 #to flip the images if his is facing right or left
        self.in_air = 0