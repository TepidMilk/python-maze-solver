from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(20, 20, 5, 5, 20, 20, win)
    win.wait_for_close()

main()