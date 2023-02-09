#global representation
currentplayer = None
gamerunning = True
winner = None
tie = None
import random
#board representation
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
def boarddisplay(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def playerinput(board):
    global currentplayer
    position = int(input("Type position (1-9):  "))
    if board[position-1] == "X" or board[position-1] == "O":
        print("Oop, wont work")
        playerinput(board)
    elif position < 1 or position > 9:
        print("Oop, wont work")
        playerinput(board)
    else:
        board[position - 1] = currentplayer

def switchplayer():
    global currentplayer
    if currentplayer == "X" or None:
        currentplayer = "O"
    else:
        currentplayer = "X"

def checkwin(board):
    global gamerunning
    if (board[0] == board[1] == board[2] and board[0] != "-" or
    board[3] == board[4] == board[5] and board[3] != "-" or
    board[6] == board[7] == board[8] and board[6] != "-" or
    board[0] == board[3] == board[6] and board[0] != "-" or
    board[1] == board[4] == board[7] and board[1] != "-" or
    board[2] == board[5] == board[8] and board[2] != "-" or
    board[0] == board[4] == board[8] and board[0] != "-" or
    board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentplayer
        print("{} is the winner".format(winner))
        if winner != None:
            gamerunning = False
            boarddisplay(board)

def checktie(board):
    global tie
    if "-" not in board:
        gamerunning = False
        print("Game is tie")
        tie = True

def computerinput(board):
    comput = random.randint(0,8)
    if board[comput] == "X" or board[comput] == "O":
        computerinput(board)
    if board[comput] == "-":
        board[comput] = "O"
        switchplayer()

def restart():
    global winner
    global board
    global tie
    global gamerunning
    if tie == True or winner != None:
        statement = input("will you like to play again (yes or no): ")
        if statement == "yes".lower():
            board = ["-","-","-",
                     "-","-","-",
                     "-","-","-",]
            tie = None
            winner = None
            gamerunning = True
        elif statement == "no".lower():
            print("Game End")


while gamerunning is True:
    switchplayer()
    boarddisplay(board)
    playerinput(board)
    checkwin(board)
    checktie(board)
    restart()
    computerinput(board)
    checkwin(board)
    checktie(board)
    restart()