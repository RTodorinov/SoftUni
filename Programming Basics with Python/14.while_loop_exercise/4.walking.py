''' Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.
Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня
и когато постигне целта си да се изписва "Goal reached! Good job!"
и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките,
които е извървяла докато се прибира.
След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише:
"{разликата между стъпките} more steps to reach goal." '''

GOAL = 10_000
steps_walked = 0

while steps_walked < GOAL:
    steps = input()  # тук е стринг защото може да имаме "Going home"

    if steps == "Going home":
        steps_walked += int(input())
        break
    steps_walked += int(steps)  # тук сменяме видът на променливата.

if steps_walked >= GOAL:
    print("Goal reached! Good job!")
    print(f"{steps_walked - GOAL} steps over the goal!")

else:
    print(f"{(GOAL - steps_walked)} more steps to reach goal.")
