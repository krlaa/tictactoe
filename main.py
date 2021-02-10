me = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

row = ""
column = ""
quitGame = False
legalMove = True
player1 = True
piece = "x"

count = 0;
compareString = ""
finalStr = "ooo" if player1 else "xxx"

def winCon():
  global piece
  global compareString
  global quitGame
  for i in range(3):
    for j in range(3):
      compareString+=game[i][j]
      if(compareString==finalStr):
        
        quitGame = True
        game_board()
        print(("player1" if player1 else "player2") +" won the game")  
    compareString = ""
  for i in range(3):
    for j in range(3):
      compareString+=game[j][i]
      if(compareString==finalStr):
        
        quitGame = True
        game_board()
        print(("player1" if player1 else "player2") +" won the game")    
    compareString = ""
  for i in range(3,0):
    compareString+=game[i][i]
    if(compareString==finalStr):
        quitGame = True
        game_board()
        print(("player1" if player1 else "player2") +" won the game")   
    compareString = ""
  for i in range(3):
    compareString+=game[i][i]
    if(compareString==finalStr):
        
        quitGame = True
        game_board()
        print(("player1" if player1 else "player2") +" won the game")    
    compareString = ""
def game_board():
    global game
    print("  0 1 2")
    for count, row in enumerate(game):
        print(count, *row)


def checkLegal(row, column):
    global player1
    if (game[row][column] == "_"):
        return True
    elif (player1 == True and game[row][column] == "x"):
        return False
    elif (player1 == False and game[row][column] == "o"):
        return False
    else:
        return False


def getInput(player):
    global legalMove
    global quitGame
    global row
    global column
    while (legalMove):
        row = input("{0} enter the row # example:0-2 or press q to quit game".
                    format(player))
        if (row == "q"):
            quitGame = True
            return None
        column = input(
            "{0} enter the column # example:0-2 or press q to quit game".
            format(player))
        if (column == "q"):
            quitGame = True
            return None
        row = int(row)
        column = int(column)
        if (not (row >= 0 and row <= 2) or not (column >= 0 and column <= 2)):
            pass
        else:
            break


def move(piece):
    global player1
    if (checkLegal(row, column)):
        game[row][column] = piece
        winCon()
    else:
        getInput("player1" if player1 else "player2")
        move(piece)
        winCon()


while (not quitGame):
    game_board()
    getInput("player1" if player1 else "player2")
    if(not quitGame):
      if (player1):
          move(piece)
          player1 = not player1
          piece = "x"
      else:
          move(piece)
          player1 = not player1
          piece = "o"
