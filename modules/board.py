# Creating a play board 3x3
board = [[" " for _ in range(3)] for _ in range(3)]


# Printing play board
def board_print():
    for row in board:
        print("|".join(row))
        print("-" * 5)