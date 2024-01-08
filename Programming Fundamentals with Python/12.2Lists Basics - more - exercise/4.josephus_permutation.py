people = input()
circle = [int(x) for x in people.split()]

k = int(input())
executed = []
idx = 0

while circle:
    idx = (idx + k - 1) % len(circle)
    executed.append(circle.pop(idx))

result = "[" + ",".join(map(str, executed)) + "]"
print(result)


# def josephus_permutation(people, k):
#     circle = list(map(int, people.split()))
#     executed = []
#     idx = 0
#
#     while circle:
#         idx = (idx + k - 1) % len(circle)
#         executed.append(circle.pop(idx))
#
#     result = "[" + ",".join(map(str, executed)) + "]"
#     return result
#
#
# people = input()
# k = int(input())
#
# josephus_result = josephus_permutation(people, k)
# print(josephus_result)


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
