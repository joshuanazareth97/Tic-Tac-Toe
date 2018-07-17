import board
import ai
from random import randint

#array to represent 9 spaces on the board. Each can hold " ", "X" or "O"
gameboard = []

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
        s=input("Enter P1's desired symbol X or O: ").upper()
    user['symbol'] = s
    if(s == "O"):
        comp['symbol'] = "X"
    else:
        comp['symbol'] = "O"

def getUserMove(curr_board,player):
    if player == user:
        while(True):
            try:
                pos = int(input("{}'s move (1-9): ".format(player['id'].upper())))
                while not ((pos in range(1,10)) and (board.updateBoard(curr_board,pos,player['symbol']))):
                        pos = int(input("Enter VALID and FREE position (1-9): "))
                break
            except:
                print("Enter valid NUMBER please!")
    elif player == comp:
        move = ai.bestMove(curr_board, player['symbol'])
        board.updateBoard(curr_board, move, player['symbol'])


def game(curr_board):
    current_player = user
    curr_board = board.clearBoard(curr_board)
    board.displayBoard(curr_board)
    while (True):
        if not board.isFree(curr_board): break
        getUserMove(curr_board,current_player)
        board.displayBoard(curr_board)
        if ai.hasWon(current_player['symbol'],curr_board):
            print("{} has won!".format(current_player['symbol']))
            break
        if current_player == user: current_player = comp
        else: current_player = user



wantsToPlay = True
setSymbols()
while (wantsToPlay):
    game(gameboard)
    inp = input("Play Again? (y/n): ").lower()
    wantsToPlay = inp == 'y' or inp == 'yes'
