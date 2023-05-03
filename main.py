# 运行程序
import pygame
from Game import Game

if __name__ == '__main__':
    pygame.init()
    game = Game(400)
    game.run()  # run
