
# string_one, string_two = input().split()
# total_sum = 0
# if len(string_one) > len(string_two):
#     for index in range(len(string_two)):
#         total_sum += ord(string_one[index]) * ord(string_two[index])
#     for index in range(len(string_two), len(string_one)):
#         total_sum += ord(string_one[index])
# elif len(string_two) > len(string_one):
#     for index in range(len(string_one)):
#         total_sum += ord(string_one[index]) * ord(string_two[index])
#     for index in range(len(string_one), len(string_two)):
#         total_sum += ord(string_two[index])
# else:
#     for index in range(len(string_one)):
#         total_sum += ord(string_one[index]) * ord(string_two[index])
# print(total_sum)


# words = input().split()
# first_word = words[0]
# second_word = words[1]
#
# min_len = min(len(first_word), len(second_word))
# result = 0
# for idx in range(min_len):
#     first_word_char = first_word[idx]
#     second_word_char = second_word[idx]
#     result += ord(first_word_char) * ord(second_word_char)
#
# for idx in range(min_len, len(first_word)):
#     result += ord(first_word[idx])
#
# for idx in range(min_len, len(second_word)):
#     result += ord(second_word[idx])
#
# print(result)


first_word, second_word = input().split()

min_len = min(len(first_word), len(second_word))
result = 0
for idx in range(min_len):
    first_word_char = first_word[idx]
    second_word_char = second_word[idx]
    result += ord(first_word_char) * ord(second_word_char)

result += sum([ord(char) for char in first_word[min_len:]])
result += sum([ord(char) for char in second_word[min_len:]])

print(result)
