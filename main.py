from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    line_1 = Line(Point(0,0), Point(150,50))
    line_2 = Line(Point(40,70), Point(520,50))
    line_3 = Line(Point(30,20), Point(530,50))
    line_4 = Line(Point(250,110), Point(150,50))
    win.draw_line(line_1, "red")
    win.draw_line(line_2, "green")
    win.draw_line(line_3, "yellow")
    win.draw_line(line_4, "blue")
    win.wait_for_close()

if __name__ == "__main__":
    main()




