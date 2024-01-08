
# reversed_words = {}
# while True:
#     string = input()
#     if string == "end":
#         break
#     new_word = string[::-1]
#     reversed_words[string] = new_word
#
# for key, value in reversed_words.items():
#     print(f"{key} = {value}")

word = input()
while word != "end":
    print(f"{word} = {word[::-1]}")
    word = input()
    