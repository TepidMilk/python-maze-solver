from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)
    cell1.draw(20, 20, 40, 40)
    cell2.draw(40, 20, 60, 40)
    cell3.draw(20, 40, 40, 60)
    cell1.draw_move(cell2)
    win.wait_for_close()

main()