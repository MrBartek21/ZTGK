import pygame, sys, ctypes
from pygame import Vector2
import random
class Level1(object):
    def __init__(self,game):
        #Get variable from class Game
        self.Game = game
        #Inicialization
        self.bit_map()
        
        

    def bit_map(self):
        
        
        self.Bit=[[1,0,2,0,1,0,2,0,1,2,2,1,0,2,1,0,2,0,1,2],[2,3,1,3,0,1,0,1,0,3,1,0,2,2,1,0,2,0,1,2],
                [1,0,2,0,1,0,2,0,1,2,2,1,0,2,1,0,2,0,1,2],[2,3,1,3,0,1,0,1,0,3,1,0,2,2,1,0,2,0,1,2]]
            
        
        
    def draw(self):
        
        y=0
        for i in range(len(self.Bit)):
            x=0
            for z in range(len(self.Bit[i])):
                   
                if self.Bit[i][z] == 1 :
                    color = (0, 255, 0)
                elif self.Bit[i][z] == 2:
                    color = (255, 0, 0)
                elif self.Bit[i][z] == 3:
                    color = (0, 0, 255)
                else:
                    color = (0, 0, 0)
                
                self.box = pygame.Rect(x, y, 64, 64)
                pygame.draw.rect(self.Game.screen, color, self.box)
                x+=64
            y+=64
                










