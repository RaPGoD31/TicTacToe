from graphics import *
import random
yasmin = GraphWin("16290804",300,350)
yasmin.setCoords(0.0,0.0,30.0,35.0)
yasmin.items = []
a=True
def Yasmin():
    x=0
    y=35
    j=9
    i,k=0,0
    while j>=0:
        arda = Rectangle(Point(x,y),Point(x+10,y-10))
        arda.draw(yasmin)
        j-=1
        x+=10
        i+=1
        k+=1
        if i==3:
            x=0
            y=25
            i=0
        if k==6:
            x=0
            y=15
            k=0
def who_won():
    if (yasmin.items[0].getText() == yasmin.items[1].getText() and yasmin.items[1].getText() == yasmin.items[2].getText()):
        if yasmin.items[0].getText() == "X":
            victoryX()
        elif yasmin.items[0].getText() == "O":
            victoryO()
        return False
    elif (yasmin.items[3].getText() == yasmin.items[4].getText() and yasmin.items[4].getText() == yasmin.items[5].getText()):
        if yasmin.items[3].getText() == "X":
            victoryX()
        elif yasmin.items[3].getText() == "O":
            victoryO()
        return False
    elif (yasmin.items[6].getText() == yasmin.items[7].getText() and yasmin.items[7].getText() == yasmin.items[8].getText()):
        if yasmin.items[6].getText() == "X":
            victoryX()
        elif yasmin.items[6].getText() == "O":
            victoryO()
        return False
    elif (yasmin.items[0].getText() == yasmin.items[3].getText() and yasmin.items[3].getText() == yasmin.items[6].getText()):
        if yasmin.items[0].getText() == "X":
            victoryX()
        elif yasmin.items[0].getText() == "O":
            victoryO()
        return False
    elif (yasmin.items[1].getText() == yasmin.items[4].getText() and yasmin.items[4].getText() == yasmin.items[7].getText()):
        if yasmin.items[1].getText() == "X":
            victoryX()
        elif yasmin.items[1].getText() == "O":
            victoryO()
        return False
    elif (yasmin.items[2].getText() == yasmin.items[5].getText() and yasmin.items[5].getText() == yasmin.items[8].getText()):
        if yasmin.items[2].getText() == "X":
            victoryX()
        elif yasmin.items[2].getText() == "O":
            victoryO()
        return False
    elif (yasmin.items[0].getText() == yasmin.items[4].getText() and yasmin.items[4].getText() == yasmin.items[8].getText()):
        if yasmin.items[0].getText() == "X":
            victoryX()
        elif yasmin.items[0].getText() == "O":
            victoryO()
        return False
    elif (yasmin.items[2].getText() == yasmin.items[4].getText() and yasmin.items[4].getText() == yasmin.items[6].getText()):
        if yasmin.items[2].getText() == "X":
            victoryX()
        elif yasmin.items[2].getText() == "O":
            victoryO()
        return False
    else:
        for i in range(9):
            if yasmin.items[i].getText() not in ['X', 'O']:
                return True
        endgame()
        return False

def victoryO():
    """O Win"""
    text1 = Text(Point(15, 2.5), "O Wins")
    text1.draw(yasmin)
    endgame2()

def victoryX():
    """X win"""
    text1 = Text(Point(15, 2.5), "X Wins")
    text1.draw(yasmin)
    endgame2()

def endgame():
    """Tie"""
    text1 = Text(Point(15, 2.5), "Draw!")
    text1.draw(yasmin)
    endgame2()

def text():
    """give a text for control who win"""
    for z in range(9):
        lan = Text(Point(5 + (z % 3) * 10, 30 - (z // 3) * 10), str(z))
        yasmin.items.append(lan)


def selam():
    """oldu gibi"""
    """o koymuyor"""
    warn = Text(Point(15, 2.5), "You cannot click the filled squares!")
    while (who_won()):
        p1 = yasmin.getMouse()
        #bazen o koymuyor, atlama
        if ((p1.getX() > 0 and p1.getX() < 10) and (p1.getY() > 25 and p1.getY() < 35)):
            if yasmin.items[0].getText() == "0":
                warn.undraw()
                a = yasmin.items[0]
                a.setText("X")
                a.draw(yasmin)
                if who_won()==True:
                    comp_play()
            else:
                try:
                    warn.draw(yasmin)
                except:
                    continue
        elif ((p1.getX() > 10 and p1.getX() < 20) and (p1.getY() > 25 and p1.getY() < 35)):
            if yasmin.items[1].getText() == "1":
                warn.undraw()
                a = yasmin.items[1]
                a.setText("X")
                a.draw(yasmin)
                if who_won() == True:
                    comp_play()
            else:
                try:
                    warn.draw(yasmin)
                except:
                    continue
        elif ((p1.getX() > 20 and p1.getX() < 30) and (p1.getY() > 25 and p1.getY() < 35)):
            if yasmin.items[2].getText() == "2":
                warn.undraw()
                a = yasmin.items[2]
                a.setText("X")
                a.draw(yasmin)
                if who_won() == True:
                    comp_play()
            else:
                try:
                    warn.draw(yasmin)
                except:
                    continue
        elif ((p1.getX() > 0 and p1.getX() < 10) and (p1.getY() > 15 and p1.getY() < 25)):
            if yasmin.items[3].getText() == "3":
                warn.undraw()
                a = yasmin.items[3]
                a.setText("X")
                a.draw(yasmin)
                if who_won() == True:
                    comp_play()
            else:
                try:
                    warn.draw(yasmin)
                except:
                    continue
        elif ((p1.getX() > 10 and p1.getX() < 20) and (p1.getY() > 15 and p1.getY() < 25)):
            if yasmin.items[4].getText() == "4":
                warn.undraw()
                a = yasmin.items[4]
                a.setText("X")
                a.draw(yasmin)
                if who_won() == True:
                    comp_play()
            else:
                try:
                    warn.draw(yasmin)
                except:
                    continue
        elif ((p1.getX() > 20 and p1.getX() < 30) and (p1.getY() > 15 and p1.getY() < 25)):
            if yasmin.items[5].getText() == "5":
                warn.undraw()
                a = yasmin.items[5]
                a.setText("X")
                a.draw(yasmin)
                if who_won() == True:
                    comp_play()
            else:
                try:
                    warn.draw(yasmin)
                except:
                    continue
        elif ((p1.getX() > 0 and p1.getX() < 10) and (p1.getY() > 5 and p1.getY() < 15)):
            if yasmin.items[6].getText() == "6":
                warn.undraw()
                a = yasmin.items[6]
                a.setText("X")
                a.draw(yasmin)
                if who_won() == True:
                    comp_play()
            else:
                try:
                    warn.draw(yasmin)
                except:
                    continue
        elif ((p1.getX() > 10 and p1.getX() < 20) and (p1.getY() > 5 and p1.getY() < 15)):
            if yasmin.items[7].getText() == "7":
                warn.undraw()
                a = yasmin.items[7]
                a.setText("X")
                a.draw(yasmin)
                if who_won() == True:
                    comp_play()
            else:
                try:
                    warn.draw(yasmin)
                except:
                    continue
        elif ((p1.getX() > 20 and p1.getX() < 30) and (p1.getY() > 5 and p1.getY() < 15)):
            if yasmin.items[8].getText() == "8":
                warn.undraw()
                a = yasmin.items[8]
                a.setText("X")
                a.draw(yasmin)
                if who_won() == True:
                    comp_play()
            else:
                try:
                    warn.draw(yasmin)
                except:
                    continue
        elif p1.getY() < 5:
            continue
def comp_play():
    x1 = random.randint(0,30)
    y1 = random.randint(5,35)
    if ((x1 > 0 and x1 < 10) and (y1 > 25 and y1 < 35)):
        if yasmin.items[0].getText() == "0":
            a = yasmin.items[0]
            a.setText("O")
            a.draw(yasmin)
        else:
            comp_play()
    elif ((x1 > 10 and x1 < 20) and (y1 > 25 and y1 < 35)):
        if yasmin.items[1].getText() == "1":
            a = yasmin.items[1]
            a.setText("O")
            a.draw(yasmin)
        else:
            comp_play()
    elif ((x1 > 20 and x1 < 30) and (y1 > 25 and y1 < 35)):
        if yasmin.items[2].getText() == "2":
            a = yasmin.items[2]
            a.setText("O")
            a.draw(yasmin)
        else:
            comp_play()
    elif ((x1 > 0 and x1 < 10) and (y1 > 15 and y1 < 25)):
        if yasmin.items[3].getText() == "3":
            a = yasmin.items[3]
            a.setText("O")
            a.draw(yasmin)
        else:
            comp_play()
    elif ((x1 > 10 and x1 < 20) and (y1 > 15 and y1 < 25)):
        if yasmin.items[4].getText() == "4":
            a = yasmin.items[4]
            a.setText("O")
            a.draw(yasmin)
        else:
            comp_play()
    elif ((x1 > 20 and x1 < 30) and (y1 > 15 and y1 < 25)):
        if yasmin.items[5].getText() == "5":
            a = yasmin.items[5]
            a.setText("O")
            a.draw(yasmin)
        else:
            comp_play()
    elif ((x1 > 0 and x1 < 10) and (y1 > 5 and y1 < 15)):
        if yasmin.items[6].getText() == "6":
            a = yasmin.items[6]
            a.setText("O")
            a.draw(yasmin)
        else:
            comp_play()
    elif ((x1 > 10 and x1 < 20) and (y1 > 5 and y1 < 15)):
        if yasmin.items[7].getText() == "7":
            a = yasmin.items[7]
            a.setText("O")
            a.draw(yasmin)
        else:
            comp_play()
    elif ((x1 > 20 and x1 < 30) and (y1 > 5 and y1 < 15)):
        if yasmin.items[8].getText() == "8":
            a = yasmin.items[8]
            a.setText("O")
            a.draw(yasmin)
        else:
            comp_play()
    else:
        comp_play()


def endgame2():
    p1 = yasmin.getKey()
    if p1=="q":
        yasmin.close()
    else:
        endgame2()

try:
    text()
    Yasmin()
    selam()
except:
    yasmin.close()

