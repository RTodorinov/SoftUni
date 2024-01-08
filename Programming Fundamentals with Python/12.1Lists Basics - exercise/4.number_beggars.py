
numbers_as_strings = input().split(", ")
count_of_beggars = int(input())
final_list = []
counter_of_index = 0
#  numbers_as_digits = [int(i) for i in numbers_as_strings]
numbers_as_digits = []
for element in numbers_as_strings:
    numbers_as_digits.append(int(element))
while counter_of_index < count_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(counter_of_index, len(numbers_as_digits), count_of_beggars):
        sum_for_current_beggar += numbers_as_digits[current_index]
    counter_of_index += 1
    final_list.append(sum_for_current_beggar)

print(final_list)

# list = input().split(", ")
# list1 = []
# list2 = []
# a = int(input())
# for i in range(a):
#     for j in range(i, len(list), a):
#         list1.append(int(list[j]))
#     list2.append(sum(list1))
#     list1.clear()
# print(list2)

# collect = input()
# collectors = int(input())
#
# collect_list = list(map(int, collect.split(", ")))
#
# collect_final = []
#
# for i in range(collectors):
#     middle_list = collect_list[i::collectors]
#     collect_final.append(sum(middle_list))
#
# print(collect_final)

# numbers = input().split(", ")
# beggars_count = int(input())
#
# beggars = [0] * beggars_count
#
# for idx in range(len(numbers)):
#     beggar_idx = idx % beggars_count
#     num = int(numbers[idx])
#     beggars[beggar_idx] += num
#
# print(beggars)

# numbers = input().split(", ")
# beggars_count = int(input())
#
# beggars = [0] * beggars_count
# pointer = 0
# for idx in range(len(numbers)):
#     num = int(numbers[idx])
#     beggars[pointer] += num
#     pointer += 1
#     if pointer >= beggars_count:
#         pointer = 0
#
# print(beggars)
