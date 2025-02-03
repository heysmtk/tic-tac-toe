from modules.functions import *


def run_game():
    current_player = "X"
    board_print()


    while True:
        try:
            row, col = map(int, input(f"Player {current_player} insert row and column (0-2): ").split())
        except ValueError:
            print("Invalid input, set two number separated by space!")
            continue

        # Checking for valid move
        if row not in range(3) or col not in range(3):
            print("Invalid coordinates! Set number between 0 and 2!")
            continue

        if player_move(current_player, row, col):
            board_print()

            if check_winner(current_player):
                print(f"Player {current_player} wins!")
                break

            if game_draw():
                print("No one wins, game draw!")
                break

            # Player switch
            current_player = "O" if current_player == "X" else "X"


# Run a game
run_game()