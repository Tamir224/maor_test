# Initialize the game board
board = [' ' for _ in range(9)]

# Function to check for a winner
def check_winner():
    # Define winning combinations
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    # Check each winning combination
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True  # We found a winner
    return False  # No winner found

# Display the game board
def display_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

# Main game loop
def play_game():
    current_player = first_player
    while True:
        display_board()
        position = int(input(f'{current_player}, choose your position (1-9): ')) - 1
        if 0 <= position <= 8 and board[position] == ' ':  # Check if the chosen position is valid and empty
            board[position] = 'X' if current_player == first_player else 'O'  # Assign X or O to the chosen position
            if check_winner():  # Check for a winner
                display_board()
                print(f"Congratulations {current_player}, you win!")
                break
            current_player = second_player if current_player == first_player else first_player  # Switch players
        else:
            print('Invalid move. Please choose an empty position between 1 and 9.')

# Start the game
if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    first_player = input('Player 1, enter your name: ')
    second_player = input('Player 2, enter your name: ')
    play_game()

