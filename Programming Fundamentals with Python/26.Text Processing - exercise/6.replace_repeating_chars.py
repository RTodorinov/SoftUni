
text = input()
final_text = ""
last_character = ""
for char in text:
    if char != last_character:
        final_text += char
        last_character = char
print(final_text)

# text = input()
# result = text[0]
#
# for ch in text:
#     if ch == result[-1]:
#         continue
#     result += ch
# print(result)
