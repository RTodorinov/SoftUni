
# divisor = int(input())
# boundary = int(input())
#
# max_number = 0
# for j in range(1, boundary + 1):
#
#     if j % divisor == 0:
#         if j >= max_number:
#             max_number = j
#
# print(max_number)

divisor = int(input())
boundary = int(input())

max_number = 0
for j in range(1, boundary + 1):

    if j % divisor == 0:
        max_number = j

print(max_number)

# divisor = int(input())
# boundary = int(input())
# number = 0
# for number in range(boundary, divisor - 1, -1):
#     if number % divisor == 0:
#         break
# print(number)
