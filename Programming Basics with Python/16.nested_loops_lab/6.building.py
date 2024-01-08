# Напишете програма, която извежда на конзолата номерата на стаите в една сграда
# (в низходящ ред), като са изпълнени следните условия:
# •	На всеки четен етаж има само офиси;
# •	На всеки нечетен етаж има само апартаменти;
# •	Всеки апартамент се означава по следния начин
# : А{номер на етажа}{номер на апартамента}, номерата на апартаментите започват от 0;
# •	Всеки офис се означава по следния начин
# : О{номер на етажа}{номер на офиса}, номерата на офисите също започват от 0;
# •	На последният етаж винаги има апартаменти и те са по-големи от останалите,
# затова пред номера им пише 'L', вместо 'А'. Ако има само един етаж, то има само големи апартаменти!
# От конзолата се прочитат две цели числа - броят на етажите и броят на стаите за един етаж.

number_of_floors = int(input())
apartments_per_floor = int(input())

apartment_name = ""
apartment_number = 0

for current_floor in range(number_of_floors, 0, -1):
    for current_apartment in range(apartments_per_floor):
        apartment_number = current_floor * 10 + current_apartment
        if current_floor == number_of_floors:
            apartment_name = f"L{apartment_number}"
        elif current_floor % 2 == 0:
            apartment_name = f"O{apartment_number}"
        elif current_floor % 2 != 0:
            apartment_name = f"A{apartment_number}"

        print(apartment_name, end=" ")
    print()
