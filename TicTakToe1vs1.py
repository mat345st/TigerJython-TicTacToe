from gturtle import *
from database1 import *
#from testGPanel import *
import subprocess
#from gconsole import *
#makeTurtle(mousePressed = mouseClicked)

#final
fieldSize = 100
startPosX = fieldSize * -1.5
startPosY = fieldSize * -1.5

#Databas for logging wins
db = Database("wins")
dbName = Database("names")

bgColor = "#F0FFFF"

#open the window
setFramePositionCenter()
setPlaygroundSize(1000,500)
makeTurtle()
ht()
#stat = TurtleFrame("Statistiken")

#parameters for playing
running = 1
currentPlayer = 1
winner = 0
#name1 = "Spieler 1"
#name2 = "Spieler 2"
print("First player: " + str(currentPlayer))
print("Added")
#   x   y
fields=[ [0,0,0],[0,0,0],[0,0,0]  ]
#

#get the row by y
def getRow(y):
    z = 0
    a = startPosY
    if y < a:
        return None
    repeat 4:
        if y < a:
            return z
        a += fieldSize
        z += 1
    
#get the column by x
def getColumn(x):
    z = 0
    a = startPosX
    if x < a:
        return None
    repeat 4:
        if x < a:
            return z
        a += fieldSize
        z += 1
    
# go to a field
def goToField(rows,columns):
    setPos(startPosX + (columns-1) * fieldSize,startPosY + (rows-1) * fieldSize)
    
    
#fill the field at the current position
def fillField():
    global currentPlayer
    pu()
    right(90)
    fd(fieldSize / 2)
    left(90)
    fd(fieldSize / 2)
    pd()
    setPenWidth(7)
    if currentPlayer == 1:
        openDot(fieldSize / 10 * 8)
    else:
        right(45)
        repeat 4:
            fd(1/1.414 * fieldSize / 10 *9)  
            bk(1/1.414 * fieldSize / 10 *9)
            right(90)
        left(45)

    #Mit Farben:
    #pu()
    #fd(fieldSize / 10)
    #rt(90)
    #fd(fieldSize/10)
    #lt(90)
    #pd()
    #startPath()
    #repeat 4:
    #    fd(fieldSize/10*8)
    #    right(90)
    #fillPath()

def processingBar(sec):
    global fieldSize
    sec -= 0.1
    y = fieldSize * -1.5 - fieldSize / 10
    xmin = fieldSize * -1.5 - fieldSize / 5
    xmax = fieldSize * 1.5 + fieldSize / 5
    setPenWidth(5)
    setPos(xmin, y)
    right(90)
    repeat sec * 20:
        fd((-1 * xmin + xmax) / (sec * 20))
        delay(sec*1000 / sec/20)
    delay(100)
    right(-180)
    setPenColor(bgColor)
    fd(xmax + xmin*-1)
    right(90)
        
        


#################################################################
#at start und restart
def start():
    global currentPlayer
    global fields
    setTitle("TicTakToe")
    addStatusBar(20)
    setStatus()
    if currentPlayer == 1:
        setCustomCursor("kreuz.png")
    else:
        setCustomCursor("kreis.png")
    fields=[ [0,0,0],[0,0,0],[0,0,0]  ]
    clear(bgColor)
    setHeading(0)
    
    #setStat()

#at restart
def restart():
    global winner
    start()
    #eigentlich unnötig
    if winner == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1
    winner = None
    clear()

#####################################


def getCurrentName():
    global currentPlayer
    return getName(currentPlayer)
    #global dbn
    #dbn = Database("names")
    #if currentPlayer == 1:
    #    return dbn.n1
    #elif currentPlayer == 2:
    #    return dbn.n2
   # else:
    #    return "Error"
    
def getName(player):
    dbName = Database("names")
    if player == 1:
        return dbName.n1
    elif player == 2:
        return dbName.n2
    else:
        return "Error"



def getWinner():
    #oben nach unten von links nach rechts
    if fields[0][0] == fields[0][1] == fields[0][2] and fields[0][0] != 0:
        return fields[0][0]
    if fields[1][0] == fields[1][1] == fields[1][2] and fields[1][0] != 0:
        return fields[1][0]
    if fields[2][0] == fields[2][1] == fields[2][2] and fields[2][0] != 0:
        return fields[2][0]
    
    #von links nachrecht von oben nach unten
    if fields[0][0] == fields[1][0] == fields[2][0] and fields[0][0] != 0:
        return fields[0][0]
    if fields[0][1] == fields[1][1] == fields[2][1] and fields[0][1] != 0:
        return fields[0][1]
    if fields[0][2] == fields[1][2] == fields[2][2] and fields[0][2] != 0:
        return fields[0][2]
    
    #links oben nach rechts unten
    if fields[0][2] == fields[1][1] == fields[2][0] and fields[0][2] != 0:
        return fields[0][2]
    #links unten nach rechts oben
    if fields[0][0] == fields[1][1] == fields[2][2] and fields[0][0] != 0:
        return fields[0][0]
    for s in fields:
        for i in s:
            if i == 0:
                return None
    return 0



#change the player
def changePlayer():
    global currentPlayer
    #print("Get " + str(currentPlayer))

    if currentPlayer == 1:
        currentPlayer = 2
        setFillColor("red")
        setPenColor("red")
        setCustomCursor("kreis.png")
        #print("Now 2 Real " + str(currentPlayer))
    else:
        currentPlayer = 1
        setPenColor("blue")
        setFillColor("blue")
        setCustomCursor("kreuz.png")
    setStatus()
        #print("Now 1 Real " + str(currentPlayer))


def setStatus():
    setStatusText("Player: " + str(getCurrentName()))
##########################################################################
@onMouseHit
def mouseClicked(x, y):
    global running
    global winner
    global db
    if running == 0: #or isRightMouseButton():
        print("Not running")
        return
    running = 0
    print("Running not hit")
    row = getRow(y)
    column = getColumn(x)
    print("---\nSpalte: " + str(column))
    print("Zeile: " + str(row))
    
    if row == None or column == None:
        #print("Return: None selected")
        running = 1
        print("running now no field")
        return
    
    execHit(row,column)

def execHit(row,column):
    global running
    global winner
    global db
    if fields[row-1][column-1] != 0:
        print("Already filled")
        running = 1
        print("Running now already filled")
        return
    fields[row-1][column-1] = currentPlayer
    #print("Set field to " + str(fields[row-1][column-1]))
    #print("Player: " + str(currentPlayer))
    changePlayer()
    
    #Go to the size field
    goToField(row,column)
    fillField()
    print(str(fields)+"\n---")
    
    winner = getWinner()
    running = 1
    print("Running now exec")
    
    db = Database("wins")
    if winner != None:
        setStatusText("Ende")
        setPenColor("black")
        setPos(fieldSize + 100 , 0)
        if winner == 0:
            db.played += 1
            label("Kein Gewinner")
        else:
            label("Gewinner: "+ str(getName(winner)))
            db.played += 1
            if winner == 1:
                db.wins1 += 1
            elif winner == 2:
                db.wins2 += 1
        running = 0
        print("Running not bar")
        #tf = TurtleFrame("Statistiken")
        processingBar(6.5)
        #delay(6000)
        running = 1
        print("Running now bar")
        
        restart()
    
    
@onKeyHit
def onKeyClicked(keyCode):
    global running
    global winner
    global db
    if running == 0: #or isRightMouseButton():
        return
    running = 0
    print("Running not key")
    #1 = 49; 9 = 57
    #print("1")
    if keyCode < 49 or keyCode > 57:
       # print("2")
       running = 1
       print("Running now no key")
       return
   # print("3")
    row = 0
    column = 0
   # print("Test")
    if keyCode >= 49 and keyCode <= 51:
       # print("4")
        row = 2
        if keyCode == 50:
            column = 1
        elif keyCode == 51:
            column = 2
    elif keyCode>= 52 and keyCode <= 54:
        #print("5")
        row = 1
        if keyCode == 53:
            column = 1
        elif keyCode == 54:
            column = 2
    else:
      #  print("6")
        if keyCode == 56:
              column = 1
        elif keyCode == 57:
             column = 2
    
    execHit(row+1,column+1)
    
    
        
    
    
###########################################################################





def grid():
    setPos(startPosX, startPosY)
    repeat 3:
        repeat 3:
            repeat 4:
                fd(fieldSize)
                rt(90)
            fd(fieldSize)
        right(90)
        fd(fieldSize)
        right(90)
        fd(fieldSize * 3)
        right(180)


try:
    db.wins1
except KeyError:
    print("Set wins")
    db.wins1 = 0
    db.wins2 = 0
    db.played = 0


try:
    dbName.n1
except KeyError:
    print("Set names")
    dbName.n1 = "Spieler 1"
    dbName.n2 = "Spieler 2"


start()
grid()
savePlayground()
