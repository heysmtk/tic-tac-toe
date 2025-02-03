# Creating a play board 3x3
board = [[" " for _ in range(3)] for _ in range(3)]


# Printing play board
def board_print():
    for row in board:
        print("|".join(row))
        print("-" * 5)


# Make move function
def player_move(player, row, col):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("This field is already set, try again!")
        return False


# Function for check rows, cols and diagonals
def check_winner(player):
    # Check rows and cols
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
        
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False


# Function for checking draw game
def game_draw():
    return all(board[i][j] != " " for i in range(3) for j in range(3))
