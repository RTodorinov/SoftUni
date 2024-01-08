
# n = int(input())
# word = input()
# my_list = []
# list_including_word = []
#
# for _ in range(n):
#     current_string = input()
#     my_list.append(current_string)
#
#     if word in current_string:
#         list_including_word.append(current_string)
#
# print(my_list)
# print(list_including_word)

n = int(input())
word = input()
my_list = []

for _ in range(n):
    my_list.append(input())
print(my_list)
filtered = []

for string in my_list:
    if word in string:
        filtered.append(string)
print(filtered)

# number = int(input())
# special_word = input()
# strings = []
# for _ in range(number):
#     string = input()
#     strings.append(string)
# print(strings)
# for idx in range(len(strings) - 1, -1, -1):
#     element = strings[idx]
#     if special_word not in element:
#         strings.remove(element)
# print(strings)
