'''
Гошо работи в ресторант и отговаря за зареждането на съдомиялната накрая на деня.
Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки
от препарат за съдомиялна е достатъчно, за да измие определено количество съдове.
Знае се, че всяка бутилка съдържа 750 мл. препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.
Приемете, че на всяко трето зареждане със съдове, съдомиялната се пълни само с тенджери,
а останалите пъти с чинии. Докато не получите команда "End" ще продължите да получавате бройка съдове,
които трябва да бъдат измити.
От конзолата се четат:
•	Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10]
На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се изчерпи,
брой съдове, които трябва да бъдат измити - цяло число в интервала [1…100]
Изход
В случай, че количеството препарат е било достатъчно за измиването на съдовете:
"Detergent was enough!"
"{брой чисти чинии} dishes and {брой чисти тенджери} pots were washed."
"Leftover detergent {количество останал препарат} ml."
В случай, че количеството препарат не е било достатъчно за измиването на съдовете:
"Not enough detergent, {количество не достигнал препарат} ml. more necessary!"
'''

bottles_count = int(input())

total_detergent = bottles_count * 750
dish = 5
pot = 15
total_dishes, total_pots = 0, 0
cycle = 1

while True:
    dishes = input()
    if dishes == "End":
        break

    new_dishes = int(dishes)
    dishes, pots = 0, 0
    if cycle % 3 == 0:
        pots = new_dishes
        detergent = pot
    else:
        dishes = new_dishes
        detergent = dish

    total_detergent -= detergent * new_dishes
    if total_detergent < 0:
        print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
        exit()
    total_pots += pots
    total_dishes += dishes
    cycle += 1
print("Detergent was enough!")
print(f"{total_dishes} dishes and {total_pots} pots were washed.")
print(f"Leftover detergent {total_detergent} ml.")
