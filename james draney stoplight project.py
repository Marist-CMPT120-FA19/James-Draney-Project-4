#traffic light assingment
#yktv
#James Draney
#jamesdraney99@gmail.com


from graphics import *

def main():
    win = GraphWin()
    Center = Point(100,100)
    shape = Rectangle(Point(130,190),Point(70,30))
    shape.setFill("white")
    shape.setOutline("black")
    shape.draw(win) 
    circ = Circle(Point(99.5,65),20)
    circ.setFill("red")
    circ.setOutline("black")
    circ.draw(win)
    circ = Circle(Point(99.5,110),20)
    circ.setFill("yellow")
    circ.setOutline("black")
    circ.draw(win)
    circ = Circle(Point(99.5,155),20)
    circ.setFill("green")
    circ.setOutline("black")
    circ.draw(win)
main()
