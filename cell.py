from graphics import Point, Line

class Cell():


    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.visited = False
        self.__win = window

    def draw(self, point1, point2):
        self.__x1 = point1.x
        self.__y1 = point1.y
        self.__x2 = point2.x
        self.__y2 = point2.y
        left_color = "white"
        right_color = "white"
        top_color = "white"
        bottom_color = "white"
        if self.has_left_wall:
            left_color = "black"
        if self.has_right_wall:
            right_color = "black"
        if self.has_top_wall:
            top_color = "black"
        if self.has_bottom_wall:
            bottom_color = "black"
        self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), left_color
            )
        self.__win.draw_line(
                Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), right_color
            )
        self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), top_color
            )
        self.__win.draw_line(
                Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), bottom_color
            )

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "grey"
        self_center = Point(
            (self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2
        )
        to_center = Point(
            (to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2
        )
        self.__win.draw_line(
            Line(self_center, to_center), color
        )
        

