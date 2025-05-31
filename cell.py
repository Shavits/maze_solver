from graphics import Point, Line

class Cell():


    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, point1, point2):
        self.__x1 = point1.x
        self.__y1 = point1.y
        self.__x2 = point2.x
        self.__y2 = point2.y
        if self.has_left_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "black"
            )
        if self.has_right_wall:
            self.__win.draw_line(
                Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "black"
            )
        if self.has_top_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "black"
            )
        if self.has_bottom_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "black"
            )

