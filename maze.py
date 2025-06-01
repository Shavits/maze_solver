from cell import Cell
from graphics import Point, Line
import time
import random


class Maze():

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.directions = {"up" : (0,-1), "down" : (0,1), "left" : (-1,0), "right" : (1,0)}
        if seed is not None:
            random.seed(seed)
        self.__create_cells()


    def __create_cells(self):
        for col in range(self.__num_cols):
            self.__cells.append([])
            for row in range(self.__num_rows):
                self.__cells[col].append(Cell(self.__win))
                self.__draw_cell(col, row)
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)

    

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

    def __break_walls_r(self,col,row):
        print(f"breaking walls {col}, {row}")
        self.__cells[col][row].visited = True
        while True:
            to_visit = []
            for dir_name, dir_value in self.directions.items():
                nbr_col = col + dir_value[0]
                nbr_row = row + dir_value[1]
                #print(f"checking neigbour at {dir_name}, {nbr_col}, {nbr_row}")
                if nbr_col >= 0 and nbr_col<self.__num_cols and nbr_row >= 0 and nbr_row < self.__num_rows:
                    #print("in bounds")
                    if not self.__cells[nbr_col][nbr_row].visited:
                        to_visit.append((dir_name,(nbr_col, nbr_row)))
            if len(to_visit) == 0:
                self.__draw_cell(col,row)
                print("dead_end")
                return
            idx = random.randint(0, len(to_visit)-1)
            
            dir_name, (nbr_col,nbr_row) = to_visit[idx]
            if dir_name == "up":
                self.__cells[col][row].has_top_wall = False
                self.__cells[nbr_col][nbr_row].has_bottom_wall = False
            elif dir_name == "down":
                self.__cells[col][row].has_bottom_wall = False
                self.__cells[nbr_col][nbr_row].has_top_wall = False
            elif dir_name == "left":
                self.__cells[col][row].has_left_wall = False
                self.__cells[nbr_col][nbr_row].has_right_wall = False
            elif dir_name == "right":
                self.__cells[col][row].has_right_wall = False
                self.__cells[nbr_col][nbr_row].has_left_wall = False
            print(dir_name)
            self.__draw_cell(col, row)
            self.__draw_cell(nbr_col, nbr_row)
            self.__break_walls_r(nbr_col,nbr_row)

            





