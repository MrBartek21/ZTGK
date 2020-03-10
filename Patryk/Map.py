import pygame, sys, ctypes
from pygame import Vector2

class Level1(object):
    def __init__(self,game):
        #Get variable from class Game
        self.Game = game
        #Inicialization
        self.bit_map()
        
        

    def bit_map(self):
        self.Bit = [[1,0,1,0,1,0,1,0,1,0,1,0,],[0,1,0,1,0,1,0,1,0,1,0,1,],[1,0,1,0,1,0,1,0,1,0,1,0,],[0,1,0,1,0,1,0,1,0,1,0,1,]]
        
        
    def draw(self):
        
        y=0
        for i in range(len(self.Bit)):
            x=0
            for z in range(len(self.Bit[i])):
                   
                if self.Bit[i][z] == 1 :
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 0)
                
                self.box = pygame.Rect(x, y, 32, 32)
                pygame.draw.rect(self.Game.screen, color, self.box)
                x+=32
            print(x)
            print(y)
            y+=32
                











