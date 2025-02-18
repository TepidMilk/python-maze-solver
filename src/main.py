from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    point1 = Point(0,0)
    point2 = Point(800, 600)
    line = Line(point1, point2)
    win.draw_line(line, "black")
    win.wait_for_close()

main()