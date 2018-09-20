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

mensagem=Text(Point(165,170), 'O')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(175,171), 'R')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(186,172), 'D')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(197,173), 'E')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(208,174), ' M')
mensagem.setOutline("green")
mensagem.draw(win)


mensagem=Text(Point(235,180), 'E')
mensagem.setOutline("green")
mensagem.draw(win)

mensagem=Text(Point(255,183), 'P')
mensagem.setOutline("green")
mensagem.draw(win)

mensagem=Text(Point(265,185), 'R')
mensagem.setOutline("green")
mensagem.draw(win)

mensagem=Text(Point(275,188), 'O')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(285,191), 'G')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(295,194), 'R')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(305,197), 'E')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(315,200), 'S')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(325,203), 'S')
mensagem.setOutline("green")
mensagem.draw(win)
mensagem=Text(Point(335,207), 'O')
mensagem.setOutline("green")
mensagem.draw(win)

bpolygon=Polygon(Point(230,230 ), Point(223,239),Point(237, 233),Point(222, 233), Point(235, 239))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')

bpolygon=Polygon(Point(240,240 ), Point(233,249),Point(247, 243),Point(231, 243), Point(245, 249))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')







win.getMouse()
win.close()
