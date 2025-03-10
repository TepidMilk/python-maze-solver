from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(20, 20, 20, 20, 20, 20, win)
    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze._solve_bsf()
    win.wait_for_close()

main()