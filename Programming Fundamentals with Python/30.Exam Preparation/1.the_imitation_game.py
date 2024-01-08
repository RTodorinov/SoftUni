def move(encrypted_message, command):
    number_of_letters = int(command[1])
    first_part = encrypted_message[:number_of_letters]
    second_part = encrypted_message[number_of_letters:]
    encrypted_message = second_part + first_part
    return encrypted_message


def insert(encrypted_message, command):
    index = int(command[1])
    value = command[2]
    first_part = encrypted_message[:index]
    second_part = encrypted_message[index:]
    encrypted_message = first_part + value + second_part
    return encrypted_message


def change_all(encrypted_message, command):
    substring = command[1]
    replacement = command[2]
    while substring in encrypted_message:
        encrypted_message = encrypted_message.replace(substring, replacement)
    return encrypted_message


decrypted_message = input()
current_command = input()
while current_command != "Decode":
    current_command = current_command.split("|")
    action = current_command[0]
    if action == "Move":
        decrypted_message = move(decrypted_message, current_command)

    elif action == "Insert":
        decrypted_message = insert(decrypted_message, current_command)

    elif action == "ChangeAll":
        decrypted_message = change_all(decrypted_message, current_command)

    current_command = input()

print(f"The decrypted message is: {decrypted_message}")


