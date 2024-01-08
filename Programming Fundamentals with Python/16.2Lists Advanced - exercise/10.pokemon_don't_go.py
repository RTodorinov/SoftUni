#
# sequence_of_integers = [int(x) for x in input().split()]
# removed_list = []
#
# while sequence_of_integers:
#     index = int(input())
#
#     if index < 0:
#         number = sequence_of_integers.pop(0)
#         removed_list.append(number)
#         sequence_of_integers.insert(0, sequence_of_integers[-1])
#         for i in range(len(sequence_of_integers)):
#             if sequence_of_integers[i] <= number:
#                 sequence_of_integers[i] += number
#             else:
#                 sequence_of_integers[i] -= number
#
#     elif index > len(sequence_of_integers) - 1:
#         number = sequence_of_integers.pop(-1)
#         sequence_of_integers.insert(len(sequence_of_integers), sequence_of_integers[0])
#         removed_list.append(number)
#         for i in range(len(sequence_of_integers)):
#             if sequence_of_integers[i] <= number:
#                 sequence_of_integers[i] += number
#             else:
#                 sequence_of_integers[i] -= number
#
#     else:
#         number = sequence_of_integers.pop(index)
#         removed_list.append(number)
#         for i in range(len(sequence_of_integers)):
#             if sequence_of_integers[i] <= number:
#                 sequence_of_integers[i] += number
#             else:
#                 sequence_of_integers[i] -= number
#
# print(sum(removed_list))


def remove_element(current_list, index, removed_list):
    number = current_list.pop(index)
    removed_list.append(number)
    for i in range(len(current_list)):
        if current_list[i] <= number:
            current_list[i] += number
        else:
            current_list[i] -= number
    return current_list, removed_list


def index_less_than_zero(current_list, removed_list):
    number = current_list.pop(0)
    removed_list.append(number)
    current_list.insert(0, current_list[-1])
    for i in range(len(current_list)):
        if current_list[i] <= number:
            current_list[i] += number
        else:
            current_list[i] -= number
    return current_list, removed_list


def index_greater_than_lastone(current_list, removed_list):
    number = current_list.pop(-1)
    current_list.insert(len(current_list), current_list[0])
    removed_list.append(number)
    for i in range(len(current_list)):
        if current_list[i] <= number:
            current_list[i] += number
        else:
            current_list[i] -= number
    return current_list, removed_list


sequence_of_integers = [int(ch) for ch in input().split(" ")]
removed_list = []

while sequence_of_integers:
    index = int(input())

    if index < 0:
        sequence_of_integers, removed_list = index_less_than_zero(sequence_of_integers, removed_list)
    elif index > len(sequence_of_integers) - 1:
        sequence_of_integers, removed_list = index_greater_than_lastone(sequence_of_integers, removed_list)
    else:
        sequence_of_integers, removed_list = remove_element(sequence_of_integers, index, removed_list)

print(sum(removed_list))
