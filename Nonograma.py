import pygame
import sys

class Nonograma:
    def __init__(self, grid, solution, row_clues, col_clues):
        self.grid = grid
        self.solution = solution
        self.row_clues = row_clues
        self.col_clues = col_clues
        self.size = len(grid)

    def toggle_cell(self, x, y):
        if 0 <= y < self.size and 0 <= x < self.size:
            self.grid[y][x] = 1 - self.grid[y][x]

    def verificar(self):
        for fila in range(self.size):
            for columna in range(self.size):
                if self.grid[fila][columna] != self.solution[fila][columna]:
                    return False
        return True
