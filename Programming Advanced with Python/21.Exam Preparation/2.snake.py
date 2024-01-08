MATRIX_SIZE = int(input())

snake_row, snake_col, lairs, matrix, food_quantity, snake_alive = 0, 0, [], [], [0], [True]
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(MATRIX_SIZE):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        snake_row, snake_col = row, matrix[row].index("S")
    elif "B" in matrix[row]:
        lairs.append([row, matrix[row].index("B")])


def check_valid_index(row_, col_):
    return 0 <= row_ < MATRIX_SIZE and 0 <= col_ < MATRIX_SIZE


def snake_teleport(row_, col_):
    lairs.remove([row_, col_])
    return lairs[0][0], lairs[0][1]


def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


def snake_step(row_, col_, direction_):
    new_row, new_col = movement(row_, col_, direction_)
    if not check_valid_index(new_row, new_col):
        snake_alive[0] = False
        matrix[row_][col_] = "."
        return row_, col_

    step = matrix[new_row][new_col]
    if step == "B":
        matrix[new_row][new_col] = "."
        new_row, new_col = snake_teleport(new_row, new_col)
    elif step == "*":
        food_quantity[0] += 1

    matrix[row_][col_] = "."
    matrix[new_row][new_col] = "S"
    return new_row, new_col


while food_quantity[0] < 10 and snake_alive[0]:
    direction = input()
    if direction in directions:
        snake_row, snake_col = snake_step(snake_row, snake_col, direction)

if snake_alive[0]:
    game_status = "You won! You fed the snake."
else:
    game_status = "Game over!"

print(game_status)
print(f"Food eaten: {food_quantity[0]}")
[print(*row, sep="") for row in matrix]
