import pygame
import sys

from const import *
from game import Game

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess Application")
        self.game = Game()

    def mainloop(self):
        
        screen = self.screen
        game = self.game

        while True:
            
            self.game.show_background(screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

main = Main()
main.mainloop()
