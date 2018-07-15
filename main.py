import board
from random import randint

player = {
    'symbol': "", #Either "X" or "O"
    'turn': 1  #Can be 1 (2nd Turn) or 0 (1st Turn)
}

comp = {
    'symbol': "", #Either "X" or "O"
    'turn': 1  #Can be 1 (2nd Turn) or 0 (1st Turn)
}

def setSymbols():
    s=""
    while(s !="X" and s != "O"):
        s=input("Enter desired symbol X or O: ").upper()
    player['symbol'] = s
    if(s == "O"):
        comp['symbol'] = "X"
    else:
        comp['symbol'] = "O"

def setTurn():
    player['turn'] = randint(0,1)
    if(player['turn']): comp['turn'] = 0
    else: comp['turn'] = 1

def getPlayerMove(curr_board):
    pos = int(input("Enter position of your move (1-9): "))
    while not ((pos in range(1,10)) and (board.updateBoard(curr_board,pos,player['symbol']))):
            pos = int(input("Enter position of your move (1-9): "))


def main():
    setSymbols()
    setTurn()
    board.clearBoard(board.board)
    getPlayerMove(board.board)
    board.displayBoard(board.board)
#    if not(player['turn']): #Player Turn = 0 (1st turn)
main()
