# def main_game_logic():
#     def get_player_position(matrix, player):
#         for row_index, row_data in enumerate(matrix):
#             if player in row_data:
#                 return row_index, row_data.index(player)
#
#     rows, columns = 8, 8
#     current_player, second_player = 'w', 'b'
#     matrix = [input().split(' ') for _ in range(rows)]
#     current_player_position = get_player_position(matrix, current_player)
#     second_player_position = get_player_position(matrix, second_player)
#     current_change, second_change = -1, +1
#     capture_condition, queen_condition = False, False
#
#     while not queen_condition and not capture_condition:
#         current_player_row, current_player_column = current_player_position
#         second_player_row, second_player_column = second_player_position
#
#         current_player_row += current_change
#         current_player_position = (current_player_row, current_player_column)
#
#         if current_player_row == second_player_row and abs(current_player_column - second_player_column) == 1:
#             capture_condition = True
#             current_player_position = (current_player_row, second_player_column)
#         elif current_player_row in [0, rows - 1]:
#             queen_condition = True
#         else:
#             current_player_position, second_player_position = second_player_position, current_player_position
#             current_change, second_change = second_change, current_change
#             current_player, second_player = second_player, current_player
#
#     return current_player_position, current_player, capture_condition
#
#
# def print_function(position_data, player_win, capture_condition):
#     row, column = position_data
#     row_names = [8, 7, 6, 5, 4, 3, 2, 1]
#     column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     position_name = f'{column_names[column]}{row_names[row]}'
#
#     if capture_condition:
#         return f'Game over! {player_win} win, capture on {position_name}.'
#     else:
#         return f'Game over! {player_win} pawn is promoted to a queen at {position_name}.'
#
#
# position_data, current_player, capture_condition = main_game_logic()
# player_win = 'White' if current_player == 'w' else 'Black'
# print(print_function(position_data, player_win, capture_condition))


SIZE = 8

board = []
positions = [[], []]


def save_positions(search_for, index_to_save, row_):
    if search_for in board[row_]:
        positions[index_to_save].append(row_)
        positions[index_to_save].append(board[row_].index(search_for))


for row in range(SIZE):
    board.append(input().split())

    save_positions("w", 0, row)
    save_positions("b", 1, row)

#  print(positions)

if abs(positions[0][1] - positions[1][1]) != 1 or positions[1][0] > positions[0][0]:
    if SIZE - positions[0][0] - 1 <= positions[1][0]:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.")
else:
    place = (positions[0][0] + positions[1][0]) // 2

    if positions[0][0] % 2 == positions[1][0] % 2:
        print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.")
    else:
        print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")

