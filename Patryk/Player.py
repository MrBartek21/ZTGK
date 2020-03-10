import pygame, sys, ctypes
from pygame import Vector2

class Player_Move(object):
    def __init__(self,game):
        #Get variable from class Game
        self.Game = game
        #Inicialization
        self.Player_pos = Vector2(10,(self.Game.ScreenHeight-100))
        self.gravity = 1
        self.sprint = 1

    def tick(self):
        
        # Input
        keys = pygame.key.get_pressed()
        # Sprint
        if keys[pygame.K_LSHIFT]:
            if self.sprint<2:
                    self.sprint *=1.1
        else:
            self.sprint = 1
        # Right and left
        if self.Player_pos.x>10:
            if keys[pygame.K_LEFT]:
                print(self.sprint) 
                self.Player_pos.x -= 5*self.sprint  
        if keys[pygame.K_RIGHT]:
            self.Player_pos.x += 5*self.sprint 
        #Jump
        if self.Player_pos.y<=self.Game.ScreenHeight-100:
            if keys[pygame.K_UP]:
                self.Player_pos.y -= 10
                self.gravity*=1.1
            elif keys[pygame.K_SPACE]:
                self.Player_pos.y -= 10
                self.gravity*=1.1
        #Gravitacion        
        if self.Player_pos.y<self.Game.ScreenHeight-100:        

            self.Player_pos.y += self.gravity
            #Floor
            if self.Player_pos.y>self.Game.ScreenHeight-100:
                
               self.Player_pos.y = self.Game.ScreenHeight-100
               self.gravity=1
        
                
            

    def draw(self):
        #Spawn Player
        self.box = pygame.Rect(self.Player_pos.x, self.Player_pos.y, 30, 50)
        pygame.draw.rect(self.Game.screen, (0, 0, 0, 0), self.box)
        











