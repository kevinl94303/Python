"""
Name: Kevin Li
UNI: krl2134
game_of_life takes a board which is a 2 dimensional matrix and returns the 
board which is the next step according to the rules of conway's game of life.
neighbors is a helper function.

"""
import copy

def game_of_life(board):
    next_board = copy.deepcopy(board)
    #deep copies board to copy all elements by value
    for y in range (0,len(board)):
        for x in range(0,len(board[y])):
            if board[y][x] == "X":
                if neighbors(board,x,y) < 2 or neighbors(board,x,y) > 3:
                    next_board[y][x] = " "
                else:
                    next_board[y][x] = "X"
            if board[y][x] == " ":
                if neighbors(board,x,y) == 3:
                    next_board[y][x] = "X"
                else:
                    next_board[y][x] = " "
            
    return next_board
    
def neighbors(b,x,y):
    #checks the number of live neighbors for cell x,y in board b
    #checks bounds of x and y to ensure neighbor is in boundaries
    live_neighbors = 0
    if y > 0 and x > 0 and b[y-1][x-1] == "X":
        live_neighbors += 1
    if y > 0 and b[y-1][x] == "X":
        live_neighbors += 1
    if y > 0 and x < len(b[y-1]) - 1 and b[y-1][x+1] == "X":
        live_neighbors += 1
    if x > 0 and b[y][x-1] == "X":
        live_neighbors += 1
    if x < len(b[y]) - 1 and b[y][x+1] == "X":
        live_neighbors += 1
    if y < len(b) - 1 and x > 0 and b[y+1][x-1] == "X":
        live_neighbors += 1
    if y < len(b) - 1 and b[y+1][x] == "X":
        live_neighbors += 1
    if y < len(b) - 1 and x < len(b[y+1]) - 1 and b[y+1][x+1] == "X":
        live_neighbors += 1
    return live_neighbors


if __name__ == '__main__':

    inp_board = [
            [" "," "," "," "," "],
            [" "," "," "," "," "],
            [" ","X","X","X"," "],
            [" "," "," "," "," "],
            [" "," "," "," "," "]
    ]

    out_board = [
            [" "," "," "," "," "],
            [" "," ","X"," "," "],
            [" "," ","X"," "," "],
            [" "," ","X"," "," "],
            [" "," "," "," "," "]
    ]

    print("Input Board:", inp_board)
    print("Your next board:", game_of_life(inp_board))
    print("Expected next board:", out_board)

    print("Input Board:", out_board)
    print("Your next board:", game_of_life(out_board))
    print("Expected next board:", inp_board)
