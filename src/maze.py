import time
import random
from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.current = None
    
    def _create_cells(self):
        y_start = self._cell_size_y
        if self._num_cols < 2 or self._num_rows < 2:
            raise Exception("Invalid Maze Size")
        if self._cell_size_x < 10 or self._cell_size_y < 10:
            raise Exception("Invalid Cell Size")
        for i in range(self._num_cols):
            self._cells.append([Cell(self._win)] * self._num_rows)
        for col in self._cells:
            self._y1 = y_start
            for cell in col:
                self.current = cell
                self._draw_cell(self._cell_size_x, self._cell_size_y)
                self._y1 += self._cell_size_y
            self._x1 += self._cell_size_x

    def _draw_cell(self, i, j):
        if self._win == None:
            return
        x1 = self._x1
        y1 = self._y1
        x2 = self._x1 + i
        y2 = self._y1 + j
        self.current.draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.1)

