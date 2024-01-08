first_char = input()
second_char = input()
excluded_char = input()

first_number = ord(first_char)
second_number = ord(second_char)
excluded_number = ord(excluded_char)

counter = 0

for fn in range(first_number, second_number + 1):
    for sn in range(first_number, second_number + 1):
        for tn in range(first_number, second_number + 1):
            if fn == excluded_number or sn == excluded_number or tn == excluded_number:
                continue

            combination = f"{chr(fn)}{chr(sn)}{chr(tn)}"
            counter += 1

            print(combination, end=" ")
print(counter)
