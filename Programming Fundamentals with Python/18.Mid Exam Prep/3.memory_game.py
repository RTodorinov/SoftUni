
sequence = input().split()  # ако нямаме аритметически операции взимаме числата като елементи
indexes = input()
number_of_moves = 0

while indexes != "end":

    first_index, second_index = [int(x) for x in indexes.split()]
    number_of_moves += 1
    len_sequence = len(sequence)
    #  проверяваме дали индексите не са извън дължината на листа и дали първия е равен на втория
    if first_index == second_index or not 0 <= first_index < len_sequence or not 0 <= second_index < len_sequence:
        cut_in_half = len_sequence // 2
        element_to_insert = f"-{number_of_moves}a"
        # sequence.insert(cut_in_half, element_to_insert)
        # sequence.insert(cut_in_half, element_to_insert)
        sequence = sequence[:cut_in_half] + [element_to_insert, element_to_insert] + sequence[cut_in_half:]
        print("Invalid input! Adding additional elements to the board")
    elif sequence[first_index] == sequence[second_index]:
        print(f"Congrats! You have found matching elements - {sequence[first_index]}!")
        del sequence[first_index]
        if first_index < second_index:
            second_index -= 1
        del sequence[second_index]
    else:
        print("Try again!")

    if not sequence:
        break

    indexes = input()

if sequence:
    print("Sorry you lose :(")
    print(*sequence)
else:
    print(f"You have won in {number_of_moves} turns!")
