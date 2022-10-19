from mimetypes import init
from pickle import TRUE
from turtle import width
import pygame
import math
from queue import PriorityQueue
# pygame.init()
width=800
WIN= pygame.display.set_mode((width,width))
pygame.display.set_caption("A* Path Finding Algorithm")

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
PURPULE=(128,0,128)
ORANGE=(265,165,0)
GREY=(128,128,128)
TURQUOISE=(64,224,208)


class spot:
    def __init__(self,row,col,width,total_rows):
        self.row=row
        self.col=col
        self.x=row*width
        self.y=col*width
        self.color=WHITE
        self.total_rows=total_rows
    
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color==RED

    def is_open(self):
        return self.color ==GREEN
    
    def is_barrier(self):
        return self.color==BLACK
    
    def is_start(self):
        return self.color==ORANGE
    
    def is_end(self):
        return self.color==TURQUOISE
    
    def reset(self):
        return self.color==WHITE
    
    def make_closed(self):
        self.color=RED
    
    def make_open(self):
        self.color=GREEN
    
    def make_barrier(self):
        self.color=BLACK
    
    def make_end(self):
        self.color=TURQUOISE
    
    def make_path(self):
        self.color=PURPULE
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
        
    
    def update_neighbors(self,grid):
        pass

    def __lt__(self,other):
        return False








game_over=False
while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    
    
    
    # spot.draw(self,win)
    pygame.display.update()