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
mensagem=Text(Point(208,174), 'M')
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


bpolygon=Polygon(Point(250,250 ), Point(243,259),Point(257, 253),Point(241, 253), Point(255, 259))
bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')

bpolygon=Polygon(Point(270,270 ), Point(263,279),Point(277, 273),Point(262, 273), Point(275, 279))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')

bpolygon=Polygon(Point(230,200 ), Point(223,209),Point(237, 203),Point(222, 203), Point(235, 209))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(172, 223 ), Point(165,232),Point(179, 226),Point(164, 226), Point(177, 232))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(180 ,251 ), Point(175,260),Point(189, 254),Point(174, 254), Point(187, 260))
bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(289, 220), Point(282,229),Point(296, 223),Point(281, 223), Point(294,229))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(305, 245), Point(298,254),Point(312, 248),Point(297, 248), Point(310,254))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(216,269), Point(209,278),Point(222, 272),Point(208, 272), Point(221,278))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(187,207), Point(182,215),Point(194, 210),Point(179,210 ), Point(192,215))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(198, 234), Point(193,242),Point(202, 236),Point(192,236 ), Point(199,242))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(164, 191), Point(157,199),Point(170, 194),Point(156,194 ), Point(169,199))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(260, 209), Point(253,217),Point(267, 212),Point(252,212 ), Point(265,217))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(260, 232), Point(253,239),Point(265, 235),Point(253,235 ), Point(265,239))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(319, 219), Point(312,227),Point(326,222),Point(312,222), Point(324,227))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(300, 263), Point(295,272),Point(306,266),Point(293,266), Point(305,272))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(276, 246), Point(270,254),Point(282,249),Point(269,249), Point(281,254))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(244, 276), Point(238,284),Point(251,279),Point(236,279), Point(249,284))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(213, 250), Point(208,259),Point(219,253),Point(206,253), Point(218,259))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(210, 214), Point(205,222),Point(217,217),Point(203,217), Point(215,222))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(327, 241), Point(322,248),Point(332,244),Point(322,244), Point(332,248))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(184, 192), Point(179,199),Point(189,195),Point(178,195), Point(189,199))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(204,195) ,Point(199,202),Point(209,198),Point(199,198), Point(209,202))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')

bpolygon=Polygon(Point(161, 207) ,Point(156,214),Point(166,210),Point(156,210), Point(166,214))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(235, 216) ,Point(230,223),Point(240,219),Point(230,219), Point(240,223))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')
bpolygon=Polygon(Point(300, 169) ,Point(295,176),Point(305,172),Point(295,172), Point(305,176))

bpolygon.setFill("white")
bpolygon.draw(win)
bpolygon.setOutline('white')



win.getMouse()
win.close()
