def find_snake(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "S":
                return row, col


def is_valid_move(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


n = int(input())
territory = [list(input()) for _ in range(n)]
snake_row, snake_col = find_snake(territory)
food_quantity = 0
game_over = False
burrows = []

for row in range(n):
    for col in range(n):
        if territory[row][col] == "B":
            burrows.append((row, col))

while True:
    command = input()
    new_row, new_col = snake_row, snake_col

    if command == "up":
        new_row -= 1
    elif command == "down":
        new_row += 1
    elif command == "left":
        new_col -= 1
    elif command == "right":
        new_col += 1

    if not is_valid_move(territory, new_row, new_col):
        game_over = True
        break

    if territory[new_row][new_col] == "-":
        territory[new_row][new_col] = "."
        territory[snake_row][snake_col] = "."
        snake_row, snake_col = new_row, new_col
    elif territory[new_row][new_col] == "*":
        food_quantity += 1
        territory[new_row][new_col] = "."
        territory[snake_row][snake_col] = "."
        snake_row, snake_col = new_row, new_col

    if food_quantity >= 10:
        break

    if (new_row, new_col) in burrows:
        burrows.remove((new_row, new_col))
        burrow_row, burrow_col = burrows[0]
        territory[new_row][new_col] = "."
        snake_row, snake_col = burrow_row, burrow_col
        territory[snake_row][snake_col] = "S"

if game_over:
    print("Game over!")
else:
    territory[snake_row][snake_col] = "S"
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")

for row in territory:
    print("".join(row))
