import pygame
from Clases.ClassBullet import Bullet

class Player():
    def __init__(self,x,y):
        self.reset(x,y) 

    def update(self,screen, world, ghost_group, lava_group,exit_group,bullet_group, game_over):
        current_time = pygame.time.get_ticks()

        if game_over == 0:
            self.move_player(current_time, bullet_group)
            self.animate()
            self.apply_gravity()
            self.check_vulnerability(current_time)
            self.check_collisions(world)
            game_over = self.check_collisions_with_groups(ghost_group, lava_group, exit_group, game_over)
            self.update_position()

        elif game_over == -1:
            self.die()

        self.draw(screen)

        return game_over


    def move_player(self, current_time, bullet_group):
        #move the player(calculate the future position and the move it)
        dx = 0   
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
        if key[pygame.K_f]:
            if current_time - self.last_shot_time >= self.shoot_cooldown:
                self.shoot(bullet_group)
                self.last_shot_time = current_time

        self.dx = dx
    
    def animate(self):
        walk_cooldown = 10 #for the animation to go slower
        if self.counter > walk_cooldown: #to control the speed of the animation
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]
    
    def apply_gravity(self):
        self.dy = 0
        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.dy += self.vel_y 
    
    def check_vulnerability(self, current_time):
        #check for invulnerability
            if self.invulnerable:
                if current_time - self.last_hit_time >= self.hit_cooldown:
                    self.invulnerable = False
    
    def check_collisions(self, world):
        #check for collision
        self.in_air = True
        for tile in world.tile_list:
            #check for collision in x direction
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            #check for collision in y direction (he can still move in x direction)
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                #check if below the ground, when he is jumping
                if self.vel_y < 0:
                    self.dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                #check if above the ground, when he is falling
                elif self.vel_y >= 0:
                    self.dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = False


    def check_collisions_with_groups(self, ghost_group,lava_group, exit_group, game_over):
        current_time = pygame.time.get_ticks()
        #check for collision with enemies
        if pygame.sprite.spritecollide(self, ghost_group, False):
            if not self.invulnerable:
                self.lives -= 1
                self.invulnerable = True
                self.last_hit_time = current_time

                if self.lives <= 0:
                    game_over = -1

        #check for collision with lava
        if pygame.sprite.spritecollide(self, lava_group, False):
            game_over = -1
            self.lives = 0
        
        #check for collision with exit
        if pygame.sprite.spritecollide(self, exit_group, False):
            game_over = 1
            
        
        return game_over

    def shoot(self, bullet_group):
        direction =  self.direction if self.direction != 0 else 1
        bullet = Bullet(self.rect.centerx, self.rect.centery,direction)
        bullet_group.add(bullet)

    def update_position(self): 
        self.rect.x += self.dx
        self.rect.y += self.dy

    def die(self):
        self.image = self.dead_image
        if self.rect.y > -80:
            self.rect.y -= 5
    
    def draw(self, screen): 
        #draw player onto screen
        if self.invulnerable:
            self.image.set_alpha(120)  # transparent
        else:
            self.image.set_alpha(255)  # normal

        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)
    
    

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

        #jumping attributes
        self.vel_y = 0
        self.jumped = False #to avoid infinite jumping
        self.in_air = 0
        self.direction = 0 #to flip the images if his is facing right or left

        #shooting atributes
        self.shoot_cooldown = 300 #miliseconds 
        self.last_shot_time = 0

        #lives attributes
        self.lives = 3 
        self.invulnerable = False
        self.last_hit_time = 0
        self.hit_cooldown = 1000 #1 sec = 1000ms
    
    
