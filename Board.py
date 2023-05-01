# Board类
import random

import pygame

from Block import Block
from text_wrap import draw_text


class Board:
    def __init__(self, screen_w, screen_h):
        self.cells_check = False  # 所有block是否均被填满
        self.screen_w = screen_w  # 窗口宽度
        self.screen_h = screen_h  # 窗口高度
        self.rows = self.cols = 4  # block行列个数
        self.cells = [[0] * self.cols for _ in range(self.rows)]
        self.block_size = (min(self.screen_w, self.screen_h) / self.rows)
        self.block_margin = (min(self.screen_w, self.screen_h) / self.rows) * 0.1

        self.font_size = self.screen_w // self.rows // 3  # 字体大小
        self.font_name = 'Algerian'  # 字体
        self.text_color = (0, 0, 0)  # 字体颜色(黑色)
        # 初始化棋盘，生成两个随机位置的方块
        self.add_block()
        self.add_block()

    def new_game(self):
        self.cells_check = False
        self.cells = [[0] * self.cols for _ in range(self.rows)]
        self.add_block()
        self.add_block()

    def add_block(self):
        # 生成一个新方块，数值为2或4
        random_val = random.choice([2, 4])
        empty_pos = self.get_random_empty_cell()
        if empty_pos is not None:
            row, col = empty_pos
            self.cells[row][col] = random_val
        else:
            self.cells_check = True

    def get_random_empty_cell(self):
        # 获取一个随机的空格子位置
        empty_cells = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col] == 0:
                    empty_cells.append((row, col))

        if len(empty_cells) != 0:
            return random.choice(empty_cells)
        else:
            return None

    def move(self, direction):
        # 根据方向移动棋盘
        moved = False
        if direction == 'up':
            self.move_up()
            moved = True
        elif direction == 'down':
            self.move_down()
            moved = True
        elif direction == 'left':
            self.move_left()
            moved = True
        elif direction == 'right':
            self.move_right()
            moved = True
        if moved:
            self.add_block()

    def move_up(self):
        for col in range(self.cols):
            lines = []
            for row in range(self.rows):
                if self.cells[row][col] != 0:
                    lines.append(self.cells[row][col])
                    self.cells[row][col] = 0
            lines = self.merge_cells(lines)
            for row in range(len(lines)):
                self.cells[row][col] = lines[row]

    def move_down(self):
        for col in range(self.cols):
            lines = []
            for row in range(self.rows):
                if self.cells[self.rows - row - 1][col] != 0:
                    lines.append(self.cells[self.rows - row - 1][col])
                    self.cells[self.rows - row - 1][col] = 0
                lines = self.merge_cells(lines)
            for row in range(len(lines)):
                self.cells[self.rows - row - 1][col] = lines[row]

    def move_left(self):
        for row in range(self.rows):
            lines = []
            for col in range(self.cols):
                if self.cells[row][col] != 0:
                    lines.append(self.cells[row][col])
                    self.cells[row][col] = 0
            lines = self.merge_cells(lines)
            for col in range(len(lines)):
                self.cells[row][col] = lines[col]

    def move_right(self):
        for row in range(self.rows):
            lines = []
            for col in range(self.cols):
                if self.cells[row][self.cols - col - 1] != 0:
                    lines.append(self.cells[row][self.cols - col - 1])
                    self.cells[row][self.cols - col - 1] = 0
            lines = self.merge_cells(lines)
            for col in range(len(lines)):
                self.cells[row][self.cols - col - 1] = lines[col]

    @staticmethod
    def merge_cells(line):
        merged_line = []
        for i in range(1, len(line)):
            if line[i] == line[i - 1]:
                line[i - 1] += line[i]
                line[i] = 0
        for i in range(len(line)):
            if line[i] != 0:
                merged_line.append(line[i])
        for i in range(len(line) - len(merged_line)):
            merged_line.append(0)
        return merged_line

    def draw(self, surface):
        # 遍历所有的方块，绘制到 Pygame 窗口上
        for row in range(self.rows):
            for col in range(self.cols):
                block = Block(self.cells[row][col])
                val = block.get_value()
                color = block.get_color()

                x = col * self.block_size + self.block_margin
                y = row * self.block_size + self.block_margin
                width = height = self.block_size - self.block_margin * 2

                # 绘制block
                pygame.draw.rect(surface, color, (x, y, width, height))
                if val != 0:
                    font_size = self.font_size if val < 100 else int(self.font_size * 0.7)
                    font = pygame.font.SysFont(self.font_name, font_size)
                    text = font.render(str(val), True, self.text_color)
                    text_rect = text.get_rect(center=(x + width / 2, y + height / 2))
                    surface.blit(text, text_rect)

    def draw_tip(self, surface):
        tip_bg_color = (42, 194, 210)
        tip_color = (0, 0, 0)
        tip_width = self.screen_w * 0.7
        tip_height = self.screen_h * 0.4
        tip_x = self.screen_w * 0.15
        tip_y = self.screen_h * 0.2
        pygame.draw.rect(surface, tip_bg_color, (tip_x, tip_y, tip_width, tip_height))
        font = pygame.font.SysFont(self.font_name, self.screen_w * 7 // 100)
        t = "The game is over. please press 'R' to play again, or press 'esc' to exit the game"
        text_rect = pygame.Rect(tip_x, tip_y, tip_width, tip_height)
        draw_text(surface, t, tip_color, text_rect, font, aa=True)
