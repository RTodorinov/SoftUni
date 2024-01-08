
# words = input().split()
# count_by_letter = {}
#
# for word in words:
#     for letter in word:
#         if letter not in count_by_letter:
#             count_by_letter[letter] = 0
#         count_by_letter[letter] += 1
#
# for key, value in count_by_letter.items():
#     print(f"{key} -> {value}")


# words = input().split()
# count_by_letter = {}
#
# for word in words:
#     for letter in word:
#         if letter in count_by_letter:
#             count_by_letter[letter] += 1
#         else:
#             count_by_letter[letter] = 1
#
# # for letter, count in count_by_letter.items():
# #     print(f"{letter} -> {count}")
#
# for letter in count_by_letter:
#     print(f"{letter} -> {count_by_letter[letter]}")

words = [char for char in input() if char != " "]
count_by_letter = {}
for word in words:
    if word not in count_by_letter.keys():
        count_by_letter[word] = 0
    count_by_letter[word] += 1
for letter, count in count_by_letter.items():
    print(f"{letter} -> {count}")
