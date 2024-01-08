
numbers = [int(x) for x in input().split()]
result = sorted([x for x in numbers if x > sum(numbers) / len(numbers)], reverse=True)
if result:
    print(*result[:5])
else:
    print("No")

# result = sorted([x for x in numbers if x > sum(numbers) / len(numbers)])
# print(*result[-5:][-1::-1])


# FIRST_COUNT = 5
#
# numbers = [int(x) for x in input().split()]
# avg_num = sum(numbers) / len(numbers)
# filtered_nums = sorted([x for x in numbers if x > avg_num])  # filter(lambda x: x > avg_num, numbers)
#
# if not filtered_nums:
#     print("No")
# else:
#     # for i in range(FIRST_COUNT):
#     #     if filtered_nums:
#     #         print(filtered_nums.pop(), end=" ")
#     print(*[filtered_nums.pop() for i in range(FIRST_COUNT) if filtered_nums])
