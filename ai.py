import board

def hasWon(char, curr_board):
    #get all spaces in whoch player has played
    played_moves = [i for i,x in enumerate(curr_board) if x == char]
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
    for list in winning_positions:
        if(all(move in played_moves for move in list)):
            #print("{} has won!".format(char))
            return True
    return False

def bestMove(curr_board, char, debug=False):
    print("Playing computer move")
    simulation = [x for x in curr_board]
    if char == "O": enemy_char = "X"
    else: enemy_char = "O"

    #Return winning move if it exists
    for i in range(1,10):
        simulation = [x for x in curr_board]
        if(board.updateBoard(simulation, i, char)):
            if hasWon(char, simulation):
                if debug: print("Found winning position")
                return i

    #If winning move does not exist, clear simulation and block enemy's winning move
    for i in range(1,10):
        simulation = [x for x in curr_board]
        if(board.updateBoard(simulation, i, enemy_char)):
            if hasWon(enemy_char, simulation):
                if debug: print("Blocked enemy winning position")
                return i

    #If enemy cannot win on next move, play corner move
    for i in [1,3,9,7]:
        simulation = [x for x in curr_board]
        if(board.updateBoard(simulation, i, char)):
            if debug: print("Playing first corner move avaialable")
            return i

    #If corners are full, play center
    simulation = [x for x in curr_board]
    if(board.updateBoard(simulation,5,char)):
        if debug: print("Playing center")
        return 5

    #If center is full, play edges
    for i in [2,4,6,8]:
        simulation = [x for x in curr_board]
        if(board.updateBoard(simulation)):
            if debug: print("Playing first available edge")
            return i

    if debug: print("algorithm is not catching all cases! error")
    return false
