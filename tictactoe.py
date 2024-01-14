
game_board: list = [" "," "," "," "," "," "," "," "," "]

winning_player = ""

winning_lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] # Row, Row, Row, Column, Column, Column, Diagonal, Diagonal

def print_board(board:list):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])


def is_move_legal(board:list, move:int):
    if board[move - 1] == " ":
        return True
    else:
        return False
    
    
def has_player_won(board: list):
    # Remember zero-based indexing
    
    for line in winning_lines:
        if board[line[0]] != " " and board[line[0]] == board[line[1]] == board[line[2]]:
            return True
            
    return False


def get_winning_player(board: list):
    for line in winning_lines:
        if board[line[0]] != " " and board[line[0]] == board[line[1]] == board[line[2]]:
            if board[line[0]] == "X":
                return "X"
            else: return "O"
    
    return "Neither player"


def is_game_cat(board:list):
    if has_player_won(board):
        return False
    
    for square in board:
        if square == " ":
            return False
    
    return True
    

def get_move(board:list, player:str):
    move = None
    while move == None:
        print_board(board)
        
        move = int(input("What is " + player + "'s move (1-9)?"))
        if not is_move_legal(board,move):
            print("That is not a legal move, try again")
            move = None
    
    return move
    

if __name__ == "__main__":
    while True:
        game_board[get_move(game_board,"X") - 1] = "X"
        
        if has_player_won(game_board):
            break
        
        if is_game_cat(game_board):
            break
        
        game_board[get_move(game_board,"O") - 1] = "O"
        
        if has_player_won(game_board):
            break
        
        if is_game_cat(game_board):
            break
    
    winning_player = get_winning_player(game_board)
    print_board(game_board)
    print(winning_player + " wins!")