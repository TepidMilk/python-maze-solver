from line import Line
from point import Point
class Cell():
    def __init__(self, win):
        self.has_l_wall = True
        self.has_r_wall = True
        self.has_t_wall = True
        self.has_b_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_l_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        if self.has_t_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        if self.has_b_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")
        if self.has_r_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")