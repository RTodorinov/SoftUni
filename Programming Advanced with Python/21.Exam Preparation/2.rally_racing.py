# def create_matrix(size):
#     matrix = []
#     for _ in range(size):
#         data = input().split(' ')
#         matrix.append(data)
#
#     return matrix
#
# def main_game_logic(matrix):
#     car_coordinates = [0, 0]
#     up_tunel_coordinate, down_tunel_coordinate = [(i, matrix[i].index('T')) for i in range(len(matrix)) if 'T' in matrix[i]]
#     distance = 0
#     finish_condition = False
#
#     while True:
#         command = input()
#
#         if command == 'End':
#             matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
#             return matrix, distance, finish_condition
#
#         elif command == 'down':
#             car_coordinates[0] += 1
#         elif command == 'up':
#             car_coordinates[0] -= 1
#         elif command == 'right':
#             car_coordinates[1] += 1
#         elif command == 'left':
#             car_coordinates[1] -= 1
#
#         if matrix[car_coordinates[0]][car_coordinates[1]] == 'T':
#             matrix[car_coordinates[0]][car_coordinates[1]] = '.'
#             if tuple(car_coordinates) == up_tunel_coordinate:
#                 matrix[down_tunel_coordinate[0]][down_tunel_coordinate[1]] = '.'
#                 car_coordinates = [down_tunel_coordinate[0], down_tunel_coordinate[1]]
#             else:
#                 matrix[up_tunel_coordinate[0]][up_tunel_coordinate[1]] = '.'
#                 car_coordinates = [up_tunel_coordinate[0], up_tunel_coordinate[1]]
#
#             distance += 30
#             continue
#
#         elif matrix[car_coordinates[0]][car_coordinates[1]] == 'F':
#             finish_condition = True
#             distance += 10
#             matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
#             return matrix, distance, finish_condition
#
#         distance += 10
#
#
# def print_function(data, racing_number):
#     matrix, distance, finish_condition = data
#
#     if finish_condition:
#         print(f'Racing car {racing_number} finished the stage!')
#     else:
#         print(f'Racing car {racing_number} DNF.')
#
#     print(f'Distance covered {distance} km.')
#     for row in matrix:
#         print(''.join(row))
#
#
# size = int(input())
# racing_number = input()
# matrix = create_matrix(size)
# print_function(main_game_logic(matrix), racing_number)


SIZE = int(input())
racing_number = input()
matrix, tunnel, row, col, kilometers = [], [], 0, 0, 0

for row_ in range(SIZE):
    matrix.append(input().split())

    if "T" in matrix[row_]:
        tunnel.append([row_, matrix[row_].index("T")])

command = input()

while command != "End":

    if command == "up":
        row -= 1
    elif command == "down":
        row += 1

    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    step_on = matrix[row][col]

    if step_on == ".":
        kilometers += 10

    elif step_on == "T":
        kilometers += 30
        matrix[row][col] = "."
        tunnel.remove([row, col])
        row, col = tunnel[0]
        matrix[row][col] = "."

    elif step_on == "F":
        kilometers += 10
        print(f"Racing car {racing_number} finished the stage!")
        break

    command = input()

else:
    print(f"Racing car {racing_number} DNF.")

matrix[row][col] = "C"

print(f"Distance covered {kilometers} km.")
[print(*row, sep="") for row in matrix]
