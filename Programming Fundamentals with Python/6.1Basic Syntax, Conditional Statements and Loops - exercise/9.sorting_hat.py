
IF_BREAK = False
while True:
    name = input()

    if name == "Welcome!":
        break
    if name == "Voldemort":
        IF_BREAK = True
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

if IF_BREAK:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")

# name = input()
# while name != "Welcome!":
#     if name == "Voldemort":
#         break
#     if len(name) < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif len(name) == 5:
#         print(f"{name} goes to Slytherin.")
#     elif len(name) == 6:
#         print(f"{name} goes to Ravenclaw.")
#     elif len(name) > 6:  # else
#         print(f"{name} goes to Hufflepuff.")
#     name = input()
# if name == "Voldemort":
#     print("You must not speak of that name!")
# else:
#     print("Welcome to Hogwarts.")
