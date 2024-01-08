
# n = int(input())
# for _ in range(n):
#     num = int(input())
#     if num % 2 != 0:
#         print(f"{num} is odd!")
#         break
# else:
#     print("All numbers are even.")

# n = int(input())
# for _ in range(n):
#     num = int(input())
#     if not num % 2 == 0:
#         print(f"{num} is odd!")
#         break
# else:
#     print("All numbers are even.")

# n = int(input())
# all_nums_are_even = True
# for _ in range(n):
#     num = int(input())
#     if num % 2 != 0:
#         all_nums_are_even = False
#         print(f"{num} is odd!")
#         break
# if all_nums_are_even:
#     print("All numbers are even.")

# n = int(input())
# for _ in range(n):
#     num = int(input())
#     if num % 2 != 0:
#         print(f"{num} is odd!")
#         exit()
#
# print("All numbers are even.")
''' в последния случай exit() приключва програмата директно '''

n = int(input())
for _ in range(n):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        break
else:
    print("All numbers are even.")
