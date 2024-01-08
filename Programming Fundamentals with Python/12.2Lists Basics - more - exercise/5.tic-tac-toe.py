# field = []
# for _ in range(3):
#     line = input().split()
#     field.append(list(map(int, line)))
# ''' Here, we're reading the input for the tic-tac-toe field. The field is represented as a list of lists (field),
# where each inner list represents a row in the tic-tac-toe grid. We iterate through each row and split the input line
# into a list of integers using split(), then convert each element to an integer using map(int, line),
#  and finally, append the resulting list to the field.'''
#
#
# def check_winner(player):
#     # Check rows and columns
#     for i in range(3):
#         if all(field[i][j] == player for j in range(3)):
#             return True
#         if all(field[j][i] == player for j in range(3)):
#             return True
#
#     # Check diagonals
#     if all(field[i][i] == player for i in range(3)) or all(field[i][2 - i] == player for i in range(3)):
#         return True
#
#     return False
#
#
# ''' This function check_winner(player) takes a player (either 1 or 2) as an argument
# and checks if that player has won.
# It does this by iterating through the rows and columns of the field and checking if all the values in a row, column,
# or diagonal are equal to the player value.
#
# i is used in the loops to iterate over the rows and diagonals. It takes values from 0 to 2, representing the indices
# of rows and diagonals.
# j is used in the nested loops to iterate over the columns. It also takes values from 0 to 2, representing the indices
# of columns.'''
#
# # Check for both players
# if check_winner(1):
#     print("First player won")
# elif check_winner(2):
#     print("Second player won")
# else:
#     print("Draw!")
#
# ''' Finally, after defining the check_winner function, we use it to determine the outcome of the game.
# We call check_winner with player values 1 and 2 to check if either player has won. If either of them has won,
# we print the corresponding message. If neither player has won and the board is full, we print "Draw!".
#
# In summary, i and j are loop variables used to iterate over the rows, columns,
# and diagonals of the tic-tac-toe grid while checking for a winner.'''

first_row = input().split()
second_row = input().split()
third_row = input().split()
''' We're reading the three lines of input, each representing a row in the tic-tac-toe grid, 
and splitting them into lists of strings.'''

name_player = "First"
found = False

for player in range(1, 3):
    player = str(player)
    line = [player, player, player]
    if line == first_row or second_row == line or third_row == line:  # преверка на редовете
        found = True
    for index in range(0, 3):
        if first_row[index] == player and second_row[index] == player and third_row[index] == player:  # проверка на колоните
            found = True
    if first_row[0] == player and second_row[1] == player and third_row[2] == player:  # ляв диагонал
        found = True
    elif first_row[2] == player and second_row[1] == player and third_row[0] == player:  # десен диагонал
        found = True
    if found:
        print(f"{name_player} player won")
        break
    name_player = "Second"
else:
    print("Draw!")

''' We're then iterating through each player (1 and 2) using a loop. For each player, you're creating a list called 
line that contains three elements of the player's number. We're checking if any row contains all elements equal to 
the player's number, and if so, setting found to True.

Next, we're using nested loops to check for columns where all elements are equal to the player's number. 
Additionally, we're checking for diagonal winning combinations.

If a winning combination is found, we're printing the corresponding player's message and breaking out of the loop.
If no winning combination is found for both players, you print "Draw!"'''
