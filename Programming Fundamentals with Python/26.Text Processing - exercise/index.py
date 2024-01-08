# 1

def length_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def characters_are_valid(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(username):
    if " " in username:
        return False
    return True


def username_is_valid(username):
    if length_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)

# 2

first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    # We have multiplication here
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else:  # len(second_string) == len(first_string)
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
print(total_sum)

# 3

filename_plus_extension = input().split("\\")
filename, extension = filename_plus_extension[-1].split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")

# 4

initial_message = input()
encrypted_message = ""
for character in initial_message:
    encrypted_character = chr(ord(character) + 3)
    encrypted_message += encrypted_character
print(encrypted_message)

# 5

single_string = input()
for index in range(len(single_string)):
    if single_string[index] == ":":
        print(f":{single_string[index + 1]}")

# 6

text = input()
final_text = ""
last_character = ""
for current_character in text:
    if current_character != last_character:
        final_text += current_character
        last_character = current_character
print(final_text)

# 7

some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    elif some_string[index] == ">":
        final_string += some_string[index]  # final_string += ">"
        strength += int(some_string[index + 1])
    else:
        final_string += some_string[index]
print(final_string)

# 9

text = input().upper()
unique_symbols = ""
current_symbol = ""
repetitions = ""
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else:  # text[index] is digit -> working with repetitions
        for next_symbols_index in range(index, len(text)):
            if not text[next_symbols_index].isdigit():
                break
            repetitions += text[next_symbols_index]
        unique_symbols += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)


# 10

def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbols_repetition = match_symbol * uninterrupted_match_length
            if winning_symbols_repetition in left_part and winning_symbols_repetition in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(check_ticket(ticket))
