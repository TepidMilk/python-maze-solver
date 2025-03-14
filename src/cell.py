from line import Line
from point import Point
class Cell():
    def __init__(self, win = None):
        self.visited = False
        self.has_l_wall = True
        self.has_r_wall = True
        self.has_t_wall = True
        self.has_b_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        
    """method allowing cell to draw itself"""
    def draw(self, x1, y1, x2, y2):
        if self._win == None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_b_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")
        elif not self.has_b_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_t_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        elif not self.has_t_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_l_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        elif not self.has_l_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_r_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        elif not self.has_r_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
    
    """Draws a line showing a move from one cell to another"""
    def draw_move(self, to_cell, undo=False):
        fill_color = "blue"
        if undo == True:
            fill_color = "red"
        from_x = (self._x1 + self._x2) // 2 
        from_y = (self._y1 + self._y2) // 2
        to_x = (to_cell._x1 + to_cell._x2) // 2
        to_y = (to_cell._y1 + to_cell._y2) // 2
        line = Line(Point(from_x, from_y), Point(to_x, to_y))
        self._win.draw_line(line, fill_color)
        