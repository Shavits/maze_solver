from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.draw(Point(100, 100), Point(200, 200))
    cell2.draw(Point(200, 100), Point(300, 200))
    cell1.draw_move(cell2, True)

    win.wait_for_close()

if __name__ == "__main__":
    main()




