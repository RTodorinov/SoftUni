ROWS_COUNT, COLS_COUNT = [int(el) for el in input().split(",")]


def is_in_area(row_, col):
    return 0 <= row_ < ROWS_COUNT and 0 <= col < COLS_COUNT


matrix = []
total_cheese_count = 0
mouse_position = None
eaten_cheese_count = 0

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row_index in range(ROWS_COUNT):
    row_data = list(input())
    if 'M' in row_data:
        col_index = row_data.index('M')
        mouse_position = [row_index, col_index]
    total_cheese_count += row_data.count('C')
    matrix.append(row_data)

direction = input()

while direction != "danger":
    current_row, current_col = mouse_position
    row_to_go, col_to_go = direction_mapper[direction]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    if not is_in_area(desired_row, desired_col):
        print("No more cheese for tonight!")
        break
    if matrix[desired_row][desired_col] == "C":
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        eaten_cheese_count += 1
        mouse_position = [desired_row, desired_col]

        if eaten_cheese_count == total_cheese_count:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[desired_row][desired_col] == "T":
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        print("Mouse is trapped!")
        break
    elif matrix[desired_row][desired_col] == "@":
        direction = input()
        continue
    else:
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        mouse_position = [desired_row, desired_col]

    direction = input()

else:
    print("Mouse will come back later!")

for row in matrix:
    print(*row, sep='')


# def is_valid_idx(row, col):
#     return 0 <= row < N and 0 <= col < M
#
#
# N, M = (int(el) for el in input().split(","))
# moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
# cupboard = []
# mouse_r, mouse_c = 0, 0
# cheese_count = 0
# eaten_cheese = 0
#
# for r in range(N):
#     cupboard.append(list(input()))
#     for c in range(M):
#         if cupboard[r][c] == "M":
#             mouse_r, mouse_c = r, c
#         elif cupboard[r][c] == "C":
#             cheese_count += 1
#
# direction = input()
#
# while direction != "danger":
#     new_row = mouse_r + moves[direction][0]
#     new_col = mouse_c + moves[direction][1]
#
#     if not is_valid_idx(new_row, new_col):
#         print("No more cheese for tonight!")
#         break
#     elif cupboard[new_row][new_col] == "C":
#         cupboard[new_row][new_col] = "M"
#         cupboard[mouse_r][mouse_c] = "*"
#         mouse_r, mouse_c = new_row, new_col
#         eaten_cheese += 1
#         if eaten_cheese == cheese_count:
#             print("Happy mouse! All the cheese is eaten, good night!")
#             break
#     elif cupboard[new_row][new_col] == "T":
#         cupboard[new_row][new_col] = "M"
#         cupboard[mouse_r][mouse_c] = "*"
#         print("Mouse is trapped!")
#         break
#     elif cupboard[new_row][new_col] == "@":
#         pass
#     else:
#         cupboard[new_row][new_col] = "M"
#         cupboard[mouse_r][mouse_c] = "*"
#         mouse_r, mouse_c = new_row, new_col
#
#     direction = input()
#
# if direction == "danger":
#     print("Mouse will come back later!")
#
# [print(*row, sep="") for row in cupboard]
