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

w=0
for z in range(0,20):
    for x in range(159,353):
        y=0.0007868937*(x**2)+(-0.19290505676*x)+169.83498452
        ponto=Point(x-w,y+z)
        ponto.setOutline("white")
        ponto.draw(win)
    w=w+0.3




win.getMouse()
win.close()
