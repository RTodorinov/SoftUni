floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):  # започваме да броим етажите от от най големия надолу
    for room in range(0, rooms):  # броим стаите на етажа
        if floor == floors:  # проверяваме дали е последния етаж
            print(f"L{floor}{room} ", end="")  # принтираме на един ред
            continue
        if floor % 2 == 0:  # проверяваме дали е четна стаята
            print(f"O{floor}{room} ", end="")
        else:
            print(f"A{floor}{room} ", end="")
    print("")  # сваляме на следващия ред за всеки етаж
