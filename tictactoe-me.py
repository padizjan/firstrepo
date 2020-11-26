# testing code for tic-tac-toe versus
import random
import pprint

theBoard = {7: ' ', 8: ' ', 9: ' ',
            4: ' ', 5: ' ', 6: ' ',
            1: ' ', 2: ' ', 3: ' '}

def printBoard(bo):
    print(bo[7] + '|' + bo[8] + '|' + bo[9])
    print('-+-+-')
    print(bo[4] + '|' + bo[5] + '|' + bo[6])
    print('-+-+-')
    print(bo[1] + '|' + bo[2] + '|' + bo[3])

def addtoBoard(bo,le):
    bo[le] = 'X'

def addtoBoardAI(bo, le):
    bo[le] = 'O'

def game():
    while True:
        while True:
            try:
                x = int(input('''Where will you place 'X'?'''))
                if x in range(1,10):
                    break
                else:
                    print('You have inputted a wrong value.')
                    continue
            except ValueError:
                print('You have inputted a wrong value.')
                continue
        if theBoard[x] != ' ':
            print('That space is already occupied')
            continue
        else:
            break
    addtoBoard(theBoard, x)
    
def computerTurn():
    while True:
        y = random.randint(1,9)
        if theBoard[y] != ' ':
            continue
        else:
            addtoBoardAI(theBoard, y)
            break
        
def checkWinner(win):
    if theBoard[7] == theBoard[8] == theBoard[9] != ' ':
        print('Game over!!')
        return 1
    elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':
        print('Game over!!')
        return 1
    elif theBoard[1] == theBoard[2] == theBoard[3] != ' ':
        print('Game over!!')
        return 1
    elif theBoard[7] == theBoard[5] == theBoard[3] != ' ':
        print('Game over!!')
        return 1
    elif theBoard[9] == theBoard[5] == theBoard[1] != ' ':
        print('Game over!!')
        return 1
    elif theBoard[7] == theBoard[4] == theBoard[1] != ' ':
        print('Game over!!')
        return 1
    elif theBoard[8] == theBoard[5] == theBoard[2] != ' ':
        print('Game over!!')
        return 1
    elif theBoard[9] == theBoard[6] == theBoard[3] != ' ':
        print('Game over!!')
        return 1
    

win = 0
print('You will be player X, and the computer will be O.')
printBoard(theBoard)
for i in range(10):
    game()
    printBoard(theBoard)
    win = checkWinner(win)
    if win == 1:
        print("Player won! [ X ]")
        break
    elif i == 4:
        print('No one won.....')
        break
    print('''Computer's turn.''')
    computerTurn()
    printBoard(theBoard)
    win = checkWinner(win)
    if win == 1:
        print("Computer won! [ O ]")
        break
    
