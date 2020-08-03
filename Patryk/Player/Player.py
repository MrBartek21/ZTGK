import pygame, sys, ctypes
from pygame import Vector2

class Player_Move(object):
    def __init__(self,game):
        #Get variable from class Game
        self.Game = game
        self.Chempion()
        #Inicialization
        self.Player_pos = Vector2(10,128)
        self.gravity = self.weight*0.01
        self.sprint = 1
        
    def tick(self):
        #Actualy Bit
        self.Row =int(self.Player_pos.y/64)
        self.Col =int(self.Player_pos.x/64)
        
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
                 
                self.Player_pos.x -= self.speed*self.sprint  
        if keys[pygame.K_RIGHT]:
            self.Player_pos.x += self.speed*self.sprint 
        #Jump
            
        if self.Player_pos.y<=(self.Row+2)*64:
            if keys[pygame.K_UP]:
                self.Player_pos.y -= 10
                self.gravity*=1.1
                
           
            
        #Gravitacion        
               

        self.Player_pos.y += self.gravity
            #Floor
        if self.Game.Map.Bit[self.Row+2][self.Col]==1:
            
                    
            self.Player_pos.y = (self.Row)*64
            self.gravity=self.weight*0.01
            
                
            

    def draw(self):
        #Spawn Player
        self.box = pygame.Rect(self.Player_pos.x, self.Player_pos.y, 64, 128)
        pygame.draw.rect(self.Game.screen, (255, 0, 0, 0), self.box)
        

    def Chempion(self):
        #---------------------------------------------------------------
# potrzebuje abyyś tu pobierał jaka klasa postaci i pobierał jej te 6 danych
        #---------------------------------------------------------------
        #get json information
        self.speed = 8
        self.damage = 0
        self.atack_speed = 0
        self.range = 0
        self.weight = 60
        self.armor = 0
        
        
        
        
    










