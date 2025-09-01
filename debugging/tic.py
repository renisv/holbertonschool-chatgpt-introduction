#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]  # Return the winning player

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]  # Return the winning player

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]  # Return the winning player

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]  # Return the winning player

    return None  # No winner yet

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Get valid row input
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                if 0 <= row <= 2:
                    break
                else:
                    print("Invalid row! Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input! Please enter a number (0, 1, or 2).")
        
        # Get valid column input
        while True:
            try:
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if 0 <= col <= 2:
                    break
                else:
                    print("Invalid column! Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input! Please enter a number (0, 1, or 2).")
        
        # Check if spot is available
        if board[row][col] == " ":
            board[row][col] = player
            
            # Check for winner
            winner = check_winner(board)
            if winner:
                print_board(board)
                print("Player " + winner + " wins!")
                break
            
            # Check for draw
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Switch players
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()