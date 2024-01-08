# # string = [char for char in input()]
# string = list(input())
# reversed_string = []
# # print("".join(string[::-1]))
# while string:
#     reversed_char = string.pop()
#     reversed_string.append(reversed_char)
#
# print("".join(reversed_string))


string = list(input())

while string:
    print(string.pop(), end="")

# string = list(input())
# reversed_string = []
#
# for i in range(len(string)):
#     reversed_string.append(string.pop())
#
# print("".join(reversed_string))
