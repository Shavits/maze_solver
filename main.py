from graphics import Window, Line, Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(
        x1=50,
        y1=50,
        num_rows=4,
        num_cols=4,
        cell_size_x=50,
        cell_size_y=50,
        win=win
    )

    win.wait_for_close()

if __name__ == "__main__":
    main()




