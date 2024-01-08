# numbers = [n for n in input().split()]
# string_text = input()
#
# msg_show = ""
# for num in numbers:
#     find_index = sum([int(s_num) for s_num in num])
#     if find_index >= len(string_text):
#         find_index = find_index - len(string_text)
#     msg_show += string_text[find_index]
#     string_text = string_text[:find_index] + string_text[find_index + 1:]
#
# print(msg_show)

# sequence_of_numbers = [int(num) for num in input().split()]
#
# first_car = len(sequence_of_numbers) // 2
#
# first_car_score = sum([num if num != 0 else -sum(sequence_of_numbers[:first_car][:pos]) * 0.2 for pos, num in
#                        enumerate(sequence_of_numbers[:first_car])])
# second_car_score = sum([num if num != 0 else -sum(sequence_of_numbers[::-1][:first_car][:pos]) * 0.2 for pos, num in
#                     enumerate(sequence_of_numbers[::-1][:first_car])])
#
# if first_car_score < second_car_score:
#     print(f"The winner is left with total time: {first_car_score:.1f}")
# else:
#     print(f"The winner is right with total time: {second_car_score:.1f}")


# sequence_of_timers = input().split()
# timers_as_integers = []
# for timer in sequence_of_timers:
#     timers_as_integers.append(int(timer))
# middle_timer = len(timers_as_integers)//2
# left_side = timers_as_integers[0:middle_timer]
# right_side = timers_as_integers[middle_timer+1:][::-1]
#
# left_time = 0
# right_time = 0
# for seconds in left_side:
#     left_time += seconds
#     if seconds == 0:
#         left_time -= 0.2*left_time
# for seconds2 in right_side:
#     right_time += seconds2
#     if seconds2 == 0:
#         right_time -= 0.2 * right_time
#
# if left_time > right_time:
#     print(f'The winner is right with total time: {right_time:.1f}')
# elif left_time<right_time:
#     print(f'The winner is left with total time: {left_time:.1f}')
#

# main_list = input().split()
# skip_number_k = int(input())
#
# final_numbers = list()
# pos = skip_number_k - 1
# index = 0
# len_list = (len(main_list))
#
# while len_list > 0:
#     index = (pos + index) % len_list
#     final_numbers.append(main_list.pop(index))
#     len_list -= 1
#
#
# print(f"[{','.join(final_numbers)}]")

