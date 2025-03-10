import time
import random
from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        if seed != None:
            random.seed(seed)
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._entrance = None
        self._exit = None
    
    def _create_cells(self):
        if self._num_cols <= 2  or self._num_rows <= 2:
            raise Exception("Invalid Maze Size")
        if self._cell_size_x < 10 or self._cell_size_y < 10:
            raise Exception("Invalid Cell Size")
        self._cells = [
        [Cell(self._win) for _ in range(self._num_rows)] 
        for _ in range(self._num_cols)
        ]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _create_adjaceny_list(self):
        adjaceny_list = {}
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                current = self._cells[i][j]
                if current not in adjaceny_list:
                    adjaceny_list[current] = []
                if current.has_l_wall == False and i != 0:
                    adjaceny_list[current].append(self._cells[i-1][j])
                if current.has_t_wall == False and j != 0:
                    adjaceny_list[current].append(self._cells[i][j-1])
                if current.has_r_wall == False and i != self._num_cols - 1:
                    adjaceny_list[current].append(self._cells[i+1][j])
                if current.has_b_wall == False and j != self._num_rows - 1:
                    adjaceny_list[current].append(self._cells[i][j+1])
        return adjaceny_list


    def _draw_cell(self, i, j):
        if self._win == None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        i = random.choice([0, self._num_cols - 1])
        i = random.choice([i, random.randrange(1, self._num_cols - 2)])
        if i == 0 or i == self._num_cols - 1:
            j = random.randrange(0, self._num_rows)
        else:
            j = random.choice([0, self._num_rows - 1])
        self._entrance = (i, j)        
        midpoint_x = self._num_cols / 2
        midpoint_y = self._num_rows / 2
        ei = midpoint_x + (midpoint_x - i - 1)
        ej = midpoint_y + (midpoint_y - j - 1)
        ei = int(ei)
        ej = int(ej)
        self._exit = (ei, ej)
        exit = self._cells[ei][ej]

        if j == 0:
            self._cells[i][j].has_t_wall = False
            exit.has_b_wall = False
        elif j == self._num_rows - 1:
            self._cells[i][j].has_b_wall = False
            exit.has_t_wall = False
        elif i == 0:
            self._cells[i][j].has_l_wall = False
            exit.has_r_wall = False
        elif i == self._num_cols - 1:
            self._cells[i][j].has_r_wall = False
            exit.has_l_wall = False
        
        self._draw_cell(i,j)
        self._draw_cell(ei, ej)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        n = self._num_cols - 1
        m = self._num_rows - 1
        while True:
            to_visit = []
            left = (i-1, j)
            right = (i+1, j)
            up = (i, j-1)
            down = (i, j+1)
            if i > 0 and self._cells[i-1][j].visited == False:
                to_visit.append(left)
            if i < n and self._cells[i+1][j].visited == False:
                to_visit.append(right)
            if j > 0 and self._cells[i][j-1].visited == False:
                to_visit.append(up)
            if j < m and self._cells[i][j+1].visited == False:
                to_visit.append(down)
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction = random.choice(to_visit)
            if direction == left:
                self._cells[i][j].has_l_wall = False
                self._cells[left[0]][left[1]].has_r_wall = False
                self._break_walls_r(left[0], left[1])
            elif direction == right:
                self._cells[i][j].has_r_wall = False
                self._cells[right[0]][right[1]].has_l_wall = False
                self._break_walls_r(right[0], right[1])
            elif direction == up:
                self._cells[i][j].has_t_wall = False
                self._cells[up[0]][up[1]].has_b_wall = False
                self._break_walls_r(up[0], up[1])
            elif direction == down:
                self._cells[i][j].has_b_wall = False
                self._cells[down[0]][down[1]].has_t_wall = False
                self._break_walls_r(down[0], down[1])
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(self._entrance[0], self._entrance[1])
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self._exit[0]][self._exit[1]]:
            return True
        #down move
        if j < (self._num_rows - 1) and self._cells[i][j].has_b_wall == False and self._cells[i][j+1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        #right move
        if i < (self._num_cols - 1) and self._cells[i][j].has_r_wall == False and self._cells[i+1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        #left move
        if i > 0 and self._cells[i][j].has_l_wall == False and self._cells[i-1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        #up move
        if j > 0 and self._cells[i][j].has_t_wall == False and self._cells[i][j-1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        return False
    
    def _solve_bsf(self):
        adjaceny_list = self._create_adjaceny_list()
        to_visit = []
        to_visit.append(self._cells[self._entrance[0]][self._entrance[1]])
        current = to_visit[0]
        while to_visit:
            self._animate()
            current.visited = True
            current = to_visit.pop(0)
            sorted_neighbors = adjaceny_list[current]
            for neighbor in sorted_neighbors:
                if neighbor == self._cells[self._exit[0]][self._exit[1]]:
                    current.draw_move(neighbor)
                    return
                if neighbor.visited == False and neighbor not in to_visit:
                    current.draw_move(neighbor)
                    to_visit.append(neighbor)
        return
        
        