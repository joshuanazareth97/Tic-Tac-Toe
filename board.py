# Contains the board array and the methods used to access and update the same

board = [" "]*10 #array to represent 9 spaces on the board. Each can hold " ", "X" or "O"

#function to print the board array in human readable form
def displayBoard(board):
    print("|", end=" ")
    for space in board[7:]:
        print(space + " | ", end = "")
    print("")
    print("|", end=" ")
    for space in board[4:7]:
        print(space + " | ", end ="")
    print("")
    print("|", end=" ")
    for space in board[1:4]:
        print(space + " | ", end = "")
    print("")

#check for free space
def isFree(board, n = None):
    if n==None:
        for i in board[1:]:
            if i ==" ": return True
        print("Board is full!")
        return False
    if (board[n] == " "):
        return True
    else:
        return False

#update board only if that position is free
def updateBoard(board, n, char):
    if isFree(board, n):
        board[n] = char
        return True
    else:
        print("That space on the board is not free!")
        return False

def clearBoard(board):
    board = [" "]*10
    board[0] = 9

if __name__ == "__main__":
    print("This script must be imported into another to use properly!")
