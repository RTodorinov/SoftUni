# variant 1
# unique_numbers = [int(x) for x in input().split()]
# # unique_numbers = list(map(int, input().split()))
# target_number = int(input())
#
# for i in range(len(unique_numbers)):
#     for j in range(i + 1, len(unique_numbers)):
#         if unique_numbers[i] + unique_numbers[j] == target_number:
#             print(f"{unique_numbers[i]} + {unique_numbers[j]} = {target_number}")


# variant 2

unique_numbers = [int(x) for x in input().split()]
target_number = int(input())

targets = set()
values_map = {}

for value in unique_numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f"{pair} + {value} = {target_number}")
    else:
        resulting_number = target_number - value
        targets.add(resulting_number)
        values_map[resulting_number] = value
