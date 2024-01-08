
# characters = input().split(", ")
# values = 0
# ascii_values = dict.fromkeys(characters, int(values))
# for char, value in ascii_values.items():
#     ascii_values[char] += ord(char)
# print(ascii_values)

characters = input().split(", ")
ascii_values = {char: ord(char) for char in characters}
print(ascii_values)
