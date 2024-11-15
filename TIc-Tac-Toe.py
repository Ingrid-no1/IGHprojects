# Initialize the board dynamically
board_size = 3
board_spaces = [[str(i + j * board_size + 1) for i in range(board_size)] for j in range(board_size)]

# Display the board layout
def board_layout():
    print("\n!! TIC-TAC-TOE !!\n")
    for row in board_spaces:
        print(" | ".join(row))
        if row != board_spaces[-1]:
            print("-" * (board_size * 4 - 1))

# Check if a player has won
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(board_size):
        if len(set(board_spaces[i])) == 1:  # Check rows
            return board_spaces[i][0]
        if len(set(row[i] for row in board_spaces)) == 1:  # Check columns
            return board_spaces[0][i]
    # Check diagonals
    if len(set(board_spaces[i][i] for i in range(board_size))) == 1:
        return board_spaces[0][0]
    if len(set(board_spaces[i][board_size - i - 1] for i in range(board_size))) == 1:
        return board_spaces[0][board_size - 1]
    return None

# Check if the board is full
def board_full():
    return all(cell in {"X", "O"} for row in board_spaces for cell in row)

# Validate player input
def get_valid_input(player):
    while True:
        try:
            placement = int(input(f"Player {player}, choose a number (1-{board_size ** 2}): "))
            if placement < 1 or placement > board_size ** 2:
                raise ValueError("Invalid range")
            row, col = divmod(placement - 1, board_size)
            if board_spaces[row][col] in {"X", "O"}:
                print("Spot taken. Try again.")
            else:
                return row, col
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {board_size ** 2}.")

# Play the game
def play_game():
    board_layout()
    current_player = "X"
    while not board_full() and not check_winner():
        row, col = get_valid_input(current_player)
        board_spaces[row][col] = current_player
        board_layout()
        current_player = "O" if current_player == "X" else "X"

    winner = check_winner()
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

# Run the game
play_game()
