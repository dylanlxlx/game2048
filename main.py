import pygame
from Game import Game

if __name__ == '__main__':
    pygame.init()
    game = Game(600, 600)
    game.run()
