
def chars_in_range(a, b):
    result = []
    for char in range(ord(a) + 1, ord(b)):
        result.append(chr(char))
    return " ".join(result)


char1 = input()
char2 = input()
print(chars_in_range(char1, char2))

# def all_the_characters(first, second):
#     characters = []
#     for current_character_as_digit in range(ord(first) + 1, ord(second)):
#         characters.append(chr(current_character_as_digit))
#     return characters
#
#
# first_character = input()
# second_character = input()
# result = all_the_characters(first_character, second_character)
# print(" ".join(result))
