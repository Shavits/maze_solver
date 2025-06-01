from cell import Cell
from graphics import Point, Line
import time


class Maze():

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()


    def __create_cells(self):
        for col in range(self.__num_cols):
            self.__cells.append([])
            for row in range(self.__num_rows):
                self.__cells[col].append(Cell(self.__win))
                self.__draw_cell(col, row)
        self.__break_entrance_and_exit()

    

    def __draw_cell(self, col, row):
        if self.__win is None:
            return
        self.__cells[col][row].draw(
            Point(
                self.__x1 + col * self.__cell_size_x,
                self.__y1 + row * self.__cell_size_y,
            ),
            Point(
                self.__x1 + (col + 1) * self.__cell_size_x,
                self.__y1 + (row + 1) * self.__cell_size_y,
            )
        )
        self.__animate()

    
    def __animate(self):
        if self.__win is  None:
            return
        self.__win.redraw()
        time.sleep(0.05)


    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)

