import board
from random import randint

user = {
    'symbol': "", #Either "X" or "O"
    'id': 'p1'  #Can be 1 (2nd Turn) or 0 (1st Turn)
}

comp = {
    'symbol': "", #Either "X" or "O"
    'id': 'p2'  #Can be 1 (2nd Turn) or 0 (1st Turn)
}


def setSymbols():
    s=""
    while(s !="X" and s != "O"):
        s=input("Enter desired symbol X or O: ").upper()
    user['symbol'] = s
    if(s == "O"):
        comp['symbol'] = "X"
    else:
        comp['symbol'] = "O"

def setTurn():
    dice =  randint(0,1)
    if dice :
        current_player = user
    else:
        current_player = comp

def getUserMove(curr_board,player):
    pos = int(input("{}'s move (1-9): ".format(player['id'].upper())))
    while not ((pos in range(1,10)) and (board.updateBoard(curr_board,pos,player['symbol']))):
            pos = int(input("Enter VALID and FREE position (1-9): "))


def hasWon(player, curr_board):
    #get all spaces in whoch player has played
    played_in = [i for i,x in enumerate(curr_board) if x ==player['symbol']]
    winning_positions = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
    ]
    if played_in in winning_positions:
        print("{} has won!".format(player['id'].upper()))
        return True
    else:
        return False

def main():
    setSymbols()
    current_player = user
    setTurn()
    board.clearBoard(board.board)
    while (not hasWon(current_player,board.board)) and board.isFree(board.board):
        if current_player == user: current_player = comp
        else: current_player = user
        board.displayBoard(board.board)
        getUserMove(board.board,current_player)

    board.displayBoard(board.board)



main()
