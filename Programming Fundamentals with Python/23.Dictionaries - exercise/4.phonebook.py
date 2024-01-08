
# phonebook = {}
# n = 0
# while True:
#     contacts = input()
#     parts = contacts.split("-")
#     if len(parts) == 1:
#         n = int(contacts)
#         break
#
#     name = parts[0]
#     number = parts[1]
#     if name not in phonebook:
#         phonebook[name] = number
#
# for _ in range(n):
#     name = input()
#     if name in phonebook:
#         print(f"{name} -> {phonebook[name]}")
#     else:
#         print(f"Contact {name} does not exist.")

phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone_number = entry.split("-")
    phonebook[name] = phone_number  # ще го създаде ако не съществува или ще го презапише ако го има
for search in range(int(entry)):
    searched_name = input()
    if searched_name in phonebook.keys():  # in phonebook
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
