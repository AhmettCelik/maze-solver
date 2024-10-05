from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(300, 400, 400, 500)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(600, 400, 700, 500)

    c1.draw_move(c2, True)

    win.wait_for_close()

if __name__ == "__main__":
    main()
