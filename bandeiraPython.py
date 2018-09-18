from graphics import*
win=GraphWin('bandeira do Brasil',500,400)
aRectengle=Rectangle(Point(0,0),Point(500,400))
aRectengle.setFill("green")
aRectengle.draw(win)



apolygon=Polygon(Point(50,200) ,Point(250,50) , Point(250,50) , Point(450,200), Point(250,350))
apolygon.setFill("yellow")
apolygon.draw(win)
acircle=Circle(Point(250,200), 100)
acircle.setFill("blue")
acircle.draw(win)






win.getMouse()
win.close()
