def check_index(index_):
    if 0 <= index_ < len(decrypted_spell[0]):
        return True
    print("The spell was too weak.")


def abjuration_spell():
    decrypted_spell[0] = decrypted_spell[0].upper()
    print(decrypted_spell[0])


def necromancy_spell():
    decrypted_spell[0] = decrypted_spell[0].lower()
    print(decrypted_spell[0])


def illusion_spell(index_, letter):
    if check_index(index_):
        decrypted_spell[0] = decrypted_spell[0][:index_] + letter + decrypted_spell[0][index_ + 1:]
        print("Done!")


def divination_spell(first_substring, second_substring):
    if first_substring in decrypted_spell[0]:
        decrypted_spell[0] = decrypted_spell[0].replace(first_substring, second_substring)
        print(decrypted_spell[0])


def alteration_spell(substring):
    if substring in decrypted_spell[0]:
        decrypted_spell[0] = decrypted_spell[0].replace(substring, "", 1)
        print(decrypted_spell[0])


allowed_spells = ["Abracadabra", "Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]
decrypted_spell = [input()]
command = input()

while command != "Abracadabra":
    current_command = command.split()
    if current_command[0] not in allowed_spells:
        print("The spell did not work!")
    else:

        if current_command[0] == "Abjuration":
            abjuration_spell()
        elif current_command[0] == "Necromancy":
            necromancy_spell()
        elif current_command[0] == "Illusion":
            illusion_spell(int(current_command[1]), current_command[2])
        elif current_command[0] == "Divination":
            divination_spell(current_command[1], current_command[2])
        elif current_command[0] == "Alteration":
            alteration_spell(current_command[1])
    command = input()
