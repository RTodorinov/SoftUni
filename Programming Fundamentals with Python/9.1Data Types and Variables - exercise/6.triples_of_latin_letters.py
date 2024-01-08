
n = int(input())

for char1 in range(97, 97 + n):
    for char2 in range(97, 97 + n):
        for char3 in range(97, 97 + n):
            print(f"{chr(char1)}{chr(char2)}{chr(char3)}")


# n = int(input())
# start = 97
# for char1 in range(start, start + n):
#     for char2 in range(start, start + n):
#         for char3 in range(start, start + n):
#             result = f"{chr(char1)}{chr(char2)}{chr(char3)}"
#             print(result)
