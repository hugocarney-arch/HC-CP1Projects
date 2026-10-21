import random
import time

def print_board(board):
    """Displays the 3x3 grid state clearly in the console."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    """Verifies row, column, and diagonal wins for the given player."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[cell] == player for cell in combo) for combo in win_conditions)

def is_board_full(board):
    """Checks if all spots on the game board are occupied."""
    return all(space in ['X', 'O'] for space in board)

def get_empty_cells(board):
    """Returns a list of available index positions on the board."""
    return [i for i, space in enumerate(board) if space != 'X' and space != 'O']

def make_bot_move(board, bot_marker, human_marker):
    """Executes AI logic by prioritizing wins, blocks, or strategic positions."""
    empty_cells = get_empty_cells(board)
    
    for move in empty_cells:
        board_copy = board.copy()
        board_copy[move] = bot_marker
        if check_win(board_copy, bot_marker):
            return move

    for move in empty_cells:
        board_copy = board.copy()
        board_copy[move] = human_marker
        if check_win(board_copy, human_marker):
            return move

    if 4 in empty_cells:
        return 4

    corners = [0, 2, 6, 8]
    available_corners = [c for c in corners if c in empty_cells]
    if available_corners:
        return random.choice(available_corners)

    return random.choice(empty_cells)

def play_game():
    """Manages the main game loop, player alternating, and win/tie checks."""

    board = [str(i) for i in range(1, 10)]
    human = 'X'
    bot = 'O'
    
    print("Welcome to Tic-Tac-Toe against the Bot!")
    print("You are 'X' and the Bot is 'O'. Select slots using numbers 1-9.")

    current_turn = random.choice([human, bot])
    print(f"{'You get' if current_turn == human else 'The Bot gets'} to go first!")
    print_board(board)
    
    while True:
        if current_turn == human:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move not in range(9) or board[move] in ['X', 'O']:
                    print("Invalid move. Slot is either taken or out of range. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number between 1 and 9.")
                continue
            
            board[move] = human
            print_board(board)
            
            if check_win(board, human):
                print("Congratulations! You beat the bot! ")
                break
        else:
            print("Bot is thinking...")
            time.sleep(1) 
            
            move = make_bot_move(board, bot, human)
            board[move] = bot
            print(f"Bot placed an 'O' in position {move + 1}")
            print_board(board)
            
            if check_win(board, bot):
                print("The bot wins! Better luck next time")
                break
                
        if is_board_full(board):
            print("It's a draw! Well played. ")
            break
            
        current_turn = bot if current_turn == human else human

if __name__ == '__main__':
    play_game()
