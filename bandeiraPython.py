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

for x in range(160,350):
    y=0.0007868937*(x**2)+(-0.19290505676*x)+169.83498452
    ponto=Point(x,y)
    ponto.setOutline("white")
    ponto.draw(win)

for x in range(155,349):
    y=0.00060461956*(x**2)+(-0.06672554347*x)+173.05546875
    ponto=Point(x,y)
    ponto.setOutline("white")
    ponto.draw(win)





win.getMouse()
win.close()
