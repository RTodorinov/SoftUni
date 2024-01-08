
# number = int(input())
# for i in range(1, number + 1):
#     for j in range(0, i):
#         print("*", end="")
#     print()
#
# for k in range(number + 1, 0, -1):
#     for f in range(k, 0, -1):
#         print("*", end="")
#     print()

n = int(input())

for i in range(1, n + 1):
    print(i * '*')

for i in range(n - 1, 0, -1):
    print(i * "*")
