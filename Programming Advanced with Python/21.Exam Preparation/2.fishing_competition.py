n = int(input())
matrix = [list(input()) for _ in range(n)]
fish_caught = 0
ship_position = None

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            ship_position = (i, j)

fell_into_whirlpool = False

while True:
    command = input()
    if command == "collect the nets":
        break

    row, col = ship_position
    matrix[row][col] = '-'

    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    if not (0 <= row < n):
        row = n - 1 if row < 0 else 0
    if not (0 <= col < n):
        col = n - 1 if col < 0 else 0

    ship_position = (row, col)

    if matrix[row][col] == 'W':
        fell_into_whirlpool = True
        break
    elif matrix[row][col] != '-':
        fish_caught += int(matrix[row][col])
        matrix[row][col] = '-'
        matrix[ship_position[0]][ship_position[1]] = 'S'

if fell_into_whirlpool:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{ship_position[0]},{ship_position[1]}]")
else:
    if fish_caught >= 20:
        matrix[ship_position[0]][ship_position[1]] = 'S'
        print("Success! You managed to reach the quota!")
    else:
        lack_of_fish = 20 - fish_caught
        print(f"You didn't catch enough fish and didn't reach the quota! You need {lack_of_fish} tons of fish more.")
    print(f"Amount of fish caught: {fish_caught} tons.")
    for row in matrix:
        print("".join(row))
