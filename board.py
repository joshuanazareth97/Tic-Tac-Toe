# Contains the board array and the methods used to access and update the same

board = ["X"]*10 #array to represent 9 spaces on the board. Each can hold " ", "X" or "O"

print(board)

#function to print the board array in human readable form
def displayBoard(board):
    print("|", end=" ")
    for space in board[9:6:-1]:
        print(space + " | ", end = "")
    print("")
    print("|", end=" ")
    for space in board[6:3:-1]:
        print(space + " | ", end ="")
    print("")
    print("|", end=" ")
    for space in board[3:0:-1]:
        print(space + " | ", end = "")
    print("")

#check for free space
def isFree(board, n):
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


if __name__ == "__main__":
    board[5] = " "
    updateBoard(board,5,"O")
    displayBoard(board)
