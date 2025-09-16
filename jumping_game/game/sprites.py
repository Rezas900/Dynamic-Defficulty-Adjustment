
import pygame
from .config import *
import random


#defines the player class and its properties

class Player:

    def __init__(self):
        self.rect = pygame.Rect(PLAYER_START_X, PLAYER_START_Y, 50, 50)
        self.velocity_y = 0
        self.on_ground = True
        self.jump_made = 0

    def jump(self):
        if self.jump_made < 2:
            if self.on_ground:
                self.velocity_y = JUMP_STRENGTH
                self.on_ground = False
                self.jump_made += 1
            else:
                self.velocity_y += JUMP_STRENGTH * 0.6
                self.jump_made +=1

    def dive(self):
        if not self.on_ground:
            self.velocity_y += DIVE_STRENGTH


    def apply_gravity(self):
        self.rect.y += self.velocity_y
        self.velocity_y += GRAVITY

        #check ifit has hit the ground
        ground_level = 450  
        if self.rect.bottom >= ground_level + 50:
            self.rect.bottom = ground_level + 50
            self.velocity_y = 0
            self.on_ground = True
            self.jump_made = 0

    def update(self):
        self.apply_gravity()

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

    def reset(self):
        #returns the player to the starting point
        self.rect.x = PLAYER_START_X
        self.rect.y = PLAYER_START_Y
        self.velocity_y = 0
        self.on_ground = True
        self.jump_made = 0

#A class for abstacle managment :

class Obstacle:

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        # self.speed = OBSTACLE_SPEED

    def update(self, current_speed):
        self.rect.x -= current_speed
        # if abstacle leaves the screen, we move it to the right side of screen
        if self.rect.right < 0:
            width = random.randint(20, 50)
            height = random.randint(30, 80)
            self.rect = pygame.Rect(SCREEN_WIDTH + random.randint(100, 300),
                                    500 - height, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)

    def reset(self):
        #returns the obstacle to the starting point
        self.rect.left = SCREEN_WIDTH + random.randint(50, 200)
