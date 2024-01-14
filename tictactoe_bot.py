import tictactoe as t
import random

ai_board_state: list = [" "," "," "," "," "," "," "," "," "] #used by the ai to calculate moves, is changed a lot by the minimax function

def get_human_piece():
    while True:
        human_piece = input("What piece would you like to be? (X/O)").upper()
        if human_piece == "X":
            print("Human goes first.")
            return "X"
        elif human_piece == "O":
            print("AI goes first.")
            return "O"
        else:
            print("Not a valid answer, please input X or O.")
            

def get_ai_move(board:list,ai_piece):
    global ai_board_state
    ai_board_state = board.copy()
    move = minimax(ai_board_state,ai_piece)
    move = move["index"]
    t.print_board(board)
    print("AI's move is " + str(move+1))
    
    return move


def get_empty_squares(board:list):
    empty_squares = []
    for i in range(len(board)): # range is 0 to the length of the board array - 1
        if board[i] == " ":
            empty_squares.append(i)
    return empty_squares


def get_opposite_square(square:int):
    """Takes a square of the tic tac toe board and returns the 
    square opposite. For example, given X, it will return Y
    X| | 
    -+-+-
     | | 
    -+-+-
     | |Y
     
    uses 1-9 coordinates, so x would be 1 and y would be 9
    
    throws an error to prevent it from being used with square = 5
    (the middle square), as that returns 5, and could be confusing
    """
    assert square != 5, "get_opposite_square is equal to 5, which returns 5"
    return 10 - square


def minimax(board:list,current_piece:str):
    AVAILABLE_MOVES = get_empty_squares(board)
    
    if t.has_player_won(board):
        if t.get_winning_player(board) == human_piece:
            return {"score": -1}
        elif t.get_winning_player(board) == ai_piece:
            return {"score": 1}
    elif t.is_game_cat(board):
        return {"score": 0}

    test_results = []
    
    for i in range(len(AVAILABLE_MOVES)):
        current_test_info = {}
        
        current_test_info.update({"index": AVAILABLE_MOVES[i]})
        
        board[AVAILABLE_MOVES[i]] = current_piece
        
        # recursively run minimax algorithm
        if current_piece == ai_piece:
            result = minimax(ai_board_state, human_piece)
            current_test_info.update({"score": result["score"]})
        else: 
            result = minimax(ai_board_state, ai_piece)
            current_test_info.update({"score": result["score"]})
            
        # reset the current board
        board[AVAILABLE_MOVES[i]] = " "
        
        test_results.append(current_test_info)
    
    best_test_result: int
    
    if current_piece == ai_piece:
        best_result = -1000
        for i in range(len(test_results)):
            if test_results[i]["score"] > best_result:
                best_result = test_results[i]["score"]
                best_test_result = i
    else:
        best_result = 1000
        for i in range(len(test_results)):
            if test_results[i]["score"] < best_result:
                best_result = test_results[i]["score"]
                best_test_result = i

    return test_results[best_test_result]
    

if __name__ == "__main__":
    human_piece = get_human_piece()
    ai_piece = ""
    
    if human_piece == "X":
        ai_piece = "O"
        t.game_board[t.get_move(t.game_board, "Human") - 1] = "X"
    else:
        ai_piece = "X"
    
    
    while True:
        t.game_board[get_ai_move(t.game_board, ai_piece)] = ai_piece
        
        if t.has_player_won(t.game_board):
            break
        
        if t.is_game_cat(t.game_board):
            break
        
        t.game_board[t.get_move(t.game_board, "Human") - 1] = human_piece
        
        if t.has_player_won(t.game_board):
            break
        
        if t.is_game_cat(t.game_board):
            break
        
        
    winning_player = t.get_winning_player(t.game_board)
    
    if winning_player == human_piece:
        winning_player = "Human"
    elif winning_player == ai_piece:
        winning_player = "AI"
        
    t.print_board(t.game_board)
    print(winning_player + " wins!")