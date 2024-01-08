
key = int(input())
number_of_lines = int(input())
message = []
for _ in range(number_of_lines):
    letter = input()
    character = ord(letter) + key
    message.append(chr(character))
for element in message:
    print(element, end="")
