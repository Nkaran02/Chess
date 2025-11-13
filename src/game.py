import pygame
from const import *

class Game:

    def __init__(self):
        pass

    #show  method 
    def show_background(self, surface):
        #inside this we are going to draw the board and it will reference to self.screen in main.py
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #light green 
                else:
                    color = (119, 154, 88)  #dark green

                rect = (col * SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

                pygame.draw.rect(surface , color, rect)
                