# Game类
import pygame

from Board import Board


class Game:
    def __init__(self, screen_width):
        self.screen_width = screen_width
        self.screen_height = screen_width * 1.3
        self.game_over = False

        # 初始化 Pygame
        pygame.init()

        self.board = Board(self.screen_width)
        self.game_over = False
        self.game_failed = False
        # 创建 Pygame 窗口
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("2048")

        # 设置游戏时钟
        self.clock = pygame.time.Clock()

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_over = True
                    elif event.key == pygame.K_UP:
                        if not self.board.cells_check:
                            self.board.move('up')
                    elif event.key == pygame.K_DOWN:
                        if not self.board.cells_check:
                            self.board.move('down')
                    elif event.key == pygame.K_LEFT:
                        if not self.board.cells_check:
                            self.board.move('left')
                    elif event.key == pygame.K_RIGHT:
                        if not self.board.cells_check:
                            self.board.move('right')
                    elif event.key == pygame.K_r:
                        self.board.new_game()

            self.screen.fill((255, 255, 255))
            self.board.draw(self.screen)
            if self.board.cells_check:
                self.board.draw_tip(self.screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_over = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.game_over = True
                        elif event.key == pygame.K_r:
                            self.board.new_game()
                        else:
                            continue
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
