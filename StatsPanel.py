from gpanel import *
from database1 import *

width = int(getScreenWidth() / 4.4)
height = int(getScreenHeight() / 5)

dbn = Database("names")
dbw = Database("wins")

makeGPanel(Size(width,height ))
title("Statistiken")
resizable(False)
windowPosition(10,40)
font(Font("Verdana",Font.PLAIN,16))
liste = "";

#resetWins
rW1 = [0.7,0.1]
rW2 = [1,0.2]

#changeNames
chn1 = [0.7,0.25]
chn2 = [1,0.35]

def getList():
    dbn = Database("names")
    dbw = Database("wins")
    return str(dbn.n1) + str(dbn.n2) + str(dbw.wins1) + str(dbw.wins2) + str(dbw.played)



@onMousePressed
def onMouseClicked(x,y):
    global dbw
    #resetWins
    if y >= rW1[1] and y <= rW2[1] and x >= rW1[0] and x<=rW2[0]:
        r = askYesNo("Möchtest du wirklich alle Gewinne resetten?",False)
        #False, None nicht
        if r == True:
            dbw.wins1 = 0
            dbw.wins2 = 0
            dbw.played = 0
    if y >= chn1[1] and y <= chn2[1] and x >= chn1[0] and x<=chn2[0]:
        name1 = input("Name des Spieler 1",False)
        name2 = input("Name des Spieler 2",False)
        if name1 != None:
            dbn.n1 = name1
        if name2 != None:
            dbn.n2 = name2
    print(str(x) + " " + str(y))


def setStats():
    setColor("black")
    text(0.2,0.7 , "Gespielte Spiele: " + str(dbw.played))
    text(0.2,0.4, "Siege " + str(dbn.n1) + ": " + str(dbw.wins1))
    text(0.2,0.2, "Siege " + str(dbn.n2) + ": " + str(dbw.wins2))
    setColor("gray")
    fillRectangle(rW1,rW2)
    fillRectangle(chn1,chn2)
    setColor("black")
    text(0.71,0.12,"Reset wins")
    text(0.71,0.27,"Change names")


#drawGrid(1,1,"black")
while(1==1):
    dbn = Database("names")
    dbw = Database("wins")
    if getList() != liste:
        liste = getList()
        clear()
        setStats()
   #     print("Set")
    #else:
      #  print(liste)
     #   print(getList())
    delay(1000)
    #print("a")