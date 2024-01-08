
digits = ""
text = ""
simbols = ""

string_line = input()
for letter in string_line:
    if letter.isdigit():
        digits += letter
    elif letter.isalpha():
        text += letter
    elif not letter.isalnum():
        simbols += letter
print(digits)
print(text)
print(simbols)
