
text = input()
result = ""
for char in text:
    new_char = ord(char) + 3
    result += chr(new_char)

print(result)


# text = input()
# result = "".join([chr(ord(char) + 3) for char in text])
# print(result)
