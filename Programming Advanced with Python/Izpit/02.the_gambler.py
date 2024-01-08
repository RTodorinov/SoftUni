def print_board(board):
    for row in board:
        print(''.join(row))


def is_inside_board(row, col, size):
    return 0 <= row < size and 0 <= col < size


def play_game(board, start_row, start_col, initial_amount):
    current_row, current_col = start_row, start_col
    amount = initial_amount
    jackpot = False
    is_break = False

    while True:
        command = input()
        board[current_row][current_col] = '-'

        if command == 'end':
            break

        if command == 'up':
            current_row -= 1
        elif command == 'down':
            current_row += 1
        elif command == 'left':
            current_col -= 1
        elif command == 'right':
            current_col += 1

        if not is_inside_board(current_row, current_col, len(board)):
            print("Game over! You left the board!")
            is_break = True
            break

        current_position = board[current_row][current_col]

        if current_position == 'W':
            amount += 100
        elif current_position == 'P':
            amount -= 200
            if amount <= 0:
                print("Game over! You lost everything!")
                board[current_row][current_col] = 'G'
                is_break = True
                break
        elif current_position == 'J':
            amount += 100000
            jackpot = True
            board[current_row][current_col] = 'G'
            break

        board[current_row][current_col] = 'G'

    if jackpot:
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {amount}$")
        board[current_row][current_col] = 'G'
        print_board(board)
    elif is_break:
        pass
    else:
        print(f"End of the game. Total amount: {amount}$")
        board[current_row][current_col] = 'G'
        print_board(board)


# Input
n = int(input())
matrix = [list(input()) for _ in range(n)]

# Find starting position
start_row, start_col = None, None
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'G':
            start_row, start_col = i, j

play_game(matrix, start_row, start_col, 100)
